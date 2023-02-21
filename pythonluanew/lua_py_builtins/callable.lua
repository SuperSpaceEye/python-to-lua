function callable()  end
require("pylua_init")

function callable(obj)
    if not is_pyobj(obj) then error("Not a pyobject") end

    if not obj.___is_instance then return true end
    return obj.__call__ ~= nil
end

return callable