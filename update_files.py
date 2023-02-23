core = "wget https://raw.githubusercontent.com/SuperSpaceEye/python-to-lua/master/pythonluanew/lua_py_builtins/"

import os

code = ""

code += "shell.run(\"rm pylua\")"

for root, dirs, files in os.walk("pythonluanew/lua_py_builtins"):
    for file in files:
        code += f"shell.run(\"{core+file} pylua/{file}\")\n"

with open("update_files.lua", mode="w") as file:
    file.write(code)
# print(code)