from luatypes import *

class settings:
  @staticmethod
  def define(name:string, options:table[string, any, string])->None:
    """
    Define a new setting, optional specifying various properties about it.

    While settings do not have to be added before being used, doing so allows you to provide defaults and additional metadata.

    Options for this setting. This table accepts the following fields:
    * description: A description which may be printed when running the set program.
    * default: A default value, which is returned by settings.get if the setting has not been changed.
    * type: Require values to be of this type. Setting the value to another type will error.

    :param name: The name of this option
    :param options: Options for this setting. This table accepts the following fields:
    """
    pass
  @staticmethod
  def undefine(name:string)->None:
    """
    Remove a definition of a setting.

    If a setting has been changed, this does not remove its value. Use settings.unsetfor that.

    :param name: The name of this option
    """
    pass
  @staticmethod
  def set(name:string, value)->None:
    """
    Set the value of a setting.

    Throws:

    *If this value cannot be serialised

    :param name: The name of the setting to set
    :param value: The setting's value. This cannot be nil, and must be serialisable by textutils.serialize.
    """
    pass
  @staticmethod
  def get(name:string, default:any=None)->any:
    """
    Get the value of a setting.

    :param name: The name of the setting to get.
    :param default: The value to use should there be pre-existing value for this setting. If not given, it will use the setting's default value if given, or nil otherwise.
    :returns: The setting's, or the default if the setting has not been changed.
    """
    pass
  @staticmethod
  def getDetails(name:string)->table:
    """
    Get details about a specific setting.

    :param name: The name of the setting to get.
    :returns: { description? = string, default? = any, type? = string, value? = any } Information about this setting. This includes all information from settings.define, as well as this setting's value.
    """
    pass
  @staticmethod
  def unset(name:string)->None:
    """
    Remove the value of a setting, setting it to the default.

    settings.get will return the default value until the setting's value isset, or the computer is rebooted.

    :param name: The name of the setting to unset.
    """
    pass
  @staticmethod
  def clear()->None:
    """
    Resets the value of all settings. Equivalent to calling settings.unset

    @see settings.unset

    """
    pass
  @staticmethod
  def getNames()->table[string]:
    """
    Get the names of all currently defined settings.

    :returns: An alphabetically sorted list of all currently-defined settings.
    """
    pass
  @staticmethod
  def load(sPath:string=None)->boolean:
    """
    Load settings from the given file.

    Existing settings will be merged with any pre-existing ones. Conflicting entries will be overwritten, but any others will be preserved.

    :param sPath: The file to load from, defaulting to .settings.
    :returns: Whether settings were successfully read from this file. Reasons for failure may include the file not existing or being corrupted.
    """
    pass
  @staticmethod
  def save(sPath:string=None)->boolean:
    """
    Save settings to the given file.

    This will entirely overwrite the pre-existing file. Settings defined in thefile, but not currently loaded will be removed.

    :param sPath: The path to save settings to, defaulting to .settings.
    :returns: If the settings were successfully saved.
    """
    pass