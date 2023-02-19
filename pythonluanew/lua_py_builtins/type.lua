local is_pyobj = (require "helper_functions").is_pyobj
local str = require "str"

local lua_types = {table="<lua_table>",
                   string="<lua_string>",
                   number="<lua_number>",
                   boolean="<lua_boolean>",
                   CFunction="<lua_CFunction>",
                   userdata="<lua_userdata>"
                }
lua_types["function"] = "<lua_function>"
lua_types["nil"] = "<lua_nil>"

local function pytype(obj)
    if not is_pyobj(obj) then return str(lua_types[type(obj)]) end
    return str("<class '"..obj.___name.."'>")
end

return pytype