import ast

from .context import Context

class PreNodeVisitor(ast.NodeVisitor):
    LUACODE = "[[luacode]]"

    """Node visitor"""
    def __init__(self,
                 context=None,
                 config=None,
                 has_continue=None,
                 continue_nodes=None,
                 names=None,
                 has_return=None,
                 parent_nodes=None):
        self.context = context if context is not None else Context()
        self.config = config

        self.has_continue = has_continue if has_continue is not None else [False]
        self.continue_nodes = continue_nodes if continue_nodes is not None else []
        self.names = names if names is not None else []
        self.has_return = has_return if has_return is not None else [False]
        self.parent_nodes = parent_nodes if parent_nodes is not None else []

    def visit_Assign(self, node):
        self.visit_all(node.targets[0], inline=True)
        self.visit_all(node.value, inline=True)

    def visit_AugAssign(self, node):
        self.visit_all(node.target, inline=True)
        self.visit_all(node.value, inline=True),

    def visit_Attribute(self, node):
        obj = self.visit_all(node.value, True)
    def visit_BinOp(self, node):
        self.visit_all(node.left, True),
        self.visit_all(node.right, True),

    def visit_BoolOp(self, node):
        self.visit_all(node.values[0], True),
        self.visit_all(node.values[1], True),

    def visit_Break(self, node):
        pass

    def visit_Call(self, node):
        name = self.visit_all(node.func, inline=True)
        arguments = [self.visit_all(arg, inline=True) for arg in node.args]

    def visit_ClassDef(self, node):
        bases = [self.visit_all(base, inline=True) for base in node.bases]
        self.visit_all(node.body)

    def visit_Compare(self, node):
        left = self.visit_all(node.left, inline=True)
        for i in range(len(node.ops)):
            right = self.visit_all(node.comparators[i], inline=True)

    def visit_Continue(self, node):
        self.has_continue[0] = True

    def visit_Delete(self, node):
        targets = [self.visit_all(target, inline=True) for target in node.targets]

    def visit_Dict(self, node):
        for key in node.keys:
            value = self.visit_all(key, inline=True)

        values = [self.visit_all(item, inline=True) for item in node.values]

    def visit_DictComp(self, node):
        for comp in node.generators:
            self.visit_all(comp.target, inline=True)
            self.visit_all(comp.iter, inline=True)


            for if_ in comp.ifs:
                line = "if {} then".format(self.visit_all(if_, inline=True))

        self.visit_all(node.key, inline=True)
        self.visit_all(node.value, inline=True)


    def visit_Ellipsis(self, node):
        pass

    def visit_Expr(self, node):
        output = self.visit_all(node.value)

    def visit_FunctionDef(self, node):
        self.parent_nodes.append(node)
        self.visit_all(node.body)
        for i in reversed(node.args.defaults):
            self.visit_all(i, inline=True)

        for decorator in reversed(node.decorator_list):
            self.visit_all(decorator, inline=True)
    def visit_For(self, node):
        self.visit_all(node.target, inline=True)
        self.visit_all(node.iter, inline=True)
        self.visit_all(node.body)
        if self.has_continue[0]:
            if self.has_return[0]: raise Exception("Continue and early return can't be together in one loop")
            self.has_continue[0] = False
            if len(self.parent_nodes) != 0:
                self.continue_nodes.append([node, self.parent_nodes.pop()])
            else:
                self.continue_nodes.append(node)

    def visit_Global(self, node):
        pass

    def visit_If(self, node):
        test = self.visit_all(node.test, inline=True)
        self.visit_all(node.body)

        if node.orelse:
            if isinstance(node.orelse[0], ast.If):
                elseif = node.orelse[0]
                elseif_test = self.visit_all(elseif.test, inline=True)
                self.visit_If(node.orelse[0])
            else:
                self.visit_all(node.orelse)
    def visit_IfExp(self, node):
        self.visit_all(node.test, inline=True)
        self.visit_all(node.body, inline=True)
        self.visit_all(node.orelse, inline=True)

    def visit_Import(self, node):
        pass

    def visit_Index(self, node):
        self.visit_all(node.value, inline=True)

    def visit_Lambda(self, node):
        self.visit_all(node.body, inline=True)

    def visit_List(self, node):
        elements = [self.visit_all(item, inline=True) for item in node.elts]

    def visit_ListComp(self, node):
        for comp in node.generators:
            self.visit_all(comp.target, inline=True)
            self.visit_all(comp.iter, inline=True)
            for if_ in comp.ifs:
                self.visit_all(if_, inline=True)

        self.visit_all(node.elt, inline=True)

    def visit_Module(self, node):
        self.visit_all(node.body)

    def visit_Name(self, node):
        self.names.append(node.id)
        pass

    def visit_NameConstant(self, node):
        pass

    def visit_Num(self, node):
        pass

    def visit_Pass(self, node):
        """Visit pass"""
        pass

    def visit_Return(self, node):
        self.visit_all(node.value, inline=True)
        self.has_return[0] = True

    def visit_Starred(self, node):
        self.visit_all(node.value, inline=True)

    def visit_Str(self, node):
        pass

    def visit_Subscript(self, node):
        self.visit_all(node.value, inline=True)
        self.visit_all(node.slice, inline=True)

    def visit_Tuple(self, node):
        elements = [self.visit_all(item, inline=True) for item in node.elts]

    def visit_UnaryOp(self, node):
        value = self.visit_all(node.operand, inline=True)

    def visit_While(self, node):
        """Visit while"""
        test = self.visit_all(node.test, inline=True)
        self.visit_all(node.body)

    def visit_With(self, node):
        self.visit_all(node.body)

        for i in node.items:
            line = ""
            if i.optional_vars is not None:
                self.visit_all(i.optional_vars, inline=True)
            self.visit_all(i.context_expr, inline=True)

    def generic_visit(self, node):
        """Unknown nodes handler"""
        raise RuntimeError("Unknown node: {}".format(node))

    def visit_all(self, nodes, inline=False):
        """Visit all nodes in the given list"""

        if not inline:
            last_ctx = self.context.last()
            last_ctx["locals"].push()

        visitor = PreNodeVisitor(context=self.context,
                                 config=self.config,
                                 has_continue=self.has_continue,
                                 continue_nodes=self.continue_nodes,
                                 names=self.names,
                                 has_return=self.has_return,
                                 parent_nodes=self.parent_nodes)

        if isinstance(nodes, list):
            for node in nodes:
                visitor.visit(node)
        else:
            visitor.visit(nodes)

    def emit(self, value):
        pass
