dir = function()  end
require("pylua_init")

--TODO complete dir
function dir(obj)
    if obj == nil then
        error("viewing list of object of current local scope is not implemented")
    end

    if obj.__dir__ ~= nil then
        return obj.__dir__()
    end
    local ret_list = list()

    for k, v in pairs(obj) do
        ret_list.append(str(k))
    end

    return ret_list
end

return dir