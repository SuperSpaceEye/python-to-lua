bytearray = {}
--require("pylua_init")

class = class or require("class")
pyobj = pyobj or require("pyobj")

bytearray = class(function(bytearray)
    bytearray.___name = "bytearray"

    function bytearray.__init__(self, source, encoding, errors)
        error("bytearray not implemented")
    end

    return bytearray
end, {pyobj})

return bytearray