from .luatypes import *

class Handle: pass
class Handle:
  def close(self)->boolean|List[boolean, string]:
    """
    Close this file handle, freeing any resources it uses.
    If this handle was already closed.
    :returns: If this handle was successfully closed.
    """
    pass
  def flush(self)->None:
    """
    Flush any buffered output, forcing it to be written to the file

    Throws:

    * If the handle has been closed
    """
    pass
  def lines(self, *args)->None:
    """
    Returns an iterator that, each time it is called, returns a newline from the file.

    This can be used in a for loop to iterate over all lines of a file

    Once the end of the file has been reached, nil will be returned. The file isnot automatically closed.

    Returns:
      * function()->string | None The line iterator

    Throws:

    * If the file cannot be opened for reading
    """
    pass
  def read(self, *args)->None:
    """
    Reads data from the file, using the specified formats. For eachformat provided, the function returns either the data read, or nil ifno data could be read.

    The following formats are available:

    * l: Returns the next line (without a newline on the end).
    * L: Returns the next line (with a newline on the end).
    * a: Returns the entire rest of the file.
    * ~~n: Returns a number~~ (not implemented in CC).


    These formats can be preceded by a * to make it compatible with Lua 5.1.

    If no format is provided, l is assumed.

    Parameters:
      * The formats to use

    Returns:
      string | None The data read from file
    """
    pass
  def seek(self, whence:string=None , offset:number=None)->number:
    """
    Seeks the file cursor to the specified position, and returns thenew position.

    whence controls where the seek operation starts, and is a string thatmay be one of these three values:

    The default value of whence is cur, and the default value of offsetis 0. This means that file:seek() without arguments returns the currentposition without moving.

    :param whence?: The place to set the cursor from.
    :param offset?: The offset from the start to move to.
    :returns: The new location of the file cursor.
    """
    pass

  def write(self, *args)->Handle:
    """
    Write one or more values to the file

    Parameters:
      string|number The values to write.
    :returns: The current file, allowing chained calls. Or None and string
    """
    pass


class io:
  @staticmethod
  def stdin()->None:
    """
    A file handle representing the "standard input". Reading from this file will prompt the user for input.
    """
    pass
  @staticmethod
  def stdout()->None:
    """
    A file handle representing the "standard output". Writing to this file will display the written text to the screen.
    """
    pass
  @staticmethod
  def stderr()->None:
    """
    A file handle representing the "standard error" stream.
    One may use this to display error messages, writing to it will display them on the terminal.
    """
    pass
  @staticmethod
  def close(file:Handle=None)->None:
    """
    Closes the provided file 
    :param file?: The file handle to close, defaults to the
current output file.
    """
    pass
  @staticmethod
  def flush()->None:
    """
    Flushes the current output file.
    """
    pass
  @staticmethod
  def input(file:Handle|string=None)->Handle:
    """
    Get or set the current input file.
    If the provided filename cannot be opened for reading.
    :param file: The new input file, either as a file path or pre-existing
    :returns: The current input file.
    """
    pass
  @staticmethod
  def lines(filename:string, *args)->None:
    """
    Opens the given file name in read mode and returns an iterator that,each time it is called, returns a new line from the file.

    This can be used in a for loop to iterate over all lines of a file

    Once the end of the file has been reached, nil will be returned. The file isautomatically closed.

    If no file name is given, the current input will be used instead.In this case, the handle is not used.

    Throws:

    * If the file cannot be opened for reading

    :param filename: The name of the file to extract lines from
    :param args: The argument to pass to Handle:read for each line.
    """
    pass
  @staticmethod
  def open(filename:string, mode:string=None)->Handle:
    """
    Open a file with the given mode, either returning a new file handleor nil, plus an error message.

    The mode string can be any of the following:

    * "r": Read mode
    * "w": Write mode
    * "a": Append mode


    The mode may also have a b at the end, which opens the file in "binarymode". This allows you to read binary files, as well as seek within a file.

    :param filename: The name of the file to open.
    :param mode: The mode to open the file with. This defaults to rb.
    :returns: The opened file.
    """
    pass
  @staticmethod
  def output(file:Handle|string=None)->Handle:
    """
    Get or set the current output file.

    Throws:

    * If the provided filename cannot be opened for writing.
    :param file: The new output file, either as a file path or pre-existing
    :returns: The current output file.
    """
    pass
  @staticmethod
  def read(*args)->string | None:
    """
    Read from the currently opened input file.

    This is equivalent to io.input():read(...). See the documentation there for full details.
    :param ...: The formats to read, defaulting to a whole line.
    :returns: The data read, or nil if nothing can be read.
    """
    pass
  @staticmethod
  def type(obj)->string|None:
    """
    Checks whether handle is a given file handle, and determine if it is openor not.
    :returns: "file" if this is an open file, "closed file" if it is a closed file handle, or nil if not a file handle.
    """
    pass
  @staticmethod
  def write(*args)->None:
    """
    Write to the currently opened output file.
    This is equivalent to io.output():write(...). See thedocumentation there for full details.
    :param args: The strings to write
    """
    pass