-- translates key to positive number with bound checking
local function py_calc_key(len, key, give_error)
    give_error = give_error or true
    if key < 0 then
        key = len + key
        if key < 0 then
            if give_error then
                error("IndexError: index out of range")
            else
                key = 0
            end
        end
        return key
    end
    if key >= len then
        if give_error then
            error("IndexError: index out of range")
        else
            key = len-1
        end
    end

    return key
end

-- if key < 0 then calculates real index,
local function calc_key(len, key, give_error)
    return py_calc_key(len, key, give_error)+1
end

local function is_pyobj(o)
    return type(o) == "table" and o.___is_pyobj
end

return {calc_key=calc_key,
        py_calc_key=py_calc_key,
        is_pyobj=is_pyobj}