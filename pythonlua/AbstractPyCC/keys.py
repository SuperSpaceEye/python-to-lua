from luatypes import *

class keys:
  @staticmethod
  def getName(code:number)->string | None:
    """
    Translates a numerical key code to a human-readable name. The human-readablename is one of the constants in the keys API.

    :param code: The key code to look up.
    :returns: The name of the key, or nil if not a valid key code.
    """
    pass