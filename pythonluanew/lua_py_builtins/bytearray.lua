bytearray = {}
require("pylua_init")

bytearray = class(function(bytearray)
    bytearray.___name = "bytearray"

    function bytearray.__init__(self, source, encoding, errors)
        error("bytearray not implemented")
    end

    return bytearray
end, {pyobj})

return bytearray