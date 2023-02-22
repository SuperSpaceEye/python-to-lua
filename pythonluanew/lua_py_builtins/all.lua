--function all() end
--require("pylua_init")

function all(iterable)
    for element in op_in(iterable) do
        if None == element or not element then
            return false
        end
    end
    return true
end

return all