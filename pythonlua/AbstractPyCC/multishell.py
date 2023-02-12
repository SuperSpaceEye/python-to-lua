from luatypes import *

class multishell:
  @staticmethod
  def getFocus()->number:
    """
    Get the currently visible process. This will be the one selected onthe tab bar.

    Note, this is different to getCurrent, which returns the process which iscurrently executing.

    :returns: The currently visible process's index.
    """
    pass
  @staticmethod
  def setFocus(n:number)->boolean:
    """
    Change the currently visible process.

    :param n: The process index to switch to.
    :returns: If the process was changed successfully. This will return false if there is no process with this id.
    """
    pass
  @staticmethod
  def getTitle(n:number)->string | None:
    """
    Get the title of the given tab.

    This starts as the name of the program, but may be changed usingmultishell.setTitle.

    :param n: The process index.
    :returns: The current process title, or nil if the process doesn't exist.
    """
    pass
  @staticmethod
  def setTitle(n:number, title:string)->None:
    """
    Set the title of the given process.

    Change the title of the current process

    :param n: The process index.
    :param title: The new process title.
    """
    pass
  @staticmethod
  def getCurrent()->number:
    """
    Get the index of the currently running process.

    :returns: The currently running process.
    """
    pass
  @staticmethod
  def launch(tProgramEnv:table, sProgramPath:string, *args)->None:
    """
    Start a new process, with the given environment, program and arguments.

    The returned process index is not constant over the program's run. It can besafely used immediately after launching (for instance, to update the title orswitch to that tab). However, after your program has yielded, it may nolonger be correct.

    Run the "hello" program, and set its title to "Hello!"

    :param tProgramEnv: The environment to load the path under.
    :param sProgramPath: The path to the program to run.
    """
    pass
  @staticmethod
  def getCount()->number:
    """
    Get the number of processes within this multishell.

    :returns: The  of processes.
    """
    pass