"""Unary operation description"""
import ast


_DEFAULT_FORMAT = "{operation}{value}"


class UnaryOperationDesc:
    """Unary operation description"""

    OPERATION = {
        ast.USub: {
            "value": "-",
            "format": "{value}.__neg__()",
        },
        ast.UAdd: {
            "value": "+",
            "format": "{value}.__pos__()",
        },
        ast.Not: {
            "value": "not",
            "format": "not {value}",
        },
        ast.Invert: {
            "value": "~",
            "format": "bit32.bnot({value})",
        },
    }
