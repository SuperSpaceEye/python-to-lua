from luatypes import *

class Redirect:
  def write(self, text:string)->None:
    """
    Write text at the current cursor position, moving the cursor to the end of the text.

    Unlike functions like write and print, this does not wrap the text - it simply copies thetext to the current terminal line.

    """
    pass

  def scroll(self, y:number)->None:
    """
    Move all positions up (or down) by y pixels.

    Every pixel in the terminal will be replaced by the line y pixels below it. If y is negative, itwill copy pixels from above instead.

    :param y: The number of lines to move up by. This may be a negative number.
    """
    pass

  def getCursorPos(self)->List[number, number]:
    """
    Get the position of the cursor.

    :returns: The x position of the cursor.
    """
    pass

  def setCursorPos(self, x:number, y:number)->None:
    """
    Set the position of the cursor. terminal writes will begin from this position.

    :param x: The new x position of the cursor.
    :param y: The new y position of the cursor.
    """
    pass

  def getCursorBlink(self)->boolean:
    """
    Checks if the cursor is currently blinking.

    :returns: If the cursor is blinking.
    """
    pass

  def setCursorBlink(self, blink:boolean)->None:
    """
    Sets whether the cursor should be visible (and blinking) at the current cursor position.

    :param blink: Whether the cursor should blink.
    """
    pass

  def getSize(self)->List[number, number]:
    """
    Get the size of the terminal.

    :returns: The terminal's width && height.
    """
    pass

  def clear(self)->None:
    """
    Clears the terminal, filling it with the current background colour.

    """
    pass

  def clearLine(self)->None:
    """
    Clears the line the cursor is currently on, filling it with the current background colour.

    """
    pass

  def getTextColour(self)->number:
    """
    Return the colour that new text will be written as.

    :returns: The current text colour.
    """
    pass

  def getTextColor(self)->number:
    """
    Return the colour that new text will be written as.

    :returns: The current text colour.
    """
    pass

  def setTextColour(self, colour:number)->None:
    """
    Set the colour that new text will be written as.

    :param colour: The new text colour.
    """
    pass

  def setTextColor(self, colour:number)->None:
    """
    Set the colour that new text will be written as.

    :param colour: The new text colour.
    """
    pass

  def getBackgroundColour(self)->number:
    """
    Return the current background colour. This is used when writing text and clearingthe terminal.

    :returns: The current background colour.
    """
    pass

  def getBackgroundColor(self)->number:
    """
    Return the current background colour. This is used when writing text and clearingthe terminal.

    :returns: The current background colour.
    """
    pass

  def setBackgroundColour(self, colour:number)->None:
    """
    Set the current background colour. This is used when writing text and clearing theterminal.

    :param colour: The new background colour.
    """
    pass

  def setBackgroundColor(self, colour:number)->None:
    """
    Set the current background colour. This is used when writing text and clearing theterminal.

    :param colour: The new background colour.
    """
    pass

  def isColour(self)->boolean:
    """
    Determine if this terminal supports colour.

    Terminals which do not support colour will still allow writing coloured text/backgrounds, but it will bedisplayed in greyscale.

    :returns: Whether this terminal supports colour.
    """
    pass

  def isColor(self)->boolean:
    """
    Determine if this terminal supports colour.

    Terminals which do not support colour will still allow writing coloured text/backgrounds, but it will bedisplayed in greyscale.

    :returns: Whether this terminal supports colour.
    """
    pass

  def blit(self, text:string, textColour:string, backgroundColour:string)->None:
    """
    Writes text to the terminal with the specific foreground and background characters.

    As with write, the text will be written at the current cursor location, with the cursormoving to the end of the text.

    textColour and backgroundColour must both be strings the same length as text. Allcharacters represent a single hexadecimal digit, which is converted to one of CC's colours. For instance,"a" corresponds to purple.

    Throws:

    * If the three inputs are not the same length.

    :param text: The text to write.
    :param textColour: The corresponding text colours.
    :param backgroundColour: The corresponding background colours.
    """
    pass

  def setPaletteColour(self, *args)->None:
    """
    Set the palette for a specific colour.

    ComputerCraft's palette system allows you to change how a specific colour should be displayed. For instance, youcan make colors.red more red by setting its palette to #FF0000. This does now allow you to draw morecolours - you are still limited to 16 on the screen at one time - but you can change which colours areused.

    Parameters:

    * index: number The colour whose palette should be changed.
    * colour: number A 24-bit integer representing the RGB value of the colour. For instance the integer
0xFF0000 corresponds to the colour #FF0000.

    OR:

    * index: The colour whose palette should be changed.
    * r: number The intensity of the red channel, between 0 and 1.
    * g: number The intensity of the green channel, between 0 and 1.
    * b: number The intensity of the blue channel, between 0 and 1.
    """
    pass

  def setPaletteColor(self, *args)->None:
    """
      Set the palette for a specific colour.

      ComputerCraft's palette system allows you to change how a specific colour should be displayed. For instance, youcan make colors.red more red by setting its palette to #FF0000. This does now allow you to draw morecolours - you are still limited to 16 on the screen at one time - but you can change which colours areused.

      Parameters:

      * index: number The colour whose palette should be changed.
      * colour: number A 24-bit integer representing the RGB value of the colour. For instance the integer
  0xFF0000 corresponds to the colour #FF0000.

      OR:

      * index: The colour whose palette should be changed.
      * r: number The intensity of the red channel, between 0 and 1.
      * g: number The intensity of the green channel, between 0 and 1.
      * b: number The intensity of the blue channel, between 0 and 1.
      """
    pass

  def getPaletteColour(self, colour:number)->List[number, number, number]:
    """
    Get the current palette for a specific colour.

    :param colour: The colour whose palette should be fetched.
    :returns: The red,green,blue channels, will be between 0 and 1.
    """
    pass

  def getPaletteColor(self, colour:number)->List[number, number, number]:
    """
    Get the current palette for a specific colour.

    :param colour: The colour whose palette should be fetched.
    :returns: The red,green,blue channels, will be between 0 and 1.
    """
    pass

