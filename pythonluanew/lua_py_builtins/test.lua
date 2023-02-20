local tuple = require "tuple"
local str = require "str"
local list = require "list"
local dict = require "dict"
local pyobj = require "pyobj"
local isinstance = require "isinstance"

a = tuple({1, 2, 3, 4, 5}, false)
--b = list({1, 2, 3, 4, 5})
--
--print("deb",a[0])
print(a.__str__().___d)

b = str("ababac")
print(b.__contains__("abac"))
--print(b.__str__().___d)