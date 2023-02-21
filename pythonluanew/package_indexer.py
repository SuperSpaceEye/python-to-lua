import pkgutil
import os
from pathlib import Path
import sys

class PackageIndexer:
    def init_data(self, silent=True):
        self.pyfiles = {}
        self.dllfiles = {}

        # self.not_loaded = {}

        for item in pkgutil.iter_modules():
            loader = pkgutil.get_loader(item.name)
            if not hasattr(loader, "get_filename"):
                if not silent:
                    print("FAILED TO LOAD", item.name, loader)
                continue

            path = Path(loader.get_filename())

            if not item.ispkg:
                if path.suffix != ".py":
                    self.dllfiles[item.name] = str(path)
                    continue
                self.pyfiles[item.name] = str(path)
            else:
                for root, dirs, files in os.walk(path.parent):
                    for fitem in files:
                        split = os.path.splitext(fitem)
                        if split[-1] != ".py":
                            # if split[-1] not in self.not_loaded.keys():
                            #     self.not_loaded[split[-1]] = [[fitem, root]]
                            #     continue
                            # self.not_loaded[split[-1]].append([fitem, root])
                            # print(fitem)
                            continue
                        structure = str(Path(root).relative_to(path.parent)).replace("/", ".")
                        # print(structure)

                        if structure == ".":
                            structure = "."
                        else:
                            structure = f".{structure}."

                        self.pyfiles[f"{item.name}{structure}{os.path.splitext(fitem)[0]}"] = f"{root}/{fitem}"
                    pass

        # for key in self.not_loaded.keys():
        #     for item in self.not_loaded[key]:
        #         print(item)

        # for key, value in zip(self.pyfiles.keys(), self.pyfiles.values()):
        #     print(key, value)
    def __init__(self, silent=True):
        if silent:
            with open(os.devnull, "w") as devNull:
                original = sys.stdout
                sys.stdout = devNull
                self.init_data(silent)
                sys.stdout = original
        else:
            self.init_data(silent)