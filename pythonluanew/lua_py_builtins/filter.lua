--function filter()  end
--require("pylua_init")

--TODO
function filter(func, iterable)
    if not is_pyobj(iterable) then error("filter can only be used with pyobj") end

    local lis = list()

    if func ~= nil then
        for item in op_in(iterable) do
            if func(item) then
                lis.append(item)
            end
        end
    else
        for item in op_in(iterable) do
            if item ~= nil and item ~= None and item then lis.append(item) end
        end
    end
end

return filter