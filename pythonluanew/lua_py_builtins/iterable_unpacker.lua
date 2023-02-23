helper_functions = helper_functions or require("helper_function")
local is_pyobj = helper_functions.is_pyobj

--function flatten( item, result )
--    local result = result or {}  --  create empty table, if none given during initialization
--    if type( item ) == 'table' then
--        for k, v in pairs( item ) do
--            flatten( v, result )
--        end
--    else
--        result[ #result +1 ] = item
--    end
--    return result
--end

function iterable_unpacker(item, result)
    result = result or {}
    if not is_pyobj(item) then
        result[#result+1]=item
    else
        for it in op_in(item) do
            iterable_unpacker(it, result)
        end
    end
    return table.unpack(result)
end

return iterable_unpacker