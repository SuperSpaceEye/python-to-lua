function divmod(a, b)
    if is_pyobj(a) and is_pyobj(b) then error("Not implemented") end
    return math.floor(a/b), a % b
end

return divmod