from luatypes import *
class commands:
    @staticmethod
    def exec(command:string)->List[boolean, List[string], number|None]:
        """
        Execute a specific command.
        :param command: The command to execute.
        :returns: 1. boolean Whether the command executed successfully.
                  2. { string... } The output of this command, as a list of lines.
                  3. number | nil The number of "affected" objects, or nil if the command failed. The definition of this varies from command to command.
        """
        pass
    @staticmethod
    def execAsync(command:string)->number:
        """
        Asynchronously execute a command.

        Unlike exec, this will immediately return, instead of waiting for the command to execute. This allows you to run multiple commands at the same time.

        When this command has finished executing, it will queue a task_complete event containing the result of executing this command (what exec would return).

        :param command: The command to execute
        :returns: The "task id". When this command has been executed, it will queue a task_complete event with a matching id.
        """
        pass
    @staticmethod
    def list(*args)->List[string]:
        """
        List all available commands which the computer has permission to execute.
        :param args: The sub-command to complete.
        :returns: A list of all available commands
        """
        pass
    @staticmethod
    def getBlockInfos(minX:number,
                      minY:number,
                      minZ:number,
                      maxX:number,
                      maxY:number,
                      maxZ:number,
                      dimension:string=None)->List[table]:
        """
        Get information about a range of blocks.

        This returns the same information as getBlockInfo, just for multiple blocks at once.

        Blocks are traversed by ascending y level, followed by z and x - the returned table may be indexed using x + z*width + y*depth*depth.

        :param minX: The start x coordinate of the range to query.
        :param minY: The start y coordinate of the range to query.
        :param minZ: The start z coordinate of the range to query.
        :param maxX: The end x coordinate of the range to query.
        :param maxY: The end y coordinate of the range to query.
        :param maxZ: The end z coordinate of the range to query.
        :param dimension: The dimension to query (e.g. "minecraft:overworld"). Defaults to the current dimension.

        .. note::
        Throws
            * If the coordinates are not within the world.
            * If trying to get information about more than 4096 blocks.

        """
        pass
    @staticmethod
    def getBlockInfo(x:number, y:number, z:number, dimension:string=None)->table:
        """
        Get some basic information about a block.

        The returned table contains the current name, metadata and block state (as with turtle.inspect). If there is a tile entity for that block, its NBT will also be returned.

        Throws
            * If the coordinates are not within the world, or are not currently loaded.


        :param x: The x position of the block to query.
        :param y: The y position of the block to query.
        :param z: The z position of the block to query.
        :param dimension: The dimension to query (e.g. "minecraft:overworld"). Defaults to the current dimension
        """
        pass