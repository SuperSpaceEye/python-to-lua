function len()  end
require("pylua_init")
local is_pyobj = helper_functions.is_pyobj

local function len(item)
    if not is_pyobj(item) then return #item end
    return item.__len__()
end

return len