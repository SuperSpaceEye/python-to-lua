--function abs()  end
--require("pylua_init")

helper_functions = helper_functions or require("helper_functions")
local is_pyobj = helper_functions.is_pyobj

function abs(item)
    if not is_pyobj(item) then
        if type(item) == "number" then return math.abs(item) end
    end
    return item.__abs__()
end

return abs