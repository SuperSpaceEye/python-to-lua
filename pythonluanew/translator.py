"""Python to lua translator class"""
import ast
import os
import builtins

from .config import Config
# from .prenodevisitor import PreNodeVisitor

import sys
sys.path.append("")
sys.path.append("../pythonluanew")
from .nodevisitor import CNodeVisitor as ND

class Translator:
    """Python to lua main class translator"""
    def __init__(self, config=None):
        self.config = config if config is not None else Config()

        self.output = []

    def translate(self, pycode):
        """Translate python code to lua code"""
        # in code \n (not newline char) is represented as \ and n.
        # after parsing several times it will be represented as newline instead (not two characters)
        # to prevent that, i just add 2 \ instead of \, so in code it will be \\ and \\ or \\\\
        # so that the end result will become 2 characters of \ and n
        pycode = pycode.replace("\\n", "\\\\n")

        py_ast_tree = ast.parse(pycode)

        # precompiled_parts = []
        # continue_nodes = None
        # # because CC:T lua has no goto jumps (as of right now), the continue can be emulated
        # # by refactoring body of a loop into a function with early return (early return itself can't be together with continue loop)
        # # to do that,
        # i = 0
        # if self.config.no_jumps:
        #     pre_visitor = PreNodeVisitor(config=self.config)
        #     pre_visitor.visit(py_ast_tree)
        #     # 0 - node of loop, 1 - node of fn definition
        #     continue_nodes = list(reversed(pre_visitor.continue_nodes))
        #
        #     for node in [item[0] for item in continue_nodes]:
        #         visitor = NodeVisitor(config=self.config,
        #                               continue_nodes=continue_nodes,
        #                               precompiled_parts=precompiled_parts
        #                               )
        #
        #         pre_visitor = PreNodeVisitor(context=None,
        #                                      config=self.config)
        #         pre_visitor.visit(node)
        #
        #         # names = list(tuple(v for v in set(pre_visitor.names) if v not in vars(builtins) and v not in self.config.core_prefix))
        #         var_list = list(pre_visitor.var_names)
        #         names_str = ""
        #         for name in pre_visitor.var_names:
        #             if name != var_list[len(var_list)-1]:
        #                 names_str += name + ", "
        #             else:
        #                 names_str += name
        #
        #
        #         function_name = f"continue_fn{len(precompiled_parts)}({names_str})"
        #
        #         visitor.emit(f"function {function_name}")
        #         visitor.visit_all(node.body, nopop=True)
        #         visitor.emit("end")
        #         precompiled_parts.append([[function_name, var_list, f"continue_fn{len(precompiled_parts)}"], visitor.output])
        #
        visitor = ND(config=self.config)
                              # continue_nodes=continue_nodes,
                              # precompiled_parts=precompiled_parts)
        # self.output = []

        # visitor = NodeVisitor()

        visitor.visit(py_ast_tree)

        self.output += visitor.output

        return self.to_code()

    def to_code(self, code=None, indent=0):
        """Create a lua code from the compiler output"""
        code = code if code is not None else self.output

        def add_indentation(line):
            """Add indentation to the given line"""
            indentation_width = 4
            indentation_space = " "

            indent_copy = max(indent, 0)

            return indentation_space * indentation_width * indent_copy + line

        lines = []
        for line in code:
            if isinstance(line, str):
                lines.append(add_indentation(line))
            elif isinstance(line, list):
                sub_code = self.to_code(line, indent + 1)
                lines.append(sub_code)

        return "\n".join(lines)

    @staticmethod
    def get_luainit(filename="luainit.lua"):
        """Get lua initialization code."""
        script_name = os.path.realpath(__file__)
        folder = os.path.dirname(script_name)
        luainit_path = os.path.join(folder, filename)

        with open(luainit_path) as file:
            return file.read()
        return ""
