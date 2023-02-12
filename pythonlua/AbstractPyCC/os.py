from luatypes import *

class os:
  @staticmethod
  def loadAPI(path:string)->boolean:
    """
    When possible it's best to avoid using this function. It pollutesthe global table and can mask errors.

    require should be used to load libraries instead.

    Loads the given API into the global environment.

    This function loads and executes the file at the given path, and all globalvariables and functions exported by it will by available through the use ofmyAPI.<function name>, where myAPI is the base name of the API file.

    :param path: The path of the API to load.
    :returns: Whether or not the API was successfully loaded.
    """
    pass
  @staticmethod
  def unloadAPI(name:string)->None:
    """
    See os.loadAPI for why.

    Unloads an API which was loaded by os.loadAPI.

    This effectively removes the specified table from _G.

    :param name: The name of the API to unload.
    """
    pass
  @staticmethod
  def pullEvent(filter:string=None)->List[string, ...]:
    """
    Pause execution of the current thread and waits for any events matchingfilter.

    This function yields the current process and waits for itto be resumed with a vararg list where the first element matches filter.If no filter is supplied, this will match all events.

    Unlike os.pullEventRaw, it will stop the application upon a "terminate"event, printing the error "Terminated".

    :param filter: Event to filter for.
    :returns: event The name of the event that fired.
    """
    pass
  @staticmethod
  def pullEventRaw(filter:string=None)->List[string, ...]:
    """
    Pause execution of the current thread and waits for events, including theterminate event.

    This behaves almost the same as os.pullEvent, except it allows you to handlethe terminate event yourself - the program will not stop execution whenCtrl+T is pressed.

    :param filter: Event to filter for.
    :returns: event The name of the event that fired.
    """
    pass
  @staticmethod
  def sleep(time:number)->None:
    """
    Pauses execution for the specified number of seconds, alias of _G.sleep.

    :param time: The number of seconds to sleep for, rounded up to the nearest multiple of 0.05.
    """
    pass
  @staticmethod
  def version()->string:
    """
    Get the current CraftOS version (for example, CraftOS 1.8).

    This is defined by bios.lua. For the current version of CC:Tweaked, thisshould return CraftOS 1.8.

    :returns: The current CraftOS version.
    """
    pass
  @staticmethod
  def run(env:table, path:string, *args)->boolean:
    """
    Run the program at the given path with the specified environment andarguments.

    This function does not resolve program names like the shell does. This meansthat, for example, os.run("edit") will not work. As well as this, it does notprovide access to the shell API in the environment. For this behaviour, useshell.run instead.

    If the program cannot be found, or failed to run, it will print the error andreturn false. If you want to handle this more gracefully, use an alternativesuch as loadfile.

    :param env: The environment to run the program with.
    :param path: The exact path of the program to run.
    :param args: The arguments to pass to the program.
    :returns: Whether or not the program ran successfully.
    """
    pass
  @staticmethod
  def queueEvent(name:string, *args)->None:
    """
    Adds an event to the event queue. This event can later be pulled withos.pullEvent.

    :param name: The name of the event to queue.
    :param args: The parameters of the event.
    """
    pass
  @staticmethod
  def startTimer(timer:number)->number:
    """
    Starts a timer that will run for the specified number of seconds. Oncethe timer fires, a timer event will be added to the queue withthe ID returned from this function as the first parameter.

    As with sleep, timer will automatically be rounded upto the nearest multiple of 0.05 seconds, as it waits for a fixed amountof world ticks.

    Throws:

    * If the time is below zero.

    :param timer: The number of seconds until the timer fires.
    :returns: The ID of the new timer. This can be used to filter the timer event, or cancel the timer.
    """
    pass
  @staticmethod
  def cancelTimer(token:number)->None:
    """
    Cancels a timer previously started with startTimer. This will stop the timer from firing.

    :param token: The ID of the timer to cancel.
    """
    pass
  @staticmethod
  def setAlarm(time:number)->number:
    """
    Sets an alarm that will fire at the specified in-game time. When it fires, * an alarm event will be added to the event queue with theID * returned from this function as the first parameter.

    Throws:

    * If the time is out of range.

    :param time: The time at which to fire the alarm, in the range [0.0, 24.0).
    :returns: The ID of the new alarm. This can be used to filter the alarm event, or cancel the alarm.
    """
    pass
  @staticmethod
  def cancelAlarm(token:number)->None:
    """
    Cancels an alarm previously started with setAlarm. This will stop the alarm from firing.

    :param token: The ID of the alarm to cancel.
    """
    pass
  @staticmethod
  def shutdown()->None:
    """
    Shuts down the computer immediately.

    """
    pass
  @staticmethod
  def reboot()->None:
    """
    Reboots the computer immediately.

    """
    pass
  @staticmethod
  def getComputerID()->number:
    """
    Returns the ID of the computer.

    :returns: The ID of the computer.
    """
    pass
  @staticmethod
  def computerID()->number:
    """
    Returns the ID of the computer.

    :returns: The ID of the computer.
    """
    pass
  @staticmethod
  def getComputerLabel()->string | None:
    """
    Returns the label of the computer, or nil if none is set.

    :returns: The label of the computer.
    """
    pass
  @staticmethod
  def computerLabel()->string | None:
    """
    Returns the label of the computer, or nil if none is set.

    :returns: The label of the computer.
    """
    pass
  @staticmethod
  def setComputerLabel(label:string=None)->None:
    """
    Set the label of this computer.

    :param label: The new label. May be nil in order to clear it.
    """
    pass
  @staticmethod
  def clock()->number:
    """
    Returns the number of seconds that the computer has been running.

    :returns: The computer's uptime.
    """
    pass
  @staticmethod
  def time(locale:string|table=None)->any:
    """
    Returns the current time depending on the string passed in. This willalways be in the range [0.0, 24.0).

    This function can also be called with a table returned from date,which will convert the date fields into a UNIX timestamp (number ofseconds since 1 January 1970).

    Throws:

    * If an invalid locale is passed.

    :param locale: The locale of the time, or a table filled by os.date("*t") to decode. Defaults to ingame locale if not specified.
    :returns: The hour of the selected locale, or a UNIX timestamp from the table, depending on the argument passed in.
    """
    pass
  @staticmethod
  def day(args:string=None)->number:
    """
    Returns the day depending on the locale specified.

    * If called with ingame, returns the number of days since the world was created. This is the default.
    * If called with utc, returns the number of days since 1 January 1970 in the UTC timezone.
    * If called with local, returns the number of days since 1 January 1970 in the server's local timezone.

    Throws:

    * If an invalid locale is passed.

    :param args: The locale to get the day for. Defaults to ingame if not set.
    :returns: The day depending on the selected locale.
    """
    pass
  @staticmethod
  def epoch(args:string=None)->number:
    """
    Returns the number of milliseconds since an epoch depending on the locale.

    * If called with ingame, returns the number of milliseconds since the world was created. This is the default.
    * If called with utc, returns the number of milliseconds since 1 January 1970 in the UTC timezone.
    * If called with local, returns the number of milliseconds since 1 January 1970 in the server's local timezone.

    Throws:

    * If an invalid locale is passed.

    :param args: The locale to get the milliseconds for. Defaults to ingame if not set.
    :returns: The milliseconds since the epoch depending on the selected locale.
    """
    pass
  @staticmethod
  def date(format:string=None, time:number=None)->string:
    """
    Returns a date string (or table) using a specified format string andoptional time to format.

    The format string takes the same formats as C's strftime function(http://www.cplusplus.com/reference/ctime/strftime/). In extension, itcan be prefixed with an exclamation mark (!) to use UTC timeinstead of the server's local timezone.

    If the format is exactly *t (optionally prefixed with !), atable will be returned instead. This table has fields for the year, month,day, hour, minute, second, day of the week, day of the year, and whetherDaylight Savings Time is in effect. This table can be converted to a UNIXtimestamp (days since 1 January 1970) with date.

    Throws:

    * If an invalid format is passed.

    :param format?: The format of the string to return. This defaults to %c, which expands to a string similar to "Sat Dec 24 16:58:00 2011".
    :param time?: The time to convert to a string. This defaults to the current time.
    :returns: The resulting format string.
    """
    pass