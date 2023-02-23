import js2py
from js2py import require

with open("luamin_/luamin.js", mode="r") as file:
    jscript = file.read()

# print(jscript)

context = js2py.EvalJs(enable_require=True)
context.execute(jscript)

# print(js2py.translate_js(jscript))

# f = js2py.require("luamin")

# print(f["minify"])
# print(str(f))

# with open("lua/test3.lua", mode="r") as file:
#     unminified = file.read()

unminified = \
"""
a = {1, 2, 3, 4}
x = (a or b)[1]
x = a[1]
b = 10 
cc = 20
a = b + cc;
(print or io.write)('done')"""

print(unminified)
print("\n======MINIFIED======\n")

minified = context.luamin.minify(unminified)

print(minified)
#
# print(minified)