function del() end
require("pylua_init")
local is_pyobj = helper_functions.is_pyobj

function del(item)
    if not is_pyobj(item) then return end
    item.__del__()
end

return del