float = {}
require("pylua_init")

float = class(function(float)
    float.___name = "float"

    function float.__init__(self)
        error("Not implemented")
    end

    return float
end, {pyobj})

return float