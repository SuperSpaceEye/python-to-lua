complex = {}
require("pylua_init")

complex = class(function(complex)
    complex.___name = "complex"

    function complex.__init__(self)
        error("complex type not implemented")
    end

    return complex
end, {pyobj})

return complex