None = {}
require("pylua_init")

None = class(function(None)
    None.___name = "NoneType"
    function None.__setattr__(self, key, value) end
    function None.__str__(self) return str("None") end
    function None.__eq__(other) return other.___name == "None" end
    function None.__init__(self) error("None can't have an instance") end

    return None
end, {pyobj})

return None