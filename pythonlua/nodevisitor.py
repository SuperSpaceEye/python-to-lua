"""Node visitor"""
import ast
import copy
import builtins

from .binopdesc import BinaryOperationDesc
from .boolopdesc import BooleanOperationDesc
from .cmpopdesc import CompareOperationDesc
from .nameconstdesc import NameConstantDesc
from .unaryopdesc import UnaryOperationDesc

from .context import Context
from .loopcounter import LoopCounter
from .tokenendmode import TokenEndMode
from .prenodevisitor import PreNodeVisitor


class NodeVisitor(ast.NodeVisitor):
    LUACODE = "[[luacode]]"

    """Node visitor"""
    def __init__(self,
                 context=None,
                 config=None,
                 continue_nodes=None,
                 precompiled_parts=None,
                 names=None):
        self.context = context if context is not None else Context()
        self.config = config
        self.last_end_mode = TokenEndMode.LINE_FEED
        self.output = []

        self.core_prefix = config.core_prefix
        self.core_pathname = config.core_pathname
        self.no_jumps = config.no_jumps

        if continue_nodes is not None:
            self.continue_nodes = [item[0] for item in continue_nodes]
        else:
            self.continue_nodes = []
        self.precompiled_parts = precompiled_parts if precompiled_parts is not None else []
        self.names = names if names is not None else []
        self.fn_calls = [item[1] for item in continue_nodes] if continue_nodes is not None else []

    def visit_Assign(self, node):
        """Visit assign"""
        target = self.visit_all(node.targets[0], inline=True)
        value = self.visit_all(node.value, inline=True)

        local_keyword = ""

        last_ctx = self.context.last()

        if last_ctx["class_name"]:
            target = ".".join([last_ctx["class_name"], target])

        if "." not in target and not last_ctx["locals"].exists(target):
            local_keyword = "local "
            last_ctx["locals"].add_symbol(target)


        self.emit("{local}{target} = {value}".format(local=local_keyword,
                                                     target=target,
                                                     value=value))

    def visit_AugAssign(self, node):
        """Visit augassign"""
        operation = BinaryOperationDesc.OPERATION[node.op.__class__]

        target = self.visit_all(node.target, inline=True)

        values = {
            "left": target,
            "right": self.visit_all(node.value, inline=True),
            "operation": operation["value"],
        }

        line = "({})".format(operation["format"])
        line = line.format(**values)

        self.emit("{target} = {line}".format(target=target, line=line))

    def visit_Attribute(self, node):
        """Visit attribute"""

        obj = self.visit_all(node.value, True)
        if obj == self.core_prefix:
            line = "{attr}"
            self.emit(line.format(**{"attr":node.attr}))
            return

        line = "{object}.{attr}"
        values = {
            "object": obj,
            "attr": node.attr,
        }
        self.emit(line.format(**values))

    def visit_BinOp(self, node):
        """Visit binary operation"""
        operation = BinaryOperationDesc.OPERATION[node.op.__class__]
        line = "({})".format(operation["format"])
        values = {
            "left": self.visit_all(node.left, True),
            "right": self.visit_all(node.right, True),
            "operation": operation["value"],
        }

        self.emit(line.format(**values))

    def visit_BoolOp(self, node):
        """Visit boolean operation"""
        operation = BooleanOperationDesc.OPERATION[node.op.__class__]
        line = "({})".format(operation["format"])
        values = {
            "left": self.visit_all(node.values[0], True),
            "right": self.visit_all(node.values[1], True),
            "operation": operation["value"],
        }

        self.emit(line.format(**values))

    def visit_Break(self, node):
        """Visit break"""
        self.emit("break")

    def visit_Call(self, node):
        """Visit function call"""
        line = "{name}({arguments})"

        name = self.visit_all(node.func, inline=True)
        arguments = [self.visit_all(arg, inline=True) for arg in node.args]

        self.emit(line.format(name=name, arguments=", ".join(arguments)))

    def visit_ClassDef(self, node):
        """Visit class definition"""
        bases = [self.visit_all(base, inline=True) for base in node.bases]

        local_keyword = ""
        last_ctx = self.context.last()
        if not last_ctx["class_name"] and not last_ctx["locals"].exists(node.name):
            local_keyword = "local "
            last_ctx["locals"].add_symbol(node.name)

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

        self.output[-1].append("return {node_name}".format(**values))

        self.emit("end, {{{}}})".format(", ".join(bases)))

        # Return class object only in the top-level classes.
        # Not in the nested classes.
        if self.config["class"]["return_at_the_end"] and not last_ctx["class_name"]:
            self.emit("return {}".format(name))

    def visit_Compare(self, node):
        """Visit compare"""

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

    def visit_Continue(self, node):
        """Visit continue"""
        last_ctx = self.context.last()

        if self.no_jumps:
            # raise RuntimeError("Continue can't be used")
            self.emit("return")
            return

        line = "goto {}".format(last_ctx["loop_label_name"])
        self.emit(line)

    def visit_Delete(self, node):
        """Visit delete"""
        targets = [self.visit_all(target, inline=True) for target in node.targets]
        nils = ["nil" for _ in targets]
        line = "{targets} = {nils}".format(targets=", ".join(targets),
                                           nils=", ".join(nils))
        self.emit(line)

    def visit_Dict(self, node):
        """Visit dictionary"""
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

    def visit_DictComp(self, node):
        """Visit dictionary comprehension"""
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

    def visit_Ellipsis(self, node):
        """Visit ellipsis"""
        self.emit("...")

    def visit_Expr(self, node):
        """Visit expr"""
        expr_is_docstring = False
        if isinstance(node.value, ast.Str):
            expr_is_docstring = True

        self.context.push({"docstring": expr_is_docstring})
        output = self.visit_all(node.value)
        self.context.pop()

        self.output.append(output)

    def visit_FunctionDef(self, node):
        """Visit function definition"""
        line = "{local}function {name}({arguments})"

        last_ctx = self.context.last()

        name = node.name
        if last_ctx["class_name"]:
            name = ".".join([last_ctx["class_name"], name])

        arguments = [arg.arg for arg in node.args.args]

        if node.args.vararg is not None:
            arguments.append("...")

        local_keyword = ""

        if "." not in name and not last_ctx["locals"].exists(name):
            local_keyword = "local "
            last_ctx["locals"].add_symbol(name)

        function_def = line.format(local=local_keyword,
                                   name=name,
                                   arguments=", ".join(arguments))

        self.emit(function_def)

        # print(self.fn_calls)
        for i, item in enumerate(self.fn_calls):
            if item == node:
                pass
                self.output += self.precompiled_parts[0][1]
                # for item in self.precompiled_parts[0]:
                #     print(item, "===")
                # print(self.precompiled_parts)

        self.context.push({"class_name": ""})

        temp = copy.deepcopy(self.names)
        self.visit_all(node.body)
        self.names = temp

        self.context.pop()

        body = self.output[-1]

        if node.args.vararg is not None:
            line = "local {name} = list {{...}}".format(name=node.args.vararg.arg)
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
            values = {
                "name": name,
                "decorator": decorator_name,
            }
            line = "{name} = {decorator}({name})".format(**values)
            self.emit(line)

    def visit_For(self, node):
        """Visit for loop"""
        line = "for {target} in {iter} do"

        values = {
            "target": self.visit_all(node.target, inline=True),
            "iter": self.visit_all(node.iter, inline=True),
        }

        self.emit(line.format(**values))

        continue_label = LoopCounter.get_next()
        self.context.push({
            "loop_label_name": continue_label,
        })

        if self.no_jumps and node in self.continue_nodes:
            idx = self.continue_nodes.index(node)

            self.names = list(tuple(self.names))
            self.names = list(tuple(v for v in set(self.names) if v not in vars(builtins) and v not in self.config.core_prefix))
            fn_data = copy.deepcopy(self.precompiled_parts[idx][0][2]) + "("
            for i, item in enumerate(self.precompiled_parts[idx][0][1]):
                if item in self.names:
                    fn_data += item
                else:
                    fn_data += "0"
                if i != len(self.precompiled_parts[idx][0][1])-1:
                    fn_data+=","
            fn_data += ")"

            self.emit([fn_data])
        else:
            self.visit_all(node.body)

        self.context.pop()

        if not self.no_jumps:
            self.output[-1].append("::{}::".format(continue_label))

        self.emit("end")

    def visit_Global(self, node):
        """Visit globals"""
        last_ctx = self.context.last()
        for name in node.names:
            last_ctx["globals"].add_symbol(name)

    def visit_If(self, node):
        """Visit if"""
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

    def visit_IfExp(self, node):
        """Visit if expression"""
        line = "{cond} and {true_cond} or {false_cond}"
        values = {
            "cond": self.visit_all(node.test, inline=True),
            "true_cond": self.visit_all(node.body, inline=True),
            "false_cond": self.visit_all(node.orelse, inline=True),
        }

        self.emit(line.format(**values))

    def visit_Import(self, node):
        """Visit import"""
        line = 'local {asname} = require "{name}"'
        values = {"asname": "", "name": ""}

        if node.names[0].name == self.core_pathname:
            return

        if node.names[0].asname is None:
            values["name"] = node.names[0].name
            values["asname"] = values["name"]
            values["asname"] = values["asname"].split(".")[-1]
        else:
            values["asname"] = node.names[0].asname
            values["name"] = node.names[0].name

        self.emit(line.format(**values))

    def visit_Index(self, node):
        """Visit index"""
        self.emit(self.visit_all(node.value, inline=True))

    def visit_Lambda(self, node):
        """Visit lambda"""
        line = "function({arguments}) return"

        arguments = [arg.arg for arg in node.args.args]

        function_def = line.format(arguments=", ".join(arguments))

        output = []
        output.append(function_def)
        output.append(self.visit_all(node.body, inline=True))
        output.append("end")

        self.emit(" ".join(output))

    def visit_List(self, node):
        """Visit list"""
        elements = [self.visit_all(item, inline=True) for item in node.elts]
        line = "list {{{}}}".format(", ".join(elements))
        self.emit(line)

    def visit_ListComp(self, node):
        """Visit list comprehension"""
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

    def visit_Module(self, node):
        """Visit module"""
        self.visit_all(node.body)
        self.output = self.output[0]

    def visit_Name(self, node):
        """Visit name"""
        self.emit(node.id)
        self.names.append(node.id)

    def visit_NameConstant(self, node):
        """Visit name constant"""
        self.emit(NameConstantDesc.NAME[node.value])

    def visit_Num(self, node):
        """Visit number"""
        self.emit(str(node.n))

    def visit_Pass(self, node):
        """Visit pass"""
        pass

    def visit_Return(self, node):
        """Visit return"""
        line = "return "
        line += self.visit_all(node.value, inline=True)
        self.emit(line)

    def visit_Starred(self, node):
        """Visit starred object"""
        value = self.visit_all(node.value, inline=True)
        line = "unpack({})".format(value)
        self.emit(line)

    def visit_Str(self, node):
        """Visit str"""
        value = node.s
        if value.startswith(NodeVisitor.LUACODE):
            value = value[len(NodeVisitor.LUACODE):]
            self.emit(value)
        elif self.context.last()["docstring"]:
            self.emit('--[[ {} ]]'.format(node.s))
        else:
            self.emit('"{}"'.format(node.s))

    def visit_Subscript(self, node):
        """Visit subscript"""
        line = "{name}[{index}]"
        values = {
            "name": self.visit_all(node.value, inline=True),
            "index": self.visit_all(node.slice, inline=True),
        }

        self.emit(line.format(**values))

    def visit_Tuple(self, node):
        """Visit tuple"""
        elements = [self.visit_all(item, inline=True) for item in node.elts]
        self.emit(", ".join(elements))

    def visit_UnaryOp(self, node):
        """Visit unary operator"""
        operation = UnaryOperationDesc.OPERATION[node.op.__class__]
        value = self.visit_all(node.operand, inline=True)

        line = operation["format"]
        values = {
            "value": value,
            "operation": operation["value"],
        }

        self.emit(line.format(**values))

    def visit_While(self, node):
        """Visit while"""
        test = self.visit_all(node.test, inline=True)

        self.emit("while {} do".format(test))

        continue_label = LoopCounter.get_next()
        self.context.push({
            "loop_label_name": continue_label,
        })
        self.visit_all(node.body)
        self.context.pop()

        if not self.no_jumps:
            self.output[-1].append("::{}::".format(continue_label))

        self.emit("end")

    def visit_With(self, node):
        """Visit with"""
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

    def generic_visit(self, node):
        """Unknown nodes handler"""
        raise RuntimeError("Unknown node: {}".format(node))

    def visit_all(self, nodes, inline=False, nopop=False):
        """Visit all nodes in the given list"""

        if not inline:
            last_ctx = self.context.last()
            last_ctx["locals"].push()

        visitor = NodeVisitor(context=self.context,
                              config=self.config,
                              continue_nodes=[[it1, it2] for it1, it2 in zip(self.continue_nodes, self.fn_calls)],
                              precompiled_parts=self.precompiled_parts,
                              names=self.names)

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
            last_ctx = self.context.last()
            if not nopop: last_ctx["locals"].pop()

        if inline:
            return " ".join(visitor.output)

    def emit(self, value):
        """Add translated value to the output"""
        self.output.append(value)
