function slice() end
require("pylua_init")

function slice(start, stop, step)
    if stop == nil and step == nil then return {0, start, None} end
    stop = stop or None
    step = step or None
    return {start, stop, step}
end

return slice