function all(iterable)
    for element in iterable do
        if not element then
            return false
        end
    end
    return true
end

return all