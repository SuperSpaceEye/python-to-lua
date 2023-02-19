local is_pyobj = is_pyobj or (require "helper_functions").is_pyobj

local function len(item)
    if not is_pyobj(item) then return #item end
    return item.__len__()
end

return len