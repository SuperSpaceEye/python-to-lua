function isinstance()  end
require("pylua_init")
local is_pyobj = helper_functions.is_pyobj

function isinstance(obj, items, no_instance_check)
    no_instance_check = no_instance_check or false

    -- base condition for recursive check
    if items == nil then return false end

    --Both items should be pyobjects
    if not (is_pyobj(obj) and is_pyobj(items)) then error("items should be pyobjects") end

    -- if items is an instance of some pyobject
    if not no_instance_check and items.___is_instance then
        -- if it's not a tuple, then throw error (No unions)
        if not isinstance(items, tuple) then error("TypeError: isinstance() arg 2 must be a type or a tuple of types") end
        -- if any item in tuple is instance then throw error
        for item in op_in(items) do if item.___is_instance then error("TypeError: isinstance() arg 2 must be a type or a tuple of types") end end

        -- if item itself is not an instance
        if not obj.___is_instance then return false end

        -- will recursively check while unpacking tuple until it has a single "type"
        for item in op_in(items) do
            if isinstance(obj, item) then return true end
        end
        return false
    end

    if not no_instance_check and not obj.___is_instance then return false end

    local obj_pytype = pytype(obj)
    -- check if object is a direct instance of type
    if obj_pytype == pytype(items) then return true end

    -- recursively check all base types the object inherited from
    for _, base in ipairs(obj.___bases) do
        if isinstance(base, items, true) then return true end
    end
    return false
end

return isinstance