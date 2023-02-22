from .luatypes import *

class disk:
  @staticmethod
  def isPresent(name: string) -> boolean:
    """
    Checks whether any item at all is in the disk drive
    :param name: The name of the disk drive.
    :returns: If something is in the disk drive.
    """
    pass

  @staticmethod
  def getLabel(name: string) -> string | None:
    """
    Get the label of the floppy disk, record, or other media within the givendisk drive.
    If there is a computer or turtle within the drive, this will set the label asread by os.getComputerLabel.
    :param name: The name of the disk drive.
    :returns: The name of the current media, or nil if the drive is not present or empty.
    """
    pass

  @staticmethod
  def setLabel(name: string, label: string = None) -> None:
    """
    Set the label of the floppy disk or other media
    :param name: The name of the disk drive.
    :param label: The new label of the disk
    """
    pass

  @staticmethod
  def hasData(name: string) -> boolean:
    """
    Check whether the current disk provides a mount.
    This will return true for disks and computers, but not records.
    :param name: The name of the disk drive.
    :returns: If the disk is present and provides a mount.
    """
    pass

  @staticmethod
  def getMountPath(name: string) -> string | None:
    """
    Find the directory name on the local computer where the contents of thecurrent floppy disk (or other mount) can be found.
    :param name: The name of the disk drive.
    :returns: The mount's directory, or nil if the drive does not contain a floppy or computer.
    """
    pass

  @staticmethod
  def hasAudio(name: string) -> boolean:
    """
    Whether the current disk is a music disk as opposed to a floppy diskor other item.
    If this returns true, you will can play the record.
    :param name: The name of the disk drive.
    :returns: If the disk is present and has audio saved on it.
    """
    pass

  @staticmethod
  def getAudioTitle(name: string) -> string | False | None:
    """
    Get the title of the audio track from the music record in the drive.
    This generally returns the same as disk.getLabel for records.
    :param name: The name of the disk drive.
    :returns: The track title, false if there is not a music record in the drive or nil if no drive is present.
    """
    pass

  @staticmethod
  def playAudio(name: string) -> None:
    """
    Starts playing the music record in the drive.
    If any record is already playing on any disk drive, it stops before thetarget drive starts playing. The record stops when it reaches the end of thetrack, when it is removed from the drive, when disk.stopAudio is called, orwhen another record is started.
    :param name: The name of the disk drive.
    """
    pass

  @staticmethod
  def stopAudio(name: string) -> None:
    """
    Stops the music record in the drive from playing, if it was started withdisk.playAudio.
    :param name: The name o the disk drive.
    """
    pass

  @staticmethod
  def eject(name: string) -> None:
    """
    Ejects any item currently in the drive, spilling it into the world as a loose item.
    :param name: The name of the disk drive.
    """
    pass

  @staticmethod
  def getID(name: string) -> string | None:
    """
    Returns a number which uniquely identifies the disk in the drive.
    Note, unlike disk.getLabel, this does not return anything for other media,such as computers or turtles.
    :param name: The name of the disk drive.
    :returns: The disk ID, or nil if the drive does not contain a floppy disk.
    """
    pass