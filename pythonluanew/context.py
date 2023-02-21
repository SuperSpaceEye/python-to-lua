from __future__ import annotations

from .varcontext import *

class Context:
    def __init__(self, context:Context=None):
        if context is None:
            values = {
                "class_name": "",
                "loop_label_name": "",
                "docstring": False,
                "structural_tuple":True,
            }

            self.ctx_stack = [values]
            self.var_ctx = VarContext()
        else:
            self.ctx_stack = context.ctx_stack
            self.var_ctx = context.var_ctx

    def get_var_ctx(self):
        return self.var_ctx

    def last(self):
        """Return actual context state"""
        return self.ctx_stack[-1]

    def push(self, values):
        """Push new context state with new values"""
        value = self.ctx_stack[-1].copy()
        value.update(values)
        self.ctx_stack.append(value)

    def pop(self):
        """Pop last context state"""
        assert len(self.ctx_stack) > 1, "Pop context failed. This is a last context in the stack."
        return self.ctx_stack.pop()