from __future__ import annotations
from typing import List


class VarItem:
    name = ""
    type = ""

    def __init__(self, name:str, type:str):
        self.name = name
        self.type = type

    def __eq__(self, other:VarItem|str):
        if type(other) == VarItem:
            if self.name == other.name and self.type == other.type:
                return True
            return False
        elif type(other) == str:
            if self.name == other:
                return True
            return False


class VarContext:
    data = None

    def __init__(self, var_context:VarContext=None):
        self.data = var_context if var_context is not None else []

    def push(self):
        self.data.append([])

    def pop(self)->List[VarItem]:
        return self.data.pop()

    def back(self)->List[VarItem]:
        return self.data[-1]

    def add(self, add_item:VarItem):
        for level in reversed(self.data):
            for item in level:
                if add_item == item:
                    return
        self.back().append(add_item)

    def exists(self, search_item: VarItem | str):
        for level in reversed(self.data):
            for item in level:
                if search_item == item:
                    return True
        return False