class term:
  @staticmethod
  def nativePaletteColour(colour:number)->List[number, number, number]:
    """
    Get the default palette value for a colour.

    When given an invalid colour.

    :param colour: The colour whose palette should be fetched.
    :returns: The red,green,blue channels, will be between 0 and 1.
    """
    pass
  @staticmethod
  def nativePaletteColor(colour:number)->List[number, number, number]:
    """
    Get the default palette value for a colour.

    When given an invalid colour.

    :param colour: The colour whose palette should be fetched.
    :returns: The red,green,blue channels, will be between 0 and 1.
    """
    pass
  @staticmethod
  def write(text)->None:
    """
    Write text at the current cursor position, moving the cursor to the end of the text.

    Unlike functions like write and print, this does not wrap the text - it simply copies thetext to the current terminal line.

    """
    pass
  @staticmethod
  def scroll(y:number)->None:
    """
    Move all positions up (or down) by y pixels.

    Every pixel in the terminal will be replaced by the line y pixels below it. If y is negative, itwill copy pixels from above instead.

    :param y: The number of lines to move up by. This may be a negative number.
    """
    pass
  @staticmethod
  def getCursorPos()->List[number, number]:
    """
    Get the position of the cursor.

    :returns: The x,y position of the cursor.
    """
    pass
  @staticmethod
  def setCursorPos(x:number, y:number)->None:
    """
    Set the position of the cursor. terminal writes will begin from this position.

    :param x: The new x position of the cursor.
    :param y: The new y position of the cursor.
    """
    pass
  @staticmethod
  def getCursorBlink()->boolean:
    """
    Checks if the cursor is currently blinking.

    :returns: If the cursor is blinking.
    """
    pass
  @staticmethod
  def setCursorBlink(blink:boolean)->None:
    """
    Sets whether the cursor should be visible (and blinking) at the current cursor position.

    :param blink: Whether the cursor should blink.
    """
    pass
  @staticmethod
  def getSize()->number:
    """
    Get the size of the terminal.

    :returns: The terminal's width.
    """
    pass
  @staticmethod
  def clear()->None:
    """
    Clears the terminal, filling it with the current background colour.

    """
    pass
  @staticmethod
  def clearLine()->None:
    """
    Clears the line the cursor is currently on, filling it with the current backgroundcolour.

    """
    pass
  @staticmethod
  def getTextColour()->number:
    """
    Return the colour that new text will be written as.

    :returns: The current text colour.
    """
    pass
  @staticmethod
  def getTextColor()->number:
    """
    Return the colour that new text will be written as.

    :returns: The current text colour.
    """
    pass
  @staticmethod
  def setTextColour(colour:number)->None:
    """
    Set the colour that new text will be written as.

    :param colour: The new text colour.
    """
    pass
  @staticmethod
  def setTextColor(colour:number)->None:
    """
    Set the colour that new text will be written as.

    :param colour: The new text colour.
    """
    pass
  @staticmethod
  def getBackgroundColour()->number:
    """
    Return the current background colour. This is used when writing text and clearingthe terminal.

    :returns: The current background colour.
    """
    pass
  @staticmethod
  def getBackgroundColor()->number:
    """
    Return the current background colour. This is used when writing text and clearingthe terminal.

    :returns: The current background colour.
    """
    pass
  @staticmethod
  def setBackgroundColour(colour:number)->None:
    """
    Set the current background colour. This is used when writing text and clearing theterminal.

    :param colour: The new background colour.
    """
    pass
  @staticmethod
  def setBackgroundColor(colour:number)->None:
    """
    Set the current background colour. This is used when writing text and clearing theterminal.

    :param colour: The new background colour.
    """
    pass
  @staticmethod
  def isColour()->boolean:
    """
    Determine if this terminal supports colour.

    Terminals which do not support colour will still allow writing coloured text/backgrounds, but it will bedisplayed in greyscale.

    :returns: Whether this terminal supports colour.
    """
    pass
  @staticmethod
  def isColor()->boolean:
    """
    Determine if this terminal supports colour.

    Terminals which do not support colour will still allow writing coloured text/backgrounds, but it will bedisplayed in greyscale.

    :returns: Whether this terminal supports colour.
    """
    pass
  @staticmethod
  def blit(text:string, textColour:string, backgroundColour:string)->None:
    """
    Writes text to the terminal with the specific foreground and background characters.

    As with write, the text will be written at the current cursor location, with the cursormoving to the end of the text.

    textColour and backgroundColour must both be strings the same length as text. Allcharacters represent a single hexadecimal digit, which is converted to one of CC's colours. For instance,"a" corresponds to purple.

    :param text: The text to write.
    :param textColour: The corresponding text colours.
    :param backgroundColour: The corresponding background colours.
    """
    pass
  @staticmethod
  def setPaletteColour(*args)->None:
    """
    Set the palette for a specific colour.

    ComputerCraft's palette system allows you to change how a specific colour should be displayed. For instance, youcan make colors.red more red by setting its palette to #FF0000. This does now allow you to draw morecolours - you are still limited to 16 on the screen at one time - but you can change which colours areused.

    Parameters:

    * index: The colour whose palette should be changed.
    * colour: A 24-bit integer representing the RGB value of the colour. For instance the integer
0xFF0000 corresponds to the colour #FF0000.

    OR:

    * index: The colour whose palette should be changed.
    * r: The intensity of the red channel, between 0 and 1.
    * g: The intensity of the green channel, between 0 and 1.
    * b: The intensity of the blue channel, between 0 and 1.
    """
    pass
  @staticmethod
  def setPaletteColor(*args)->None:
    """
    Set the palette for a specific colour.

    ComputerCraft's palette system allows you to change how a specific colour should be displayed. For instance, youcan make colors.red more red by setting its palette to #FF0000. This does now allow you to draw morecolours - you are still limited to 16 on the screen at one time - but you can change which colours areused.

    Parameters:

    * index: The colour whose palette should be changed.
    * colour: A 24-bit integer representing the RGB value of the colour. For instance the integer
0xFF0000 corresponds to the colour #FF0000.

    OR:

    * index: The colour whose palette should be changed.
    * r: The intensity of the red channel, between 0 and 1.
    * g: The intensity of the green channel, between 0 and 1.
    * b: The intensity of the blue channel, between 0 and 1.
    """
    pass
  @staticmethod
  def getPaletteColour(colour:number)->number:
    """
    Get the current palette for a specific colour.

    :param colour: The colour whose palette should be fetched.
    :returns: The red,green,blue channels, will be between 0 and 1.
    """
    pass
  @staticmethod
  def getPaletteColor(colour:number)->number:
    """
    Get the current palette for a specific colour.

    :param colour: The colour whose palette should be fetched.
    :returns: The red,green,blue channels, will be between 0 and 1.
    """
    pass
  @staticmethod
  def redirect(target:Redirect)->Redirect:
    """
    Redirects terminal output to a monitor, a window, or any other customterminal object. Once the redirect is performed, any calls to a "term"function - or to a function that makes use of a term function, as print -will instead operate with the new terminal object.

    A "terminal object" is simply a table that contains functions with the samenames - and general features - as those found in the term table. For example,a wrapped monitor is suitable.

    The redirect can be undone by pointing back to the previous terminal object(which this function returns whenever you switch).

    :param target: The terminal redirect the term API will draw to.
    :returns: The previous redirect object, as returned by term.current.
    """
    pass
  @staticmethod
  def current()->Redirect:
    """
    Returns the current terminal object of the computer.

    Create a new window which draws to the current redirect target.

    :returns: The current terminal redirect
    """
    pass
  @staticmethod
  def native()->Redirect:
    """
    Get the native terminal object of the current computer.

    It is recommended you do not use this function unless you absolutely haveto. In a multitasked environment, term.native will not be the currentterminal object, and so drawing may interfere with other programs.

    :returns: The native terminal redirect.
    """
    pass