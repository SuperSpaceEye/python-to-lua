from .luatypes import *

class redstone:
  @staticmethod
  def getSides()->table[string]:
    """
    Returns a table containing the six sides of the computer. Namely, "top", "bottom", "left", "right", "front" and"back".

    :returns: A table of valid sides.
    """
    pass
  @staticmethod
  def setOutput(side:string, on:boolean)->None:
    """
    Turn the redstone signal of a specific side on or off.

    :param side: The side to set.
    :param on: Whether the redstone signal should be on or off. When on, a signal strength of 15 is emitted.
    """
    pass
  @staticmethod
  def getOutput(side:string)->boolean:
    """
    Get the current redstone output of a specific side.

    :param side: The side to get.
    :returns: Whether the redstone output is on or off.
    """
    pass
  @staticmethod
  def getInput(side:string)->boolean:
    """
    Get the current redstone input of a specific side.

    :param side: The side to get.
    :returns: Whether the redstone input is on or off.
    """
    pass
  @staticmethod
  def setAnalogOutput(side:string, value:number)->None:
    """
    Set the redstone signal strength for a specific side.

    If value is not between 0 and 15.

    :param side: The side to set.
    :param value: The signal strength between 0 and 15.
    """
    pass
  @staticmethod
  def setAnalogueOutput(side:string, value:number)->None:
    """
    Set the redstone signal strength for a specific side.

    If value is not between 0 and 15.

    :param side: The side to set.
    :param value: The signal strength between 0 and 15.
    """
    pass
  @staticmethod
  def getAnalogOutput(side:string)->number:
    """
    Get the redstone output signal strength for a specific side.

    :param side: The side to get.
    :returns: The output signal strength, between 0 and 15.
    """
    pass
  @staticmethod
  def getAnalogueOutput(side:string)->number:
    """
    Get the redstone output signal strength for a specific side.

    :param side: The side to get.
    :returns: The output signal strength, between 0 and 15.
    """
    pass
  @staticmethod
  def getAnalogInput(side:string)->number:
    """
    Get the redstone input signal strength for a specific side.

    :param side: The side to get.
    :returns: The input signal strength, between 0 and 15.
    """
    pass
  @staticmethod
  def getAnalogueInput(side:string)->number:
    """
    Get the redstone input signal strength for a specific side.

    :param side: The side to get.
    :returns: The input signal strength, between 0 and 15.
    """
    pass
  @staticmethod
  def setBundledOutput(side:string, output:number)->None:
    """
    Set the bundled cable output for a specific side.

    :param side: The side to set.
    :param output: The colour bitmask to set.
    """
    pass
  @staticmethod
  def getBundledOutput(side:string)->number:
    """
    Get the bundled cable output for a specific side.

    :param side: The side to get.
    :returns: The bundle cable's output.
    """
    pass
  @staticmethod
  def getBundledInput(side:string)->number:
    """
    Get the bundled cable input for a specific side.

    :param side: The side to get.
    :returns: The bundle cable's input.
    """
    pass
  @staticmethod
  def testBundledInput(side:string, mask:number)->boolean:
    """
    Determine if a specific combination of colours are on for the given side.

    Check if colors.white and colors.black are on above the computer.

    :param side: The side to test.
    :param mask: The mask to test.
    :returns: If the colours are on.
    """
    pass