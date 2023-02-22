function any(iterable)
    for element in op_in(iterable) do
        if None ~= element and element then
            return true
        end
    end
    return false
end
return any