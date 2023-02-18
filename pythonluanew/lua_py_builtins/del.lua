local function del(item)
    if item ~= "table" then return end
    if not item.___is_pyobj then return end
    item.__del__()
end

return del