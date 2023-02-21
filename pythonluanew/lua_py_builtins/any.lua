function any(iterable)
    for element in iterable do
        if element then
            return true
        end
    end
    return false
end
return any