function all(iterable)
    for element in op_in(iterable) do
        if None == element or not element then
            return false
        end
    end
    return true
end

return all