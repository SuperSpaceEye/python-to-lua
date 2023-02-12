from luatypes import *

class gps:
    #The channel which GPS requests and responses are broadcast on.
    CHANNEL_GPS = 65534

    @staticmethod
    def locate(timeout=2, debug=False)->List[number, number, number]:
        """
        Tries to retrieve the computer or turtles own location.

        :param timeout: The maximum time in seconds taken to establish our position.
        :param debug: Print debugging messages.
        :returns: x, y, z computer's position
        """
        pass