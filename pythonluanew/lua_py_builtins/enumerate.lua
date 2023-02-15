function enumerate(t, start)
    start = start or 0

    if t == nil then

    elseif type(t) == "function" then
        local i, v = start - 1, t()
        return function()
            local index, value = i, v
            i, v = i+1, t()
            if v == nil then
                return nil
            end

            return index + start - 1, value
        end
    elseif t._is_list or t._is_str then
        local data = t
        data = t._data
        local i, v = next(data, nil)
        return function()
            local index, value = i, v
            i, v = next(data, i)

            if index == nil then
                return nil
            end

            return index + start - 1, value
        end
    end
end