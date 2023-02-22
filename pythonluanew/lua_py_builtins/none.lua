None = {}
--require("pylua_init")
helper_functions = helper_functions or require("helper_functions")
class = class or require("class")
pyobj = pyobj or require("pyobj")
local is_pyobj = helper_functions.is_pyobj

None = class(function(None)
    None.___name = "NoneType"
    function None.__setattr__(self, key, value) end
    function None.__str__(self) return str("None") end
    function None.__eq__(other)
        if not is_pyobj(other) then return false end
        return other.___name == "None"
    end
    function None.__init__(self) error("None can't have an instance") end

    return None
end, {pyobj})

return None