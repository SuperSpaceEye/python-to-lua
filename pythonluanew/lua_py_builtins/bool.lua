--function bool() end
--require("pylua_init")

helper_functions = helper_functions or require("helper_functions")
local is_pyobj = helper_functions.is_pyobj

function bool(x)
    if x == false or x == nil or x == 0 or x == None then
        return false
    end

    if is_pyobj(x) then
        if x.__bool__ ~= nil then
            return x.__bool__()
        end

        if x.__len__ ~= nil then
            return bool(x.__len__())
        end
        error("pyobj should have either __bool__ or __len__ implemented")
    end

    return true
end
return bool