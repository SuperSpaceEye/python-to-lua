bytes = {}
require("pylua_init")

bytes = class(function(bytes)
    bytes.___name = "bytearray"

    function bytes.__init__(self, source, encoding, errors)
        error("bytes not implemented")
    end

    return bytes
end, {pyobj})

return bytes