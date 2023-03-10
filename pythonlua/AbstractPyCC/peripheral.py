from .luatypes import *

class peripheral:
  @staticmethod
  def getNames()->table[string]:
    """
    Provides a list of all peripherals available.

    If a device is located directly next to the system, then its name will be listed as the side it is attached to. If a device is attached via a WiredModem, then it'll be reported according to its name on the wired network.

    :returns: A list of the names of all attached peripherals.
    """
    pass
  @staticmethod
  def isPresent(name:string)->boolean:
    """
    Determines if a peripheral is present with the given name.

    :param name: The side or network name that you want to check.
    :returns: If a peripheral is present with the given name.
    """
    pass
  @staticmethod
  def getType(peripheral:string | table)->string:
    """
    Get the types of a named or wrapped peripheral.

    :param peripheral: The name of the peripheral to find, or a wrapped peripheral instance.
    :returns: The peripheral's types, or nil if it is not present.
    """
    pass
  @staticmethod
  def hasType(peripheral:string | table, peripheral_type:string|table)->boolean | None:
    """
    Check if a peripheral is of a particular type.

    :param peripheral: The name of the peripheral or a wrapped peripheral instance.
    :param peripheral_type: The type to check.
    :returns: If a peripheral has a particular type, or nil if it is not present.
    """
    pass
  @staticmethod
  def getMethods(name:string)->table[string] | None:
    """
    Get all available methods for the peripheral with the given name.

    :param name: The name of the peripheral to find.
    :returns: A list of methods provided by this peripheral, or nil if it is not present.
    """
    pass
  @staticmethod
  def getName(peripheral:table)->string:
    """
    Get the name of a peripheral wrapped with peripheral.wrap.

    :param peripheral: The peripheral to get the name of.
    :returns: The name of the given peripheral.
    """
    pass
  @staticmethod
  def call(name:string, method:string, *args)->None:
    """
    Call a method on the peripheral with the given name.

    :param name: The name of the peripheral to invoke the method on.
    :param method: The name of the method
    """
    pass
  @staticmethod
  def wrap(name:string)->table | None:
    """
    Get a table containing all functions available on a peripheral. These can then be called instead of using peripheral.call every time.

    :param name: The name of the peripheral to wrap.
    :returns: The table containing the peripheral's methods, or nil if there is no peripheral present with the given name.
    """
    pass
  @staticmethod
  def find(ty:string, filter:string=None)->table:
    """
    Find all peripherals of a specific type, and return thewrapped peripherals.

    :param ty: The type of peripheral to look for.
    :param filter: A filter function, which takes the peripheral's name and wrapped table and returns if it should be included in the result.
    :returns: 0 or more wrapped peripherals matching the given filters.
    """
    pass