--function hasattr()  end
--require("pylua_init")

-- TODO
function hasattr(object, name)
    if pcall(getattr(object, name)) then
        return true
    else
        return false
    end
end

return hasattr