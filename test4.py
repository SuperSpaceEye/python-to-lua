import js2py
from js2py import require

with open("luamin/luamin.js", mode="r") as file:
    jscript = file.read()

# print(jscript)

context = js2py.EvalJs(enable_require=True)
context.execute(jscript)

# print(js2py.translate_js(jscript))

# f = js2py.require("luamin")

# print(f["minify"])
# print(str(f))

with open("lua/test3.lua", mode="r") as file:
    unminified = file.read()

minified = context.luamin.minify(unminified)
#
# print(minified)