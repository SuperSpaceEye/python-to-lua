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

function iterable_unpacker(item, num, result)
    result = result or {}
    num = num or {999999999}
    if not is_pyobj(item) then
        result[#result+1]=item
        num[1]=num[1]-1
    else
        for it in op_in(item) do
            if num[1] > 0 then
                iterable_unpacker(it, num, result)
            else
                result[#result+1]=item
            end
        end
    end
    return table.unpack(result)
end

return iterable_unpacker