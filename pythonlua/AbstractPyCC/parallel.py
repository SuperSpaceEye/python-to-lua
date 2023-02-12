from luatypes import *

class parallel:
  @staticmethod
  def waitForAny(*args)->None:
    """
    Switches between execution of the functions, until any of themfinishes. If any of the functions errors, the message is propagated upwardsfrom the parallel.waitForAny call.

    Print a message every second until the q key is pressed.

    :param args: The functions this task will run
    """
    pass
  @staticmethod
  def waitForAll(*args)->None:
    """
    Switches between execution of the functions, until all of them arefinished. If any of the functions errors, the message is propagated upwardsfrom the parallel.waitForAll call.

    Start off two timers and wait for them both to run.

    :param args: The functions this task will run
    """
    pass