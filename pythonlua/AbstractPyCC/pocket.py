from luatypes import *

class pocket:
  @staticmethod
  def equipBack()->boolean:
    """
    Search the player's inventory for another upgrade, replacing the existing one with that item if found.

    This inventory search starts from the player's currently selected slot, allowing you to prioritise upgrades.

    :returns: If an item was equipped.
    """
    pass
  @staticmethod
  def unequipBack()->boolean:
    """
    Remove the pocket computer's current upgrade.

    :returns: If the upgrade was unequipped.
    """
    pass
