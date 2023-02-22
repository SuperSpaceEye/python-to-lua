#!/usr/bin/env python3
"""The main entry point to the translator"""
from argparse import ArgumentParser
from pathlib import Path
import sys

from pythonluanew.config import Config
from pythonluanew.translator import Translator
from pythonluanew.construct import construct

def create_arg_parser():
    """Create and initialize an argument parser object"""
    parser = ArgumentParser(description="Python to lua translator.")
    parser.add_argument("inputfilename", metavar="IF", type=str,
                        help="A python script filename to translate it.",
                        nargs="?", default="")
    parser.add_argument("configfilename", metavar="CONFIG", type=str,
                        help="Translator configuration file in yaml format.",
                        nargs="?", default=".pyluaconf.yaml")
    parser.add_argument("--minify-lua", help="Minify lua code.",
                        dest="minify_lua", action="store_true")
    parser.add_argument("--no-jumps", help="Compiler will not use goto labels during compilation",
                        dest="no_jumps", action="store_true")
    parser.add_argument("--break-in-do", help="Compiler will wrap break statements in \"do end\"",
                        dest="break_in_do", action="store_true")

    return parser


def main():
    """Entry point function to the translator"""
    parser = create_arg_parser()
    argv = parser.parse_args()

    input_filename = argv.inputfilename
    if not Path(input_filename).is_file():
        raise RuntimeError(
            "The given filename ('{}') is not a file.".format(input_filename))

    translator = Translator(Config(argv.configfilename,
                                   argv.no_jumps,
                                   break_in_do=argv.break_in_do,
                                   minify_lua=argv.minify_lua))

    construct(input_filename, f"lua/{Path(input_filename).name.split('.')[0]}", translator, argv.minify_lua)
    return 0


if __name__ == "__main__":
    sys.exit(main())
