from .luatypes import *

class turtle:
  @staticmethod
  def craft(limit:number=64)->boolean|List[boolean, string]:
    """
    Craft a recipe based on the turtle's inventory.

    The turtle's inventory should set up like a crafting grid. For instance, tocraft sticks, slots 1 and 5 should contain planks. All other slots should beempty, including those outside the crafting "grid".

    Throws:

    * When limit is less than 1 or greater than 64.

    :param limit: = 64 The maximum number of crafting steps to run.
    :returns: True If crafting succeeds. Or false if crafting fails and a string describing why
    """
    pass
  @staticmethod
  def forward()->List[boolean, string|None]:
    """
    Move the turtle forward one block.

    :returns: Whether the turtle could successfully move. string | nil The reason the turtle could not move.
    """
    pass
  @staticmethod
  def back()->List[boolean, string|None]:
    """
    Move the turtle backwards one block.

    :returns: Whether the turtle could successfully move. string | nil The reason the turtle could not move.
    """
    pass
  @staticmethod
  def up()->List[boolean, string|None]:
    """
    Move the turtle up one block.

    :returns: Whether the turtle could successfully move. string | nil The reason the turtle could not move.
    """
    pass
  @staticmethod
  def down()->List[boolean, string|None]:
    """
    Move the turtle down one block.

    :returns: Whether the turtle could successfully move. string | nil The reason the turtle could not move.
    """
    pass
  @staticmethod
  def turnLeft()->List[boolean, string|None]:
    """
    Rotate the turtle 90 degrees to the left.

    :returns: Whether the turtle could successfully turn. string | nil The reason the turtle could not turn.
    """
    pass
  @staticmethod
  def turnRight()->List[boolean, string|None]:
    """
    Rotate the turtle 90 degrees to the right.

    :returns: Whether the turtle could successfully turn. string | nil The reason the turtle could not turn.
    """
    pass
  @staticmethod
  def dig(side:string=None)->List[boolean, string|None]:
    """
    Attempt to break the block in front of the turtle.

    This requires a turtle tool capable of breaking the block. Diamond pickaxes(mining turtles) can break any vanilla block, but other tools (such as axes)are more limited.

    :param side: The specific tool to use. Should be "left" or "right".
    :returns: Whether a block was broken. string | nil The reason no block was broken.
    """
    pass
  @staticmethod
  def digUp(side:string=None)->List[boolean, string|None]:
    """
    Attempt to break the block above the turtle. See dig for full details.

    :param side: The specific tool to use.
    :returns: Whether a block was broken. string | nil The reason no block was broken.
    """
    pass
  @staticmethod
  def digDown(side:string=None)->List[boolean, string|None]:
    """
    Attempt to break the block below the turtle. See dig for full details.

    :param side: The specific tool to use.
    :returns: Whether a block was broken. string | nil The reason no block was broken.
    """
    pass
  @staticmethod
  def place(text:string=None)->boolean:
    """
    Place a block or item into the world in front of the turtle.

    "Placing" an item allows it to interact with blocks and entities in front of the turtle. For instance, bucketscan pick up and place down fluids, and wheat can be used to breed cows. However, you cannot use place toperform arbitrary block interactions, such as clicking buttons or flipping levers.

    :param text: When placing a sign, set its contents to this text.
    :returns: Whether the block could be placed. string | nil The reason the block was not placed.
    """
    pass
  @staticmethod
  def placeUp(text:string=None)->boolean:
    """
    Place a block or item into the world above the turtle.

    :param text: When placing a sign, set its contents to this text.
    :returns: Whether the block could be placed. string | nil The reason the block was not placed.
    """
    pass
  @staticmethod
  def placeDown(text:string=None)->boolean:
    """
    Place a block or item into the world below the turtle.

    :param text: When placing a sign, set its contents to this text.
    :returns: Whether the block could be placed. string | nil The reason the block was not placed.
    """
    pass
  @staticmethod
  def drop(count:number=None)->List[boolean, string|None]:
    """
    Drop the currently selected stack into the inventory in front of the turtle, or as an item into the world ifthere is no inventory.

    If dropping an invalid number of items.

    :param count: The number of items to drop. If not given, the entire stack will be dropped.
    :returns: Whether items were dropped. string | nil The reason the no items were dropped.
    """
    pass
  @staticmethod
  def dropUp(count:number=None)->List[boolean, string|None]:
    """
    Drop the currently selected stack into the inventory above the turtle, or as an item into the world if there isno inventory.

    If dropping an invalid number of items.

    :param count: The number of items to drop. If not given, the entire stack will be dropped.
    :returns: Whether items were dropped. string | nil The reason the no items were dropped.
    """
    pass
  @staticmethod
  def dropDown(count:number=None)->List[boolean, string|None]:
    """
    Drop the currently selected stack into the inventory in front of the turtle, or as an item into the world ifthere is no inventory.

    If dropping an invalid number of items.

    :param count: The number of items to drop. If not given, the entire stack will be dropped.
    :returns: Whether items were dropped. string | nil The reason the no items were dropped.
    """
    pass
  @staticmethod
  def select(slot:number)->boolean:
    """
    Change the currently selected slot.

    The selected slot is determines what slot actions like drop or getItemCount act on.

    Throws:

    * If the slot is out of range.

    :param slot: The slot to select.
    :returns: True When the slot has been selected.
    """
    pass
  @staticmethod
  def getItemCount(slot:number=None)->number:
    """
    Get the number of items in the given slot.

    Throws:

    * If the slot is out of range.

    :param slot: The slot we wish to check. Defaults to the selected slot.
    :returns: The  of items in this slot.
    """
    pass
  @staticmethod
  def getItemSpace(slot:number=None)->number:
    """
    Get the remaining number of items which may be stored in this stack.

    For instance, if a slot contains 13 blocks of dirt, it has room for another 51.

    Throws:

    * If the slot is out of range.

    :param slot: The slot we wish to check. Defaults to the selected slot.
    :returns: The space left in this slot.
    """
    pass
  @staticmethod
  def detect()->boolean:
    """
    Check if there is a solid block in front of the turtle. In this case, solid refers to any non-air or liquidblock.

    :returns: If there is a solid block in front.
    """
    pass
  @staticmethod
  def detectUp()->boolean:
    """
    Check if there is a solid block above the turtle. In this case, solid refers to any non-air or liquid block.

    :returns: If there is a solid block in front.
    """
    pass
  @staticmethod
  def detectDown()->boolean:
    """
    Check if there is a solid block below the turtle. In this case, solid refers to any non-air or liquid block.

    :returns: If there is a solid block in front.
    """
    pass
  @staticmethod
  def compare()->boolean:
    """
    Check if the block in front of the turtle is equal to the item in the currently selected slot.

    :returns: If the block and item are equal.
    """
    pass
  @staticmethod
  def compareUp()->boolean:
    """
    Check if the block above the turtle is equal to the item in the currently selected slot.

    :returns: If the block and item are equal.
    """
    pass
  @staticmethod
  def compareDown()->boolean:
    """
    Check if the block below the turtle is equal to the item in the currently selected slot.

    :returns: If the block and item are equal.
    """
    pass
  @staticmethod
  def attack(side:string=None)->List[boolean, string|None]:
    """
    Attack the entity in front of the turtle.

    :param side: The specific tool to use.
    :returns: Whether an entity was attacked. string | nil The reason nothing was attacked.
    """
    pass
  @staticmethod
  def attackUp(side:string)->List[boolean, string|None]:
    """
    Attack the entity above the turtle.

    :param side: The specific tool to use.
    :returns: Whether an entity was attacked. string | nil The reason nothing was attacked.
    """
    pass
  @staticmethod
  def attackDown(side:string)->List[boolean, string|None]:
    """
    Attack the entity below the turtle.

    :param side: The specific tool to use.
    :returns: Whether an entity was attacked. string | nil The reason nothing was attacked.
    """
    pass
  @staticmethod
  def suck(count:number=None)->List[boolean, string|None]:
    """
    Suck an item from the inventory in front of the turtle, or from an item floating in the world.

    This will pull items into the first acceptable slot, starting at the currently selected one.

    Throws:

    * If given an invalid number of items.

    :param count: The number of items to suck. If not given, up to a stack of items will be picked up.
    :returns: Whether items were picked up. string | nil The reason the no items were picked up.
    """
    pass
  @staticmethod
  def suckUp(count:number=None)->List[boolean, string|None]:
    """
    Suck an item from the inventory above the turtle, or from an item floating in the world.

    Throws:

    * If given an invalid number of items.

    :param count: The number of items to suck. If not given, up to a stack of items will be picked up.
    :returns: Whether items were picked up. string | nil The reason the no items were picked up.
    """
    pass
  @staticmethod
  def suckDown(count:number=None)->List[boolean, string|None]:
    """
    Suck an item from the inventory below the turtle, or from an item floating in the world.

    Throws:

    * If given an invalid number of items.

    :param count: The number of items to suck. If not given, up to a stack of items will be picked up.
    :returns: Whether items were picked up. string | nil The reason the no items were picked up.
    """
    pass
  @staticmethod
  def getFuelLevel()->number:
    """
    Get the maximum amount of fuel this turtle currently holds.

    :returns: The current amount of fuel a turtle this turtle has. OR "unlimited" If turtles do not consume fuel when moving.
    """
    pass
  @staticmethod
  def refuel(count:number=None)->boolean|List[boolean, string]:
    """
    Refuel this turtle.

    While most actions a turtle can perform (such as digging or placing blocks) are free, moving consumes fuel fromthe turtle's internal buffer. If a turtle has no fuel, it will not move.

    refuel refuels the turtle, consuming fuel items (such as coal or lava buckets) from the currentlyselected slot and converting them into energy. This finishes once the turtle is fully refuelled or all items havebeen consumed.

    Throws:

    * If the refuel count is out of range.

    :param count: The maximum number of items to consume. One can pass 0 to check if an item is combustable or not.
    :returns: If the turtle was refuelled.
    """
    pass
  @staticmethod
  def compareTo(slot:number)->boolean:
    """
    Compare the item in the currently selected slot to the item in another slot.

    If the slot is out of range.

    :param slot: The slot to compare to.
    :returns: If the two items are equal.
    """
    pass
  @staticmethod
  def transferTo(slot:number, count:number=None)->boolean:
    """
    Move an item from the selected slot to another one.

    Throws:

    * If the slot is out of range.
    * If the number of items is out of range.

    :param slot: The slot to move this item to.
    :param count: The maximum number of items to move.
    :returns: If some items were successfully moved.
    """
    pass
  @staticmethod
  def getSelectedSlot()->number:
    """
    Get the currently selected slot.

    :returns: The current slot.
    """
    pass
  @staticmethod
  def getFuelLimit()->number:
    """
    Get the maximum amount of fuel this turtle can hold.

    By default, normal turtles have a limit of 20,000 and advanced turtles of 100,000.

    :returns: The maximum amount of fuel a turtle can hold. OR "unlimited" If turtles do not consume fuel when moving.
    """
    pass
  @staticmethod
  def equipLeft()->boolean|List[boolean, string]:
    """
    Equip (or unequip) an item on the left side of this turtle.

    This finds the item in the currently selected slot and attempts to equip it to the left side of the turtle. Theprevious upgrade is removed and placed into the turtle's inventory. If there is no item in the slot, the previousupgrade is removed, but no new one is equipped.

    :returns: If the item was equipped. OR false If we could not equip the item. string The reason equipping this item failed.
    """
    pass
  @staticmethod
  def equipRight()->boolean|List[boolean, string]:
    """
    Equip (or unequip) an item on the right side of this turtle.

    This finds the item in the currently selected slot and attempts to equip it to the right side of the turtle. Theprevious upgrade is removed and placed into the turtle's inventory. If there is no item in the slot, the previousupgrade is removed, but no new one is equipped.

    :returns: If the item was equipped. OR false If we could not equip the item. string The reason equipping this item failed.
    """
    pass
  @staticmethod
  def inspect()->List[boolean, table|string]:
    """
    Get information about the block in front of the turtle.

    :returns: Whether there is a block in front of the turtle. table | string Information about the block in front, or a message explaining that there is no block.
    """
    pass
  @staticmethod
  def inspectUp()->List[boolean, table|string]:
    """
    Get information about the block above the turtle.

    :returns: Whether there is a block above the turtle. table | string Information about the block above, or a message explaining that there is no block.
    """
    pass
  @staticmethod
  def inspectDown()->List[boolean, table|string]:
    """
    Get information about the block below the turtle.

    :returns: Whether there is a block below the turtle. table | string Information about the block below, or a message explaining that there is no block.
    """
    pass
  @staticmethod
  def getItemDetail(slot:number=None , detailed:boolean=None)->None | table:
    """
    Get detailed information about the items in the given slot.

    Throws:

    * If the slot is out of range.

    :param slot: The slot to get information about. Defaults to the selected slot.
    :param detailed: Whether to include "detailed" information. When true the method will contain much more information about the item at the cost of taking longer to run.
    :returns: Information about the given slot, or nil if it is empty.
    """
    pass
  @staticmethod
  def native()->None:
    """
    Historically this table behaved differently to the main turtle API, but this is no longer the case. Youshould not need to use it.

    The builtin turtle API, without any generated helper functions.

    """
    pass