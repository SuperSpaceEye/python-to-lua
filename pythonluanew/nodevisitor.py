import ast
from ast import *
import copy
import builtins

from .binopdesc import BinaryOperationDesc
from .boolopdesc import BooleanOperationDesc
from .cmpopdesc import CompareOperationDesc
from .nameconstdesc import NameConstantDesc
from .unaryopdesc import UnaryOperationDesc
from .loopcounter import LoopCounter

from .context import *
from .config import *

# https://stackoverflow.com/questions/30081275/why-is-1000000000000000-in-range1000000000000001-so-fast-in-python-3?rq=1
# https://stackoverflow.com/questions/8608587/finding-the-source-code-for-built-in-python-functions

class NodeVisitor(ast.NodeVisitor):
    LUACODE = "[[luacode]]"
    def __init__(self, context:Context=None, config:Config=None):
        self.context = context if context is not None else Context()
        self.config = config if config is not None else Config()

        self.output = []
        pass

    def emit(self, data):
        self.output.append(data)

    def visit_all(self, nodes, inline=False):
        if not inline:
            self.context.var_ctx.push()

        visitor = NodeVisitor(self.context, self.config)

        if isinstance(nodes, list):
            for node in nodes:
                visitor.visit(node)
            if not inline:
                self.output.append(visitor.output)
        else:
            visitor.visit(nodes)
            if not inline:
                self.output.extend(visitor.output)

        if not inline:
            self.context.var_ctx.pop()

        if inline:
            return " ".join(visitor.output)

    def generic_visit(self, node: AST):
        raise RuntimeError(f"Unknown node: {node}")

    def visit_Module(self, node: Module):
        self.visit_all(node.body)
        self.output = self.output[0]
    def visit_FunctionDef(self, node: FunctionDef):
        self.context.var_ctx.push()

        last_ctx = self.context.last()

        name = node.name
        self.context.var_ctx.add(VarItem(name, "fn"))

        if last_ctx["class_name"]:
            name = ".".join([last_ctx["class_name"], name])

        arguments = [arg.arg for arg in node.args.args]

        for arg in node.args.args:
            self.context.var_ctx.add(VarItem(arg.arg, "var"))

        if node.args.vararg is not None:
            arguments.append("...")

        local_keyword = ""

        if "." not in name and not self.context.var_ctx.exists(name):
            local_keyword = "local "
            self.context.var_ctx.add(VarItem(name, "var"))

        function_def = f"{local_keyword}function {name}({', '.join(arguments)})"

        self.emit(function_def)

        self.context.push({"class_name": ""})

        self.visit_all(node.body)

        self.context.pop()
        self.context.var_ctx.pop()

        body = self.output[-1]

        if node.args.vararg is not None:
            line = f"local {node.args.vararg.arg} = list {{{{...}}}}"
            body.insert(0, line)

        arg_index = -1
        for i in reversed(node.args.defaults):
            line = "{name} = {name} or {value}"

            arg = node.args.args[arg_index]
            values = {
                "name": arg.arg,
                "value": self.visit_all(i, inline=True),
            }
            body.insert(0, line.format(**values))

            arg_index -= 1

        self.emit("end")

        for decorator in reversed(node.decorator_list):
            decorator_name = self.visit_all(decorator, inline=True)
            line = f"{name}_DECORATOR = {name}; " \
                   f"{name} = function() return {decorator_name}({name}_DECORATOR) end"
            self.emit(line)
    def visit_AsyncFunctionDef(self, node: AsyncFunctionDef):
        raise NotImplementedError("Async function def")
    def visit_ClassDef(self, node: ClassDef):
        bases = [self.visit_all(base, inline=True) for base in node.bases]

        local_keyword = ""
        last_ctx = self.context.last()
        self.context.var_ctx.push()

        if not last_ctx["class_name"] and not self.context.var_ctx.exists(node.name):
            local_keyword = "local "
            self.context.var_ctx.add(node.name)

        name = node.name
        if last_ctx["class_name"]:
            name = ".".join([last_ctx["class_name"], name])

        values = {
            "local": local_keyword,
            "name": name,
            "node_name": node.name,
        }

        self.emit("{local}{name} = class(function({node_name})".format(**values))

        self.context.push({"class_name": node.name})
        self.visit_all(node.body)

        self.context.pop()
        self.context.var_ctx.pop()

        self.output[-1].append("return {node_name}".format(**values))

        self.emit("end, {{{}}})".format(", ".join(bases)))

        # Return class object only in the top-level classes.
        # Not in the nested classes.
        if self.config["class"]["return_at_the_end"] and not last_ctx["class_name"]:
            self.emit("return {}".format(name))
    def visit_Return(self, node: Return):
        line = "return "
        line += self.visit_all(node.value, inline=True)
        self.emit(line)
    def visit_Delete(self, node: Delete):
        targets = [self.visit_all(target, inline=True) for target in node.targets]
        nils = ["nil" for _ in targets]
        line = "{targets} = {nils}".format(targets=", ".join(targets),
                                           nils=", ".join(nils))
        self.emit(line)
    def visit_Assign(self, node: Assign):
        target = self.visit_all(node.targets[0], inline=True)
        value = self.visit_all(node.value, inline=True)

        local_keyword = ""

        last_ctx = self.context.last()

        if last_ctx["class_name"]:
            target = ".".join([last_ctx["class_name"], target])

        # print(self.context.var_ctx.exists(target), target)
        if "." not in target and not self.context.var_ctx.exists(target):
            local_keyword = "local "
            self.context.var_ctx.add(VarItem(target, "var"))

        self.emit("{local}{target} = {value}".format(local=local_keyword,
                                                     target=target,
                                                     value=value))
    def visit_AugAssign(self, node: AugAssign):
        operation = BinaryOperationDesc.OPERATION[node.op.__class__]

        target = self.visit_all(node.target, inline=True)

        self.context.var_ctx.add(VarItem(target, "var"))

        values = {
            "left": target,
            "right": self.visit_all(node.value, inline=True),
            "operation": operation["value"],
        }

        line = "({})".format(operation["format"])
        line = line.format(**values)

        self.emit("{target} = {line}".format(target=target, line=line))
    def visit_AnnAssign(self, node: AnnAssign):
        target = self.visit_all(node.targets[0], inline=True)
        value = self.visit_all(node.value, inline=True)

        local_keyword = ""

        last_ctx = self.context.last()

        if last_ctx["class_name"]:
            target = ".".join([last_ctx["class_name"], target])

        # print(self.context.var_ctx.exists(target), target)
        if "." not in target and not self.context.var_ctx.exists(target):
            local_keyword = "local "
            self.context.var_ctx.add(VarItem(target, "var"))

        self.emit("{local}{target} = {value}".format(local=local_keyword,
                                                     target=target,
                                                     value=value))
    def visit_For(self, node: For):
        """Visit for loop"""
        line = "for {target} in {iter} do"

        continue_label = LoopCounter.get_next()
        self.context.push({
            "loop_label_name": continue_label,
        })
        self.context.var_ctx.push()

        values = {
            "target": self.visit_all(node.target, inline=True),
            "iter": self.visit_all(node.iter, inline=True),
        }
        targets = values["target"].split(", ")
        for t in targets:
            self.context.var_ctx.add(VarItem(t, "var"))

        self.emit(line.format(**values))

        # if self.config.no_jumps and node in self.config.continue_nodes:
        #     idx = self.continue_nodes.index(node)
        #
        #     self.names = list(tuple(self.names))
        #     self.names = list(
        #         tuple(v for v in set(self.names) if v not in vars(builtins) and v not in self.config.core_prefix))
        #     fn_data = copy.deepcopy(self.precompiled_parts[idx][0][2]) + "("
        #     for i, item in enumerate(self.precompiled_parts[idx][0][1]):
        #         if item in self.names:
        #             fn_data += item
        #         else:
        #             fn_data += "0"
        #         if i != len(self.precompiled_parts[idx][0][1]) - 1:
        #             fn_data += ","
        #     fn_data += ")"
        #
        #     self.emit([fn_data])
        # else:
        self.visit_all(node.body)

        self.context.pop()
        self.context.var_ctx.pop()

        if not self.config.no_jumps:
            self.output[-1].append("::{}::".format(continue_label))

        self.emit("end")
    def visit_AsyncFor(self, node: AsyncFor):
        raise NotImplementedError("Async for")
    def visit_While(self, node: While):
        test = self.visit_all(node.test, inline=True)

        self.emit("while {} do".format(test))

        continue_label = LoopCounter.get_next()
        self.context.push({
            "loop_label_name": continue_label,
        })
        self.context.var_ctx.push()

        self.visit_all(node.body)

        self.context.pop()
        self.context.var_ctx.pop()

        if not self.config.no_jumps:
            self.output[-1].append("::{}::".format(continue_label))

        self.emit("end")
    def visit_If(self, node: If):
        test = self.visit_all(node.test, inline=True)

        line = "if {} then".format(test)

        self.emit(line)
        self.visit_all(node.body)

        if node.orelse:
            if isinstance(node.orelse[0], ast.If):
                elseif = node.orelse[0]
                elseif_test = self.visit_all(elseif.test, inline=True)

                line = "elseif {} then".format(elseif_test)
                self.emit(line)

                output_length = len(self.output)
                self.visit_If(node.orelse[0])

                del self.output[output_length]
                del self.output[-1]
            else:
                self.emit("else")
                self.visit_all(node.orelse)

        self.emit("end")
    def visit_With(self, node: With):
        self.emit("do")

        self.visit_all(node.body)

        body = self.output[-1]
        lines = []
        for i in node.items:
            line = ""
            if i.optional_vars is not None:
                line = "local {} = "
                line = line.format(self.visit_all(i.optional_vars,
                                                  inline=True))
            line += self.visit_all(i.context_expr, inline=True)
            lines.append(line)

        for line in lines:
            body.insert(0, line)

        self.emit("end")
    def visit_AsyncWith(self, node: AsyncWith):
        raise NotImplementedError("async with")
    def visit_Raise(self, node: Raise):
        raise NotImplementedError("raise")
    def visit_Try(self, node: Try):
        raise NotImplementedError("try except")
    def visit_Assert(self, node: Assert):
        raise NotImplementedError("assert")
    def visit_Import(self, node: Import):
        line = 'local {asname} = require "{name}"'
        values = {"asname": "", "name": ""}

        if node.names[0].name == self.config.core_pathname:
            return

        if node.names[0].asname is None:
            values["name"] = node.names[0].name
            values["asname"] = values["name"]
            values["asname"] = values["asname"].split(".")[-1]
        else:
            values["asname"] = node.names[0].asname
            values["name"] = node.names[0].name

        self.emit(line.format(**values))
    def visit_ImportFrom(self, node: ImportFrom):
        # print("here")
        # line = f"require {name}"
        raise NotImplementedError("import from is not implemented")

    def visit_Global(self, node: Global):
        raise NotImplementedError("global")
        # for name in node.names:
        #     self.context.var_ctx.add(VarItem(name, "var"))
    def visit_Nonlocal(self, node: Nonlocal):
        raise NotImplementedError("nonlocal")
    def visit_Expr(self, node: Expr):
        expr_is_docstring = False
        if isinstance(node.value, ast.Str):
            expr_is_docstring = True

        self.context.push({"docstring": expr_is_docstring})
        output = self.visit_all(node.value)
        self.context.pop()

        self.output.append(output)
    def visit_Pass(self, node: Pass) :pass
    def visit_Break(self, node: Break):
        self.emit("break")
    def visit_Continue(self, node: Continue):
        last_ctx = self.context.last()

        if self.config.no_jumps:
            raise RuntimeError("Continue can't be used")
            # self.emit("return")
            return

        line = "goto {}".format(last_ctx["loop_label_name"])
        self.emit(line)
    def visit_Slice(self, node: Slice) :pass
    def visit_BoolOp(self, node: BoolOp):
        operation = BooleanOperationDesc.OPERATION[node.op.__class__]
        line = "({})".format(operation["format"])
        values = {
            "left": self.visit_all(node.values[0], True),
            "right": self.visit_all(node.values[1], True),
            "operation": operation["value"],
        }

        self.emit(line.format(**values))
    def visit_BinOp(self, node: BinOp):
        operation = BinaryOperationDesc.OPERATION[node.op.__class__]
        line = "({})".format(operation["format"])
        values = {
            "left": self.visit_all(node.left, True),
            "right": self.visit_all(node.right, True),
            "operation": operation["value"],
        }

        self.emit(line.format(**values))
    def visit_UnaryOp(self, node: UnaryOp):
        operation = UnaryOperationDesc.OPERATION[node.op.__class__]
        value = self.visit_all(node.operand, inline=True)

        line = operation["format"]
        values = {
            "value": value,
            "operation": operation["value"],
        }

        self.emit(line.format(**values))
    def visit_Lambda(self, node: Lambda):
        line = "function({arguments}) return"

        arguments = [arg.arg for arg in node.args.args]

        function_def = line.format(arguments=", ".join(arguments))

        output = []
        output.append(function_def)
        output.append(self.visit_all(node.body, inline=True))
        output.append("end")

        self.emit(" ".join(output))
    def visit_IfExp(self, node: IfExp):
        line = "{cond} and {true_cond} or {false_cond}"
        values = {
            "cond": self.visit_all(node.test, inline=True),
            "true_cond": self.visit_all(node.body, inline=True),
            "false_cond": self.visit_all(node.orelse, inline=True),
        }

        self.emit(line.format(**values))
    def visit_Dict(self, node: Dict):
        keys = []

        for key in node.keys:
            value = self.visit_all(key, inline=True)
            if isinstance(key, ast.Str):
                value = "[{}]".format(value)
            keys.append(value)

        values = [self.visit_all(item, inline=True) for item in node.values]

        elements = ["{} = {}".format(keys[i], values[i]) for i in range(len(keys))]
        elements = ", ".join(elements)
        self.emit("dict {{{}}}".format(elements))
    def visit_Set(self, node: Set) :pass
    def visit_ListComp(self, node: ListComp):
        self.emit("(function()")
        self.emit("local result = list {}")

        ends_count = 0

        for comp in node.generators:
            line = "for {target} in {iterator} do"
            values = {
                "target": self.visit_all(comp.target, inline=True),
                "iterator": self.visit_all(comp.iter, inline=True),
            }
            line = line.format(**values)
            self.emit(line)
            ends_count += 1

            for if_ in comp.ifs:
                line = "if {} then".format(self.visit_all(if_, inline=True))
                self.emit(line)
                ends_count += 1

        line = "result.append({})"
        line = line.format(self.visit_all(node.elt, inline=True))
        self.emit(line)

        self.emit(" ".join(["end"] * ends_count))

        self.emit("return result")
        self.emit("end)()")
    def visit_SetComp(self, node: SetComp) :pass
    def visit_DictComp(self, node: DictComp):
        self.emit("(function()")
        self.emit("local result = dict {}")

        ends_count = 0

        for comp in node.generators:
            line = "for {target} in {iterator} do"
            values = {
                "target": self.visit_all(comp.target, inline=True),
                "iterator": self.visit_all(comp.iter, inline=True),
            }
            line = line.format(**values)
            self.emit(line)
            ends_count += 1

            for if_ in comp.ifs:
                line = "if {} then".format(self.visit_all(if_, inline=True))
                self.emit(line)
                ends_count += 1

        line = "result[{key}] = {value}"
        values = {
            "key": self.visit_all(node.key, inline=True),
            "value": self.visit_all(node.value, inline=True),
        }
        self.emit(line.format(**values))

        self.emit(" ".join(["end"] * ends_count))

        self.emit("return result")
        self.emit("end)()")
    def visit_GeneratorExp(self, node: GeneratorExp) :pass
    def visit_Await(self, node: Await):
        # https://github.com/iamcco/async-await.lua
        # https://github.com/ms-jpq/lua-async-await
        raise NotImplementedError("await")
    def visit_Yield(self, node: Yield):
        raise NotImplementedError("yield")
    def visit_YieldFrom(self, node: YieldFrom):
        raise NotImplementedError("yield from")
    def visit_Compare(self, node: Compare):
        line = ""

        left = self.visit_all(node.left, inline=True)
        for i in range(len(node.ops)):
            operation = node.ops[i]
            operation = CompareOperationDesc.OPERATION[operation.__class__]

            right = self.visit_all(node.comparators[i], inline=True)

            values = {
                "left": left,
                "right": right,
            }

            if isinstance(operation, str):
                values["op"] = operation
                line += "{left} {op} {right}".format(**values)
            elif isinstance(operation, dict):
                line += operation["format"].format(**values)

            if i < len(node.ops) - 1:
                left = right
                line += " and "

        self.emit("({})".format(line))
    def visit_Call(self, node: Call):
        line = "{name}({arguments})"

        name = self.visit_all(node.func, inline=True)
        arguments = [self.visit_all(arg, inline=True) for arg in node.args]

        self.emit(line.format(name=name, arguments=", ".join(arguments)))
    def visit_FormattedValue(self, node: FormattedValue):
        print("formatted value")
    def visit_JoinedStr(self, node: JoinedStr):
        print("joined str")
    def visit_Constant(self, node: Constant):
        t = type(node.value)

        if node.value == None:
            self.emit("nil")
            return
        if t == str:
            value = node.s
            if value.startswith(NodeVisitor.LUACODE):
                value = value[len(NodeVisitor.LUACODE):]
                self.emit(value)
            elif self.context.last()["docstring"]:
                self.emit(f'--[[ {node.s} ]]')
            else:
                self.emit(f'"{node.s}"')
            return

        if t == int or t == float:
            self.emit(str(node.value))
            return
        if t == complex:
            # https://github.com/davidm/lua-matrix/blob/master/lua/complex.lua
            # http://lua-users.org/wiki/ComplexNumbers
            # TODO implement complex numbers translation
            raise NotImplementedError("Complex number translation is not implemented")

        raise Exception(f"Unknown type {str(t)}")
        # self.emit(str(node.value))
    def visit_NamedExpr(self, node: NamedExpr) :pass
    def visit_Attribute(self, node: Attribute):
        obj = self.visit_all(node.value, True)
        if obj == self.config.core_prefix:
            line = "{attr}"
            self.emit(line.format(**{"attr": node.attr}))
            return

        line = "{object}.{attr}"
        values = {
            "object": obj,
            "attr": node.attr,
        }
        self.emit(line.format(**values))
    def visit_Subscript(self, node: Subscript):
        line = "{name}[{index}]"
        values = {
            "name": self.visit_all(node.value, inline=True),
            "index": self.visit_all(node.slice, inline=True),
        }

        self.emit(line.format(**values))
    def visit_Starred(self, node: Starred):
        value = self.visit_all(node.value, inline=True)
        line = "unpack({})".format(value)
        self.emit(line)
    def visit_Name(self, node: Name):
        self.emit(node.id)
    def visit_List(self, node: List):
        elements = [self.visit_all(item, inline=True) for item in node.elts]
        line = "list {{{}}}".format(", ".join(elements))
        self.emit(line)
    def visit_Tuple(self, node: Tuple):
        elements = [self.visit_all(item, inline=True) for item in node.elts]
        self.emit(", ".join(elements))
    def visit_MatMult(self, node: MatMult):
        raise Exception("Matrix multiplication operator @ is not implemented")
    def visit_ExceptHandler(self, node: ExceptHandler):
        raise NotImplementedError("Exception handler")