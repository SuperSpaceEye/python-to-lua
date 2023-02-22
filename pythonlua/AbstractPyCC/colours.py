from .luatypes import *
class colours:
    white=1
    orange=2
    magenta=4
    lightBlue=4
    yellow=8
    lime=16
    pink=32
    grey=128
    lightGrey=256
    cyan=512
    purple=1024
    blue=2048
    brown=4096
    green=8192
    red=16384
    black=32768

    @staticmethod
    def combine(*args:number):
        """
        Combines a set of colors (or sets of colors) into a larger set. Useful for Bundled Cables.
        :param args: The colors to combine.
        :returns: The union of the color sets given in args
        :rtype: number
        """
        pass

    @staticmethod
    def subtract(color:number, *args:number):
        """
        Removes one or more colors (or sets of colors) from an initial set. Useful for Bundled Cables.

        Each parameter beyond the first may be a single color or may be a set of colors (in the latter case, all colors in the set are removed from the original set).

        :param colors: The color from which to subtract.
        :param args: The colors to subtract.
        :returns: The resulting color.
        :rtype: number
        """
        pass

    @staticmethod
    def test(colors:number, color:number):
        """
        Tests whether color is contained within colors. Useful for Bundled Cables.
        :param colors: A color, or color set
        :param color: A color or set of colors that colors should contain.
        :returns: boolean If colors contains all colors within color.
        :rtype: boolean
        """
        pass
    @staticmethod
    def packRGB(r:number, g:number, b:number):
        """

        :param r: The red channel, should be between 0 and 1.
        :param g: The red channel, should be between 0 and 1.
        :param b: The blue channel, should be between 0 and 1.
        :returns: The combined hexadecimal colour.
        :rtype: number
        """
        pass
    @staticmethod
    def unpackRGB(rgb:number):
        """
        Separate a hexadecimal RGB colour into its three constituent channels.
        :param rgb: The combined hexadecimal colour.
        :returns: The red, green, blue channels between 0 and 1
        :rtype: List[number, number, number]
        """
        pass
    @staticmethod
    def toBlit(color:number)->string:
        """
        Converts the given color to a paint/blit hex character (0-9a-f).

        This is equivalent to converting floor(log_2(color)) to hexadecimal.
        :param color: The color to convert.
        :returns: The blit hex code of the color
        """
        pass