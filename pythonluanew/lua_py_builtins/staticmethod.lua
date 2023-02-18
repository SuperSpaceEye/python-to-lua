function staticmethod(fun)
    local wrapper = {
        is_staticmethod = true,
        fn = fun
    }
    --with this the table of the instance will not be forwarded, but the
    --table of wrapper will always be, so we need to always remove it and shift all arguments
    setmetatable(wrapper, {
        __call = function(...)
            local arg = {...}
            for k, v in pairs(arg) do
                if k == 1 then arg[k] = nil
                elseif k == #arg then
                    arg[k-1] = v
                    arg[k] = nil
                else
                    arg[k-1] = v
                end
            end
            return wrapper.fn(table.unpack(arg))
        end,
    })
    return wrapper
end