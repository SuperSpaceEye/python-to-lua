local is_pyobj = (require "helper_functions").is_pyobj
local function enumerate(t, start)
    start = start or 0

    if t == nil then error("nil object")
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
    elseif is_pyobj(t) then
        local iter = t.__iter__()
        local i = -1
        return function()
            local val = iter.__next__()
            i = i + 1
            if val ~= nil then
                return i + start - 1, val
            else
                return nil
            end
        end
    end
end

return enumerate