from luatypes import *

class Websocket:
  def receive(self, timeout:number=None)->List[string, boolean]|None:
    """
    Wait for a message from the server.
    If the websocket has been closed.
    :param timeout?: The number of seconds to wait if no message is received.
    :returns: The received message and bool if message was binary or None
    """
    pass

  def send(self, message:any, binary:boolean=None)->None:
    """
    Send a websocket message to the connected server.
    Throws:
    * If the message is too large.
    * If the websocket has been closed.
    :param message: The message to send.
    :param binary?: Whether this message should be treated as a
    """
    pass
  def close(self)->None:
    """
    Close this websocket. This will terminate the connection, meaning messages can no longer be sent or receivedalong it.
    """
    pass
class Response:
  def getResponseCode(self)->List[number, string]:
    """
    Returns the response code and response message returned by the server.
    :returns: The response code (i.e. 200) and response massage
    """
    pass
  def getResponseHeaders(self)->table[string]:
    """
    Get a table containing the response's headers, in a format similar to that required by http.request.If multiple headers are sent with the same name, they will be combined with a comma.
    Make a request to example.tweaked.cc, and print thereturned headers.
    :returns: The response's headers.
    """
    pass

class http:
  @staticmethod
  def get(*args)->Response|None:
    """
    Make a HTTP GET request to the given url.
    Parameters:

    * url: string The url to request
    * headers: table[string]? Additional headers to send as part of this request.
    * binary: bool? Whether to make a binary HTTP request. If true, the body will not be UTF-8 encoded, and the received response will not be decoded.
    Or

    * request: table[url:string, headers:table[string:string], binary:bool?, method:string?, redirect:bool?] Options for the request. See http.request for details on how
these options behave.
    :returns: The resulting http response, which can be read from.
    """
    pass
  @staticmethod
  def post(*args)->Response|None:
    """
    Make a HTTP POST request to the given url.
    Parameters:

    * url: The url to request
    * body: The body of the POST request.
    * headers?: Additional headers to send as part of this request.
    * binary?: Whether to make a binary HTTP request. If true, the body will not be UTF-8 encoded, and the received response will not be decoded.
    Or:

    * request: Options for the request. See http.request for details on how these options behave.
    :returns: The resulting http response, which can be read from.
    """
    pass
  @staticmethod
  def request(*args)->None:
    """
    Asynchronously make a HTTP request to the given url.

    This returns immediately, a http_success or http_failure will be queued once the request has completed.

    Options for the request.

    This table form is an expanded version of the previous syntax. All arguments from above are passed in as fields instead (for instance,http.request("https://example.com") becomes http.request { url = "https://example.com" }).This table also accepts several additional options:

    * url: The url to request
    * body?: An optional string containing the body of the request. If specified, a POST request will be made instead.
    * headers?: Additional headers to send as part of this request.
    * binary?: Whether to make a binary HTTP request. If true, the body will not be UTF-8 encoded, and the received response will not be decoded.

    Or:

    * request:  { url = string, body? = string, headers? = { [string] = string }, binary? = boolean, method? = string, redirect? = boolean } Options for the request.
This table form is an expanded version of the previous syntax. All arguments
from above are passed in as fields instead (for instance,
http.request("https://example.com") becomes http.request { url = "https://example.com" }).
This table also accepts several additional options:

method: Which HTTP method to use, for instance "PATCH" or "DELETE".

redirect: Whether to follow HTTP redirects. Defaults to true.
    """
    pass
  @staticmethod
  def checkURLAsync(url:string)->boolean | List[boolean, string]:
    """
    Asynchronously determine whether a URL can be requested.
    If this returns true, one should also listen for http_check which willcontainer further information about whether the URL is allowed or not.
    :param url: The URL to check.
    :returns: true When this url is not invalid. This does not imply that it is allowed - see the comment above. Or false and string with the reason
    """
    pass
  @staticmethod
  def checkURL(url:string)->boolean | List[boolean, string]:
    """
    Determine whether a URL can be requested.
    If this returns true, one should also listen for http_check which willcontainer further information about whether the URL is allowed or not.
    :param url: The URL to check.
    :returns: true When this url is valid and can be requested via http.request. Or false and string with the reason
    """
    pass
  @staticmethod
  def websocketAsync(url:string, headers:string=None)->None:
    """
    Asynchronously open a websocket.
    This returns immediately, a websocket_success or websocket_failurewill be queued once the request has completed.
    :param url: The websocket url to connect to. This should have the ws:// or wss:// protocol.
    :param headers: Additional headers to send as part of the initial websocket connection.
    """
    pass
  @staticmethod
  def websocket(url:string, headers:string=None)->Websocket:
    """
    Open a websocket.
    :param url: The websocket url to connect to. This should have the ws:// or wss:// protocol.
    :param headers: Additional headers to send as part of the initial websocket connection.
    :returns: The websocket connection.
    """
    pass