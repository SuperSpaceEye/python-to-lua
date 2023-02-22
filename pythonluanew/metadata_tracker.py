from dataclasses import dataclass
from typing import List, TypedDict, Type, Dict, NamedTuple

class ReturnSignature(NamedTuple):
    num_returned:int
    # returned_types:List[Type]
@dataclass
class MetaFunction:
    id:str
    parent:str
    # For multiple returns with different return signature
    returns:List[ReturnSignature]

# Will collect data from all compiled objects
class GlobalMetadataTracker:
    data:Dict[str, MetaFunction] = {}
    def __init__(self):
        pass
    def get_id(self, name:str):
        return self.data[name]
    def set_id(self, name:str, item:MetaFunction):
        self.data[name] = item

# Will hold conversion of current id's to global names
class CurrentIdTracker:
    data = {}