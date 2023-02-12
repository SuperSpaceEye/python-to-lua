from luatypes import *

class fs:
  @staticmethod
  def complete(*args) -> None:
    """
    Provides completion for a file or directory name, suitable for use with_G.read.
    When a directory is a possible candidate for completion, two entries areincluded - one with a trailing slash (indicating that entries within thisdirectory exist) and one without it (meaning this entry is an immediatecompletion candidate). include_dirs can be set to false to only include those with a trailing slash.
    https://tweaked.cc/module/fs.html#v:complete
    """
    pass

  @staticmethod
  def isDriveRoot(path: string) -> boolean:
    """
    Returns true if a path is mounted to the parent filesystem.
    The root filesystem "/" is considered a mount, along with disk folders andthe rom folder. Other programs (such as network shares) can exstend this tomake other mount types by correctly assigning their return value for getDrive.
    If the path does not exist.
    :param path: The path to check.
    :returns: If the path is mounted, rather than a normal file/folder.
    """
    pass

  @staticmethod
  def list(path: string) -> table[string]:
    """
    Returns a list of files in a directory.
    If the path doesn't exist.
    List all files under /rom/
    :param path: The path to list.
    :returns: A table with a list of files in the directory.
    """
    pass

  @staticmethod
  def combine(path: string, *args: string) -> string:
    """
    Combines several parts of a path into one full path, adding separators asneeded.
    On argument errors.
    Combine several file paths together
    :param path: The first part of the path. For example, a parent directory path.
    :param *args: Additional parts of the path to combine.
    :returns: The new path, with separators added between parts as needed.
    """
    pass

  @staticmethod
  def getName(path: string) -> string:
    """
    Returns the file name portion of a path.
    Get the file name of rom/startup.lua
    :param path: The path to get the name from.
    :returns: The final part of the path (the file name).
    """
    pass

  @staticmethod
  def getDir(path: string) -> string:
    """
    Returns the parent directory portion of a path.
    Get the directory name of rom/startup.lua
    :param path: The path to get the directory from.
    :returns: The path with the final part removed (the parent directory).
    """
    pass

  @staticmethod
  def getSize(path: string) -> number:
    """
    Returns the size of the specified file.
    If the path doesn't exist.
    :param path: The file to get the file size of.
    :returns: The size of the file, in bytes.
    """
    pass

  @staticmethod
  def exists(path: string) -> boolean:
    """
    Returns whether the specified path exists.
    :param path: The path to check the existence of.
    :returns: Whether the path exists.
    """
    pass

  @staticmethod
  def isDir(path: string) -> boolean:
    """
    Returns whether the specified path is a directory.
    :param path: The path to check.
    :returns: Whether the path is a directory.
    """
    pass

  @staticmethod
  def isReadOnly(path: string) -> boolean:
    """
    Returns whether a path is read-only.
    :param path: The path to check.
    :returns: Whether the path cannot be written to.
    """
    pass

  @staticmethod
  def makeDir(path: string) -> None:
    """
    Creates a directory, and any missing parents, at the specified path.
    If the directory couldn't be created.
    :param path: The path to the directory to create.
    """
    pass

  @staticmethod
  def move(path: string, dest: string) -> None:
    """
    Moves a file or directory from one path to another.
    Any parent directories are created as needed.
    If the file or directory couldn't be moved.
    :param path: The current file or directory to move from.
    :param dest: The destination path for the file or directory.
    """
    pass

  @staticmethod
  def copy(path: string, dest: string) -> None:
    """
    Copies a file or directory to a new path.
    Any parent directories are created as needed.
    If the file or directory couldn't be copied.
    :param path: The file or directory to copy.
    :param dest: The path to the destination file or directory.
    """
    pass

  @staticmethod
  def delete(path: string) -> None:
    """
    Deletes a file or directory.
    If the path points to a directory, all of the enclosed files andsubdirectories are also deleted.
    If the file or directory couldn't be deleted.
    :param path: The path to the file or directory to delete.
    """
    pass

  @staticmethod
  def open(path: string, mode: string) -> table:
    """
    Opens a file for reading or writing at a path.
    The mode string can be any of the following:
    The mode may also have a "b" at the end, which opens the file in "binarymode". This allows you to read binary files, as well as seek within a file.
    If an invalid mode was specified.
    Read the contents of a file.
    Open a file and read all lines into a table. io.lines offers an alternative way to do this.
    Open a file and write some text to it. You can run edit out.txt to see the written text.
    :param path: The path to the file to open.
    :param mode: The mode to open the file with.
    :returns: A file handle object for the file.
    """
    pass

  @staticmethod
  def getDrive(path: string) -> string | None:
    """
    Returns the name of the mount that the specified path is located on.
    If the path doesn't exist.
    Print the drives of a couple of mounts:
    :param path: The path to get the drive of.
    :returns: The name of the drive that the file is on; e.g. hdd for local files, or rom for ROM files.
    """
    pass

  @staticmethod
  def getFreeSpace(path: string) -> number | string:
    """
    Returns the amount of free space available on the drive the path islocated on.
    If the path doesn't exist.
    :param path: The path to check the free space for.
    :returns: The amount of free space available, in bytes, or "unlimited".
    """
    pass

  @staticmethod
  def find(path: string) -> table[string]:
    """
    Searches for files matching a string with wildcards.
    This string is formatted like a normal path string, but can include anynumber of wildcards (*) to look for files matching anything.For example, rom/*/command* will look for any path starting withcommand inside any subdirectory of /rom.
    If the path doesn't exist.
    :param path: The wildcard-qualified path to search for.
    :returns: A list of paths that match the search string.
    """
    pass

  @staticmethod
  def getCapacity(path: string) -> number | None:
    """
    Returns the capacity of the drive the path is located on.
    If the capacity cannot be determined.
    :param path: The path of the drive to get.
    :returns: This drive's capacity. This will be nil for "read-only" drives, such as the ROM or treasure disks.
    """
    pass

  @staticmethod
  def attributes(path: string) -> table:
    """
    Get attributes about a specific file or folder.
    The returned attributes table contains information about the size of the file, whether it is a directory,when it was created and last modified, and whether it is read only.
    The creation and modification times are given as the number of milliseconds since the UNIX epoch. This may begiven to os.date in order to convert it to more usable form.
    If the path does not exist.
    :param path: The path to get attributes for.
    :returns: { size = number, isDir = boolean, isReadOnly = boolean, created = number, modified = number } The resulting attributes.
    """
    pass


