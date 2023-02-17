function range_in(iter)
    local iter = iter.__iter__()
    return function()
        return iter.__next__()
    end
end

function operator_in(item, items)
    if items == nil then
        return range_in(item)
    else
        if (item.___is_pyobj and items.___is_pyobj) == false then
            error("Objects are not pyobj") end
        return items.__contains__(item)
    end
end

return operator_in