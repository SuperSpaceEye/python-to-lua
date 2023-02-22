local lua_types = {table="<lua_table>",
                   string="<lua_string>",
                   number="<lua_number>",
                   boolean="<lua_boolean>",
                   CFunction="<lua_CFunction>",
                   userdata="<lua_userdata>"
                }
lua_types["function"] = "<lua_function>"
lua_types["nil"] = "<lua_nil>"

function pytype(obj)
    local str = require "str"
    if not is_pyobj(obj) then return str(lua_types[type(obj)]) end
    return str("<class '"..obj.___name.."'>")
end

return pytype