from .luatypes import *

class shell:
  @staticmethod
  def execute(command:string, *args)->boolean:
    """
    Run a program with the supplied arguments.

    Unlike shell.run, each argument is passed to the program verbatim. Whileshell.run("echo", "b c") runs echo with b and c,shell.execute("echo", "b c") runs echo with a single argument b c.

    :param command: The program to execute.
    :param args: Arguments to this program.
    :returns: Whether the program exited successfully.
    """
    pass
  @staticmethod
  def run(*args)->boolean:
    """
    Run a program with the supplied arguments.

    All arguments are concatenated together and then parsed as a command line. Asa result, shell.run("program a b") is the same as shell.run("program", "a", "b").

    :param args: The program to run and its arguments.
    :returns: Whether the program exited successfully.
    """
    pass
  @staticmethod
  def exit()->None:
    """
    Exit the current shell.

    This does not terminate your program, it simply makes the shell terminateafter your program has finished. If this is the toplevel shell, then thecomputer will be shutdown.

    """
    pass
  @staticmethod
  def dir()->string:
    """
    Return the current working directory. This is what is displayed before the>  of the shell prompt, and is used by shell.resolve to handle relativepaths.

    :returns: The current working directory.
    """
    pass
  @staticmethod
  def setDir(dir:string)->None:
    """
    Set the current working directory.

    Throws:

    * If the path does not exist or is not a directory.

    :param dir: The new working directory.
    """
    pass
  @staticmethod
  def path()->string:
    """
    Set the path where programs are located.

    The path is composed of a list of directory names in a string, each separatedby a colon (:). On normal turtles will look in the current directory (.),/rom/programs and /rom/programs/turtle folder, making the path.:/rom/programs:/rom/programs/turtle.

    :returns: The current shell's path.
    """
    pass
  @staticmethod
  def setPath(path:string)->None:
    """
    Set the current program path.

    Be careful to prefix directories with a /. Otherwise they will be searchedfor from the current directory, rather than the computer's root.

    :param path: The new program path.
    """
    pass
  @staticmethod
  def resolve(path:string)->None:
    """
    Resolve a relative path to an absolute path.

    The fs and io APIs work using absolute paths, and so we must convertany paths relative to the current directory to absolute ones. Thisdoes nothing when the path starts with /.

    :param path: The path to resolve.
    """
    pass
  @staticmethod
  def resolveProgram(command:string)->string | None:
    """
    Resolve a program, using the program path and list of aliases.

    :param command: The name of the program
    :returns: The absolute path to the program, or nil if it could not be found.
    """
    pass
  @staticmethod
  def programs(include_hidden:boolean=None)->table[string]:
    """
    Return a list of all programs on the path.

    :param include_hidden: Include hidden files. Namely, any which start with.
    :returns: A list of available programs.
    """
    pass
  @staticmethod
  def complete(sLine:string)->table[string] | None:
    """
    Complete a shell command line.

    This accepts an incomplete command, and completes the program name orarguments. For instance, l will be completed to ls, and ls ro will becompleted to ls rom/.

    Completion handlers for your program may be registered withshell.setCompletionFunction.

    :param sLine: The input to complete.
    :returns: The list of possible completions.
    """
    pass
  @staticmethod
  def completeProgram(program:string)->table[string]:
    """
    Complete the name of a program.

    :param program: The name of a program to complete.
    :returns: A list of possible completions.
    """
    pass
  @staticmethod
  def setCompletionFunction(program:string, complete)->None:
    """
    Set the completion function for a program. When the program is entered on the command line, this program will be called to provide auto-complete information.

    The completion function accepts four arguments:

    For instance, when completing pastebin put rom/st our pastebin completion function will receive the shell API, an index of 2, rom/st as the current argument, and a "previous" table of { "put" }. This function may then wish to return a table containing artup.lua, indicating the entire command should be completed to pastebin put rom/startup.lua.

    You completion entries may also be followed by a space, if you wish to indicate another argument is expected.

    :param program: The path to the program. This should be an absolute path without the leading /.
    :param complete: function(shell: table, index: number, argument: string, previous: { string }):{ string } | nil The completion function.
    """
    pass
  @staticmethod
  def getCompletionInfo()->any:
    """
    Get a table containing all completion functions.

    This should only be needed when building custom shells. UsesetCompletionFunction to add a completion function.

    :returns: { [string] = { fnComplete = function } } A table mapping the absolute path of programs, to their completion functions.
    """
    pass
  @staticmethod
  def getRunningProgram()->string:
    """
    Returns the path to the currently running program.

    :returns: The absolute path to the running program.
    """
    pass
  @staticmethod
  def setAlias(command:string, program:string)->None:
    """
    Add an alias for a program.

    Alias vim to the edit program

    :param command: The name of the alias to add.
    :param program: The name or path to the program.
    """
    pass
  @staticmethod
  def clearAlias(command:string)->None:
    """
    Remove an alias.

    :param command: The alias name to remove.
    """
    pass
  @staticmethod
  def aliases()->any:
    """
    Get the current aliases for this shell.

    Aliases are used to allow multiple commands to refer to a single program. Forinstance, the list program is aliased to dir or ls. Running ls, diror list in the shell will all run the list program.

    :returns: { [string] = string } A table, where the keys are the names of aliases, and the values are the path to the program.
    """
    pass
  @staticmethod
  def openTab(*args)->None:
    """
    Open a new multishell tab running a command.

    This behaves similarly to shell.run, but instead returns the processindex.

    This function is only available if the multishell API is.

    :param args: string The command line to run.
    """
    pass
  @staticmethod
  def switchTab(id:number)->None:
    """
    Switch to the multishell tab with the given index.

    :param id: The tab to switch to.
    """
    pass