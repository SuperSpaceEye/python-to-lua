from .luatypes import *
def sleep(time:number):
    """
    Pauses execution for the specified number of seconds.

    :param time: number
    """
    pass
def write(text:string)->number:
    """
    Writes a line of text to the screen without a newline at the end, wrapping text if necessary.
    :param text: string The text to write to the string
    :return: The number of lines written
    """

    pass
def print(*args):
    """
    Prints the specified values to the screen separated by spaces, wrapping if necessary.
    :param args:
    :return: The number of lines written
    """
    pass
def printError(*args):
    """
    Prints the specified values to the screen in red, separated by spaces, wrapping if necessary.
    :param args: The values to print on the screen.
    """
    pass

def read(replaceChar:string=None,
         history:table=None,
         completeFn: Callable[[string], string]=None,
         default:string=None)->string:
    """
    Reads user input from the terminal. This automatically handles arrow keys, pasting, character replacement, history scrollback, auto-completion, and default values.
    :param replaceChar: A character to replace each typed character with. This can be used for hiding passwords, for example.
    :param history: A table holding history items that can be scrolled back to with the up/down arrow keys. The oldest item is at index 1, while the newest item is at the highest index.
    :param completeFn: function to be used for completion. This function should take the partial text typed so far, and returns a list of possible completion options.
    :param default: Default text which should already be entered into the prompt.
    :return: The text typed in.
    """
    pass
