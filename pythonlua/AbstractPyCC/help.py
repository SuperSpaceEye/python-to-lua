from luatypes import *

class help:
  @staticmethod
  def path()->string:
    """
    Returns a colon-separated list of directories where help files are searchedfor. All directories are absolute.
    :returns: The current help search path, separated by colons.
    """
    pass
  @staticmethod
  def setPath(newPath:string)->None:
    """
    Sets the colon-separated list of directories where help files are searchedfor to newPath
    :param newPath: The new path to use.
    """
    pass
  @staticmethod
  def lookup(topic:string)->string | None:
    """
    Returns the location of the help file for the given topic.
    :param topic: The topic to find
    :returns: The path to the given topic's help file, or nil if it cannot be found.
    """
    pass
  @staticmethod
  def topics()->table:
    """
    Returns a list of topics that can be looked up and/or displayed.
    :returns: A list of topics in alphabetical order.
    """
    pass
  @staticmethod
  def completeTopic(prefix:string)->table:
    """
    Returns a list of topic endings that match the prefix. Can be used withread to allow input of a help topic.
    :param prefix: The prefix to match
    :returns: A list of matching topics.
    """
    pass