--helper_functions = helper_functions or require("helper_function")
--local is_pyobj = helper_functions.is_pyobj
function sequence_unpacker(iter)
    return function()
        local temp = {}
        local item = iter()

        if item == nil then return nil end

        for item in op_in(item) do
            table.insert(temp, item)
        end
        return table.unpack(temp)
    end
end

return sequence_unpacker