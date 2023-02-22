from .luatypes import *

class textutils:
  @staticmethod
  def slowWrite(text:string, rate:number=20)->None:
    """
    Slowly writes string text at current cursor position,character-by-character.

    Like _G.write, this does not insert a newline at the end.

    :param text: The text to write to the screen
    :param rate: The number of characters to write each second, Defaults to 20.
    """
    pass
  @staticmethod
  def slowPrint(sText:string, nRate:number=20)->None:
    """
    Slowly prints string text at current cursor position,character-by-character.

    Like print, this inserts a newline after printing.

    :param sText: The text to write to the screen
    :param nRate: The number of characters to write each second, Defaults to 20.
    """
    pass
  @staticmethod
  def formatTime(nTime:number, bTwentyFourHour:boolean=None)->string:
    """
    Takes input time and formats it in a more readable format such as 6:30 PM.

    :param nTime: The time to format, as provided by os.time.
    :param bTwentyFourHour: Whether to format this as a 24-hour clock (18:30) rather than a 12-hour one (6:30 AM)
    :returns: The formatted time
    """
    pass
  @staticmethod
  def pagedPrint(text:string, free_lines:number=None)->number:
    """
    Prints a given string to the display.

    If the action can be completed without scrolling, it acts much the same asprint; otherwise, it will throw up a "Press any key to continue" prompt atthe bottom of the display. Each press will cause it to scroll down and write asingle line more before prompting again, if need be.

    :param text: The text to print to the screen.
    :param free_lines: The number of lines which will be automatically scrolled before the first prompt appears (meaning free_lines + 1 lines will be printed). This can be set to the cursor's y position - 2 to always try to fill the screen. Defaults to 0, meaning only one line is displayed before prompting.
    :returns: The number of lines printed.
    """
    pass
  @staticmethod
  def tabulate(*args)->None:
    """
    Prints tables in a structured form.

    This accepts multiple arguments, either a table or a number. Whenencountering a table, this will be treated as a table row, with each columnwidth being auto-adjusted.

    When encountering a number, this sets the text color of the subsequent rows to it.

    :param args: table[string]|number The rows and text colors to display.
    """
    pass
  @staticmethod
  def pagedTabulate(*args)->None:
    """
    Prints tables in a structured form, stopping and prompting for input shouldthe result not fit on the terminal.

    This functions identically to textutils.tabulate, but will prompt for userinput should the whole output not fit on the display.

    :param args: table[string]|number The rows and text colors to display.
    """
    pass
  @staticmethod
  def empty_json_array()->None:
    """
    A table representing an empty JSON array, in order to distinguish it from anempty JSON object.

    The contents of this table should not be modified.

    """
    pass
  @staticmethod
  def json_null()->None:
    """
    A table representing the JSON null value.

    The contents of this table should not be modified.

    """
    pass
  @staticmethod
  def serialize(t, opts:table[boolean, boolean])->string:
    """
    Convert a Lua object into a textual representation, suitable for saving in a file or pretty-printing.

    :param t: The object to serialise
    :param opts: { compact? = boolean, allow_repetitions? = boolean }
    Options for serialisation.

    * compact: Do not emit indentation and other whitespace between terms.
    * allow_repetitions: Relax the check for recursive tables, allowing them to appear multiple times (as long as tables do not appear inside themselves).

    Throws:

    * If the object contains a value which cannot be serialised. This includes functions and tables which appear multiple times.

    :returns: The serialised representation
    """
    pass
  @staticmethod
  def serialise(t, opts)->string:
    """
    Convert a Lua object into a textual representation, suitable for saving in a file or pretty-printing.

    :param t: The object to serialise
    :param opts: { compact? = boolean, allow_repetitions? = boolean }
    Options for serialisation.

    * compact: Do not emit indentation and other whitespace between terms.
    * allow_repetitions: Relax the check for recursive tables, allowing them to appear multiple times (as long as tables do not appear inside themselves).

    Throws:

    * If the object contains a value which cannot be serialised. This includes functions and tables which appear multiple times.

    :returns: The serialised representation
    """
    pass
  @staticmethod
  def unserialize(s:string)->any:
    """
    Converts a serialised string back into a reassembled Lua object.

    This is mainly used together with textutils.serialise.

    :param s: The serialised string to deserialise.
    :returns: deserialized object or None if object cannot be deserialized
    """
    pass
  @staticmethod
  def unserialise(s:string)->any:
    """
    Converts a serialised string back into a reassembled Lua object.

    This is mainly used together with textutils.serialise.

    :param s: The serialised string to deserialise.
    :returns: deserialized object or None if object cannot be deserialized
    """
    pass
  @staticmethod
  def serializeJSON(t, bNBTStyle:boolean=None)->string:
    """
    Returns a JSON representation of the given data.

    This function attempts to guess whether a table is a JSON array or object. However, empty tables are assumed to be empty objects - use textutils.empty_json_array to mark an empty array.

    This is largely intended for interacting with various functions from the commands API, though may also be used in making http requests.

    Throws:

    * If the object contains a value which cannot be serialised. This includes functions and tables which appear multiple times.

    :returns: The JSON representation of the input
    """
    pass
  @staticmethod
  def serialiseJSON(t, bNBTStyle:boolean=None)->string:
    """
    Returns a JSON representation of the given data.

    This function attempts to guess whether a table is a JSON array or object. However, empty tables are assumed to be empty objects - use textutils.empty_json_array to mark an empty array.

    This is largely intended for interacting with various functions from the commands API, though may also be used in making http requests.

    Throws:

    * If the object contains a value which cannot be serialised. This includes functions and tables which appear multiple times.

    :returns: The JSON representation of the input
    """
    pass
  @staticmethod
  def unserializeJSON(s:string, options:table)->any:
    """
    Converts a serialised JSON string back into a reassembled Lua object.

    This may be used with textutils.serializeJSON, or when communicatingwith command blocks or web APIs.

    If a null value is encountered, it is converted into nil. It can be convertedinto textutils.json_null with the parse_null option.

    If an empty array is encountered, it is converted into textutils.empty_json_array.It can be converted into a new empty table with the parse_empty_array option.

    Options which control how this JSON object is parsed.

    * nbt_style: When true, this will accept stringified NBT strings, as produced by many commands.
    * parse_null: When true, null will be parsed as json_null, rather than nil.
    * parse_empty_array: When false, empty arrays will be parsed as a new table. By default (or when this value is true), they are parsed as empty_json_array.

    :param s: The serialised string to deserialise.
    :param options?: Options which control how this JSON object is parsed.
    :returns: The deserialised object or None if the object couldn't be deserialised and string describing why
    """
    pass
  @staticmethod
  def unserialiseJSON(s:string, options:table)->any:
    """
    Converts a serialised JSON string back into a reassembled Lua object.

    This may be used with textutils.serializeJSON, or when communicatingwith command blocks or web APIs.

    If a null value is encountered, it is converted into nil. It can be convertedinto textutils.json_null with the parse_null option.

    If an empty array is encountered, it is converted into textutils.empty_json_array.It can be converted into a new empty table with the parse_empty_array option.

    Options which control how this JSON object is parsed.

    * nbt_style: When true, this will accept stringified NBT strings, as produced by many commands.
    * parse_null: When true, null will be parsed as json_null, rather than nil.
    * parse_empty_array: When false, empty arrays will be parsed as a new table. By default (or when this value is true), they are parsed as empty_json_array.

    :param s: The serialised string to deserialise.
    :param options?: Options which control how this JSON object is parsed.
    :returns: The deserialised object or None if the object couldn't be deserialised and string describing why
    """
    pass
  @staticmethod
  def urlEncode(str:string)->string:
    """
    Replaces certain characters in a string to make it safe for use in URLs or POST data.

    :param str: The string to encode
    :returns: The encoded string.
    """
    pass
  @staticmethod
  def complete(sSearchText:string, tSearchTable:table)->table[string]:
    """
    Provides a list of possible completions for a partial Lua expression.

    If the completed element is a table, suggestions will have . appended tothem. Similarly, functions have ( appended to them.

    :param sSearchText: The partial expression to complete, such as a variable name or table index.
    :param tSearchTable: The table to find variables in, defaulting to the global environment (_G). The function also searches the "parent" environment via the __index metatable field.
    :returns: The (possibly empty) list of completions.
    """
    pass