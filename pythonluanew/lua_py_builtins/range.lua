local function range(from, to, step)
    assert(from ~= nil)

    if to == nil then
        to = from
        from = 0
    end

    step = step or 1

    local i = from

    return function()
        ret = i
        if (step > 0 and i >= to) or (step < 0 and i <= to) then
            return nil
        end

        i = i + step
        return ret
    end
end

return range