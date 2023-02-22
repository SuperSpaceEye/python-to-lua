from .luatypes import *

class paintutils:
  @staticmethod
  def parseImage(image:string)->table:
    """
    Parses an image from a multi-line string

    :param image: The string containing the raw-image data.
    :returns: The parsed image data, sui for use with paintutils.drawImage.
    """
    pass
  @staticmethod
  def loadImage(path:string)->table | None:
    """
    Loads an image from a file.

    You can create a file suitable for being loaded using the paint program.

    Load an image and draw it.

    :param path: The file to load.
    :returns: The parsed image data, suitable for use with paintutils.drawImage, or nil if the file does not exist.
    """
    pass
  @staticmethod
  def drawPixel(xPos:number, yPos:number, colour:number=None)->None:
    """
    Draws a single pixel to the current term at the specified position.

    Be warned, this may change the position of the cursor and the currentbackground colour. You should not expect either to be preserved.

    :param xPos: The x position to draw at, where 1 is the far left.
    :param yPos: The y position to draw at, where 1 is the very top.
    :param colour: The color of this pixel. This will be the current background colour if not specified.
    """
    pass
  @staticmethod
  def drawLine(startX:number, startY:number, endX:number, endY:number, colour:number=None)->None:
    """
    Draws a straight line from the start to end position.

    Be warned, this may change the position of the cursor and the current background colour. You should not expect either to be preserved.

    :param startX: The starting x position of the line.
    :param startY: The starting y position of the line.
    :param endX: The end x position of the line.
    :param endY: The end y position of the line.
    :param colour: The color of this pixel. This will be the current background colour if not specified.
    """
    pass
  @staticmethod
  def drawBox(startX:number, startY:number, endX:number, endY:number, colour:number=None)->None:
    """
    Draws the outline of a box on the current term from the specified start position to the specified end position.

    Be warned, this may change the position of the cursor and the current background colour. You should not expect either to be preserved.

    :param startX: The starting x position of the line.
    :param startY: The starting y position of the line.
    :param endX: The end x position of the line.
    :param endY: The end y position of the line.
    :param colour: The color of this pixel. This will be the current background colour if not specified.
    """
    pass
  @staticmethod
  def drawFilledBox(startX:number, startY:number, endX:number, endY:number, colour:number=None)->None:
    """
    Draws a filled box on the current term from the specified start position to the specified end position.

    Be warned, this may change the position of the cursor and the current background colour. You should not expect either to be preserved.

    :param startX: The starting x position of the line.
    :param startY: The starting y position of the line.
    :param endX: The end x position of the line.
    :param endY: The end y position of the line.
    :param colour: The color of this pixel. This will be the current background colour if not specified.
    """
    pass
  @staticmethod
  def drawImage(image:table, xPos:number, yPos:number)->None:
    """
    Draw an image loaded by paintutils.parseImage or paintutils.loadImage.

    :param image: The parsed image data.
    :param xPos: The x position to start drawing at.
    :param yPos: The y position to start drawing at.
    """
    pass