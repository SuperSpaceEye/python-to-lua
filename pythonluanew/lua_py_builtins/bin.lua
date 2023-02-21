function bin()  end
require("pylua_init")

local function toBits(num,bits)
    -- returns a table of bits, most significant first.
    bits = bits or math.max(1, select(2, math.frexp(num)))
    local t = {} -- will contain the bits
    for b = bits, 1, -1 do
        t[b] = math.fmod(num, 2)
        num = math.floor((num - t[b]) / 2)
    end


    local str_result = "0b"
    for _, v in ipairs(t) do
        str_result = str_result .. v
    end
    return str(str_result)
end

function bin(item)
    local num = 0

    if is_pyobj(item) then
        num = item.__index__()
    elseif type(item) == "number" then
        num = math.floor(item)
    else
        error("Not a number")
    end
    local prefix = str("")

    if num < 0 then prefix = str("-"); num = math.abs(num) end

    return prefix+toBits(num)
end
return bin