local function range_in(iter)
    local iter = iter.__iter__(iter)
    return function()
        return iter.__next__(iter)
    end
end

function op_in(item, items)
    if items == nil then
        return range_in(item)
    else
        if (item.___is_pyobj and items.___is_pyobj) == false then
            error("Objects are not pyobj") end
        return items.__contains__(item)
    end
end

return op_in