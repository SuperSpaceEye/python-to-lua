from .luatypes import *

class rednet:
  """
  The channel used by the Rednet API to broadcast messages.
  """
  CHANNEL_BROADCAST = 65535

  """
  The channel used by the Rednet API to repeat messages.
  """
  CHANNEL_REPEAT = 65533

  """
  The number of channels rednet reserves for computer IDs. Computers with IDs greater or equal to this limit wrap around to 0.
  """
  MAX_ID_CHANNELS = 65500
  @staticmethod
  def open(modem:string)->None:
    """
    Opens a modem with the given peripheral name, allowing it to send and receive messages over rednet.

    This will open the modem on two channels: one which has the sameID as the computer, and another on the broadcast channel.

    Throws:

    * If there is no such modem with the given name

    :param modem: The name of the modem to open.
    """
    pass
  @staticmethod
  def close(modem:string=None)->None:
    """
    Close a modem with the given peripheral name, meaning it can no longer send and receive rednet messages.

    Throws:

    *If there is no such modem with the given name

    :param modem: The side the modem exists on. If not given, all open modems will be closed.
    """
    pass
  @staticmethod
  def isOpen(modem:string=None)->boolean:
    """
    Determine if rednet is currently open.

    :param modem: Which modem to check. If not given, all connected modems will be checked.
    :returns: If the given modem is open.
    """
    pass
  @staticmethod
  def send(recipient:number, message:number|boolean|string, protocol:string=None)->None:
    """
    Allows a computer or turtle with an attached modem to send a message intended for a sycomputer with a specific ID. At least one such modem must first be opened before sending is possible.

    Assuming the target was in range and also had a correctly opened modem, the target computer may then use rednet.receive to collect the message.

    :param recipient: The ID of the receiving computer.
    :param message: The message to send. Like with modem.transmit, this can contain any primitive type (numbers, booleans and strings) as well as tables. Other types (like functions), as well as metatables, will not be transmitted.
    :param protocol: The "protocol" to send this message under. When using rednet.receive one can filter to only receive messages sent under a particular protocol.
    """
    pass
  @staticmethod
  def broadcast(message, protocol:string=None)->None:
    """
    Broadcasts a string message over the predefined CHANNEL_BROADCASTchannel. The message will be received by every device listening to rednet.

    :param message:  The message to send. This should not contain coroutines or functions, as they will be converted to nil.
    :param protocol: The "protocol" to send this message under. When using rednet.receive one can filter to only receive messages sent under a particular protocol.
    """
    pass
  @staticmethod
  def receive(protocol_filter:string=None, timeout:number=None)->List[number, string, string|None]|None:
    """
    Wait for a rednet message to be received, or until nTimeout seconds have elapsed.

    :param protocol_filter: The protocol the received message must be sent with. If specified, any messages not sent under this protocol will be discarded.
    :param timeout: The number of seconds to wait if no message is received.
    :returns: The computer which sent this message, the received message, string|None the protocol this message was sent under OR None if the timeout elapsed and no message was received
    """
    pass
  @staticmethod
  def host(protocol:string, hostname:string)->None:
    """
    Register the system as "hosting" the desired protocol under the specifiedname. If a rednet lookup is performed for that protocol (andmaybe name) on the same network, the registered system will automaticallyrespond via a background process, hence providing the system performing thelookup with its ID number.

    Multiple computers may not register themselves on the same network as having thesame names against the same protocols, and the title localhost is specificallyreserved. They may, however, share names as long as their hosted protocols aredifferent, or if they only join a given network after "registering" themselvesbefore doing so (eg while offline or part of a different network).

    Throws:

    * If trying to register a hostname which is reserved, or currently in use.

    :param protocol: The protocol this computer provides.
    :param hostname: The name this computer exposes for the given protocol.
    """
    pass
  @staticmethod
  def unhost(protocol:string)->None:
    """
    Stop hosting a specific protocol, meaning it will no longer respond to rednet.lookup requests.

    :param protocol: The protocol to unregister your self from.
    """
    pass
  @staticmethod
  def lookup(protocol:string, hostname:string=None)->List[number]|number|None:
    """
    Search the local rednet network for systems hosting thedesired protocol and returns any computer IDs that respond as "registered"against it.

    If a hostname is specified, only one ID will be returned (assuming an exactmatch is found).

    :param protocol: The protocol to search for.
    :param hostname?: The hostname to search for.
    :returns: A list of computer IDs hosting the given protocol. OR The computer ID with the provided hostname and protocol, or nil if none exists.
    """
    pass
  @staticmethod
  def run()->None:
    """
    Listen for modem messages and converts them into rednet messages, which maythen be received.

    This is automatically started in the background on computer startup, andshould not be called manually.
    """
    pass