class BinaryReadHandle:
  @staticmethod
  def read(count=1) -> None:
    """
    Read a number of bytes from this file.
    When trying to read a negative number of bytes.
    If the file has been closed.
    :param count?: The number of bytes to read. When absent, a single byte will be read as a number. This
  may be 0 to determine we are at the end of the file.
    :returns: If we are at the end of the file.
    """
    pass

  @staticmethod
  def readAll() -> string | None:
    """
    Read the remainder of the file.
    If the file has been closed.
    :returns: The remaining contents of the file, or nil if we are at the end.
    """
    pass

  @staticmethod
  def readLine(withTrailing: boolean = False) -> string | None:
    """
    Read a line from the file.
    If the file has been closed.
    :param withTrailing?: Whether to include the newline characters with the returned string. Defaults to false.
    :returns: The read line or nil if at the end of the file.
    """
    pass

  @staticmethod
  def seek(whence: string = None, offset: number = None) -> number:
    """
    Seek to a new position within the file, changing where bytes are written to. The new position is an offsetgiven by offset, relative to a start position determined by whence:
    In case of success, seek returns the new file position from the beginning of the file.
    If the file has been closed.
    https://tweaked.cc/module/fs.html#v:getFreeSpace
    If failed then returns nil and string
    :param whence?: Where the offset is relative to.
    :param offset?: The offset to seek to.
    :returns: The new position.
    """
    pass

  @staticmethod
  def close() -> None:
    """
    Close this file, freeing any resources it uses.
    Once a file is closed it may no longer be read or written to.
    If the file has already been closed.
    """
    pass


class ReadHandle:
  @staticmethod
  def readLine(withTrailing: boolean = False) -> string | None:
    """
    Read a line from the file.
    If the file has been closed.
    :param withTrailing?: Whether to include the newline characters with the returned string. Defaults to false.
    :returns: The read line or nil if at the end of the file.
    """
    pass

  @staticmethod
  def readAll() -> None | string:
    """
    Read the remainder of the file.
    If the file has been closed.
    :returns: The remaining contents of the file, or nil if we are at the end.
    """
    pass

  @staticmethod
  def read(count: number = 1) -> string | None:
    """
    Read a number of characters from this file.
    When trying to read a negative number of characters.
    If the file has been closed.
    :param count?: The number of characters to read, defaulting to 1.
    :returns: The read characters, or nil if at the of the file.
    """
    pass

  @staticmethod
  def close() -> None:
    """
    Close this file, freeing any resources it uses.
    Once a file is closed it may no longer be read or written to.
    If the file has already been closed.
    """
    pass


class WriteHandle:
  @staticmethod
  def write(value) -> None:
    """
    Write a string of characters to the file.
    If the file has been closed.
    """
    pass

  @staticmethod
  def writeLine(value) -> None:
    """
    Write a string of characters to the file, following them with a new line character.
    If the file has been closed.
    """
    pass

  @staticmethod
  def flush() -> None:
    """
    Save the current file without closing it.
    If the file has been closed.
    """
    pass

  @staticmethod
  def close() -> None:
    """
    Close this file, freeing any resources it uses.
    Once a file is closed it may no longer be read or written to.
    If the file has already been closed.
    """
    pass


class BinaryWriteHandle:
  @staticmethod
  def write(*args) -> None:
    """
    Write a string or byte to the file.
    If the file has been closed.
    :param charcode: The byte to write.
    :param contents: The string to write.
    """
    pass

  @staticmethod
  def flush() -> None:
    """
    Save the current file without closing it.
    If the file has been closed.
    """
    pass

  @staticmethod
  def seek(whence: string = None, offset: number = None) -> number:
    """
    Seek to a new position within the file, changing where bytes are written to. The new position is an offsetgiven by offset, relative to a start position determined by whence:
    In case of success, seek returns the new file position from the beginning of the file.
    If the file has been closed.
    :param whence?: Where the offset is relative to.
    :param offset?: The offset to seek to.
    :returns: The new position.
    """
    pass

  @staticmethod
  def close() -> None:
    """
    Close this file, freeing any resources it uses.
    Once a file is closed it may no longer be read or written to.
    If the file has already been closed.
    """
    pass

