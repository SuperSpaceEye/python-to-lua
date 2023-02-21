function hash(object) end
require("pylua_init")

function hash(object)
    if not is_pyobj(object) then error("unhashable lua object") end
    if object.__hash__ == nil then error("unhashable object "..pytype(object).___d) end
    return object.___hash__()
end

return hash