--function getattr()  end
--require("pylua_init")

function getattr(object, name, default)
    if not is_pyobj(object) then error("obj is not pyobject") end
    if pytype(name) ~= pytype(str) and type(name) ~= "string" then error("name should be either a lua str or pystr") end

    if pcall(object.__getattr__(name)) then
        return object.__getattr__(name)
    else
        if default ~= nil or default ~= None then
            return default
        end
        error("No attribute")
    end

    --return object.__getattr__(name)
end