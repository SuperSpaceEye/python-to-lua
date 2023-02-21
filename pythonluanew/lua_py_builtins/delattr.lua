function delattr()  end
require("pylua_init")

function delattr(obj, name)
    if not is_pyobj(obj) then error("obj is not pyobject") end
    if not obj.___is_instance then error("obj is not an instance") end
    if type(name) ~= "string" or pytype(name) ~= pytype(str) then error("name should be either a lua str or pystr") end

    obj.__delattr__(str(name))
end

return delattr