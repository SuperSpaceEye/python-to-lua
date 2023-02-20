local tuple = require "tuple"
local str = require "str"
local list = require "list"
local dict = require "dict"
local pyobj = require "pyobj"
local isinstance = require "isinstance"

a = str("a b  c    d    e      o")

print(a.___d)
print(a.split(nil, 1).__str__().___d)