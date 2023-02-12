from luatypes import *
from term import *

class Window:
  def write(self, sText)->None:
    """
    """
    pass

  def blit(self, sText, sTextColor, sBackgroundColor)->None:
    """
    """
    pass

  def clear(self)->None:
    """
    """
    pass

  def clearLine(self)->None:
    """
    """
    pass

  def getCursorPos(self)->None:
    """
    """
    pass

  def setCursorPos(self, x, y)->None:
    """
    """
    pass

  def setCursorBlink(self, blink)->None:
    """
    """
    pass

  def getCursorBlink(self)->None:
    """
    """
    pass

  def isColor(self)->None:
    """
    """
    pass

  def isColour(self)->None:
    """
    """
    pass

  def setTextColor(self, color)->None:
    """
    """
    pass

  def setTextColour(self, color)->None:
    """
    """
    pass

  def setPaletteColour(self , colour, r, g, b)->None:
    """
    """
    pass

  def setPaletteColor(self, colour, r, g, b)->None:
    """
    """
    pass

  def getPaletteColour(self, colour)->None:
    """
    """
    pass

  def getPaletteColor(self, colour)->None:
    """
    """
    pass

  def setBackgroundColor(self, color)->None:
    """
    """
    pass

  def setBackgroundColour(self, color)->None:
    """
    """
    pass

  def getSize(self)->None:
    """
    """
    pass

  def scroll(self, n)->None:
    """
    """
    pass

  def getTextColor(self)->None:
    """
    """
    pass

  def getTextColour(self)->None:
    """
    """
    pass

  def getBackgroundColor(self)->None:
    """
    """
    pass

  def getBackgroundColour(self)->None:
    """
    """
    pass

  def getLine(self, y:number)->string:
    """
    Get the buffered contents of a line in this window.

    If y is not between 1 and this window's height.

    :param y: The y position of the line to get.
    :returns: The textual content of this line.
    """
    pass

  def setVisible(self, visible:boolean)->None:
    """
    Set whether this window is visible. Invisible windows will not be drawn to the screen until they are made visible again.

    Making an invisible window visible will immediately draw it.

    :param visible: Whether this window is visible.
    """
    pass

  def isVisible(self)->boolean:
    """
    Get whether this window is visible. Invisible windows will not bedrawn to the screen until they are made visible again.

    :returns: Whether this window is visible.
    """
    pass

  def redraw(self)->None:
    """
    Draw this window. This does nothing if the window is not visible.

    """
    pass

  def restoreCursor(self)->None:
    """
    Set the current terminal's cursor to where this window's cursor is. Thisdoes nothing if the window is not visible.

    """
    pass

  def getPosition(self)->number:
    """
    Get the position of the top left corner of this window.

    :returns: The x position of this
    """
    pass

  def reposition(self, new_x:number, new_y:number, new_width:number=None, new_height:number=None, new_parent:Redirect=None)->None:
    """
    Reposition or resize the given window.

    This function also accepts arguments to change the size of this window.It is recommended that you fire a term_resize event after changing a window's, to allow programs to adjust their sizing.

    :param new_x: The new x position of this window.
    :param new_y: The new y position of this window.
    :param new_width: The new width of this window.
    :param new_height: The new height of this window.
    :param new_parent: The new redirect object this
window should draw to.
    """
    pass

class window:
  @staticmethod
  def create(parent:Redirect, nX:number, nY:number, nWidth:number, nHeight:number, bStartVisible=None)->Window:
    """
    Returns a terminal object that is a space within the specified parent terminal object. This can then be used (or even redirected to) in the same manner as eg a wrapped monitor. Refer to the term API for a list of functions available to it.

    term itself may not be passed as the parent, though term.native is acceptable. Generally, term.current or a wrapped monitor will be most suitable, though windows may even have other windows assigned as their parents.

    Create a smaller window, fill it red and write some text to it.

    Create a smaller window and redirect to it.

    :param parent: The parent terminal redirect to draw to.
    :param nX: The x coordinate this window is drawn at in the parent terminal
    :param nY: The y coordinate this window is drawn at in the parent terminal
    :param nWidth: The width of this window
    :param nHeight: The height of this window
    :param bStartVisible: Whether this window is visible by
default. Defaults to true.
    :returns: The constructed window
    """
    pass