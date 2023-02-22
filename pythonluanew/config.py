"""Python to lua translator config class"""
import sys
import yaml

class Config:
    """Translator config."""
    def __init__(self,
                 filename=None,
                 no_jumps=True,
                 core_pathname="pythonlua.AbstractPyCC.CCT",
                 core_prefix="cc",
                 break_in_do=True,
                 minify_lua=True,
                 src_filename=""):
        self.data = {
            "class": {
                "return_at_the_end": False,
            },
        }
        self.no_jumps = no_jumps
        self.core_pathname = core_pathname
        self.core_prefix = core_prefix
        self.break_in_do = break_in_do
        self.minify_lua = minify_lua
        self.src_filename = src_filename

        if filename is not None:
            self.load(filename)

    def load(self, filename):
        """Load config from the file"""
        try:
            with open(filename, "r") as stream:
                data = yaml.load(stream)
                self.data.update(data)
        except FileNotFoundError:
            pass # Use a default config if the file not found
        except yaml.YAMLError as ex:
            print(ex)

    def __getitem__(self, key):
        """Get data values"""
        return self.data[key]
