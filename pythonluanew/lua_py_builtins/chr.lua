function chr()  end
require("pylua_init")

function chr(i)
    if is_pyobj(i) then
        i = i.__index__()
    end
    if type(i) ~= "number" then
        error("should be a number")
    end

    i = math.floor(i)

    return string.char(i)
end

return chr