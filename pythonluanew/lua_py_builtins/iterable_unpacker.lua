helper_functions = helper_functions or require("helper_function")
local is_pyobj = helper_functions.is_pyobj
function iterable_unpacker(iter)
    return function()
        local temp = {}
        local item = iter()

        if item == nil then return nil end

        if not is_pyobj(item) then return table.unpack(item) end

        for item in op_in(item) do
            table.insert(temp, item)
        end
        return table.unpack(temp)
    end
end

return iterable_unpacker