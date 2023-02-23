-- TODO use super().__init__ logic
--local staticmethod = staticmethod or require "staticmethod"
--local str = str or require "str"

--__STR__METHOD_CONTROLLER_DO_NOT_OVERWRITE = __STR__METHOD_CONTROLLER_DO_NOT_OVERWRITE or {
--    calls = {},
--    len = 0,
--    wrapper = function(fn, caller)
--        return function()
--            local recursed = false
--            print(caller)
--            for _, v in ipairs(__STR__METHOD_CONTROLLER_DO_NOT_OVERWRITE.calls) do
--                if rawequal(v, caller) then
--                    recursed = true
--                end
--            end
--
--            if not recursed then
--                table.insert(__STR__METHOD_CONTROLLER_DO_NOT_OVERWRITE.calls, caller)
--                local result = fn(caller)
--                table.remove(__STR__METHOD_CONTROLLER_DO_NOT_OVERWRITE.calls)
--                return result
--            else
--                return pystr("...")
--            end
--        end
--    end
--}

function class(class_init, inherited)
    inherited = inherited or {}

    local c = {}
    c.___is_pyobj = true

    for i = #inherited, 1, -1 do
        for k, v in pairs(inherited[i]) do
            if k ~= "__bases" then
                c[k] = v
            end
        end
    end

    c.___bases = {}
    for i = #inherited, 1, -1 do c.___bases[i] = inherited[i] end

    c = class_init(c)

    c.super = function()
        if c.___bases[1] ~= nil then
            return c.___bases[1]
        else
            return {__init__ = function() end}
        end
    end

    local mt = getmetatable(c) or {}
    mt.__call = function(_, ...)
        local object = {}
        object.___is_instance = true

        setmetatable(object, {
            __index = function(tbl, idx)
                local item = c[idx]
                if type(item) == "function" then
                    return function(...)
                        return c[idx](object, ...)
                    end
                elseif type(item) == "table" then
                    return item
                elseif item ~= nil then
                    return item
                else
                    return c.__getattr__(object, idx)
                end
            end,

            __newindex = function(tbl, key, value)
                if c.__setattr__ ~= nil then
                    c.__setattr__(tbl, key, value)
                else
                    rawset(tbl, key, value)
                end
            end,

            __call = function(tbl, ...) return tbl.__call__(...) end,
            __len = function(tbl) return tbl.__len__() end,
            __unm = function(tbl) return tbl.__neg__() end,
            __add = function(tbl, other) return tbl.__add__(other) end,
            __sub = function(tbl, other) return tbl.__sub__(other) end,
            __mul = function(tbl, other) return tbl.__mul__(other) end,
            __div = function(tbl, other) return tbl.__div__(other) end,
            __idiv= function(tbl, other) return tbl.__floordiv__(other) end,
            __mod = function(tbl, other) return tbl.__mod__(other) end,
            __pow = function(tbl, other) return tbl.__pow__(other) end,
            __concat = function(tbl, other) return tbl.__add__(other) end,

            __band = function(tbl, other) return tbl.__and__(other) end,
            __bor  = function(tbl, other) return tbl.__or__(other) end,
            __bxor = function(tbl, other) return tbl.__xor__(other) end,
            __bnot = function(tbl) return tbl.__not__() end,
            __shl  = function(tbl, other) return tbl.__lshift(other) end,
            __shr  = function(tbl, other) return tbl.__rshift(other) end,

            __eq = function(tbl, other) return tbl.__eq__(other) end,
            __lt = function(tbl, other) return tbl.__lt__(other) end,
            __le = function(tbl, other) return tbl.__le__(other) end,

            __gc = function(tbl) tbl.__del__() end
        })

        if type(object.__init__) == "function" then
            object.__init__(...)
        end
        --object.__str__ = __STR__METHOD_CONTROLLER_DO_NOT_OVERWRITE.wrapper(object.__str__, object)
        --object.__repr__ = __REPR__METHOD_CONTROLLER_DO_NOT_OVERWRITE.wrapper(object.__repr__, object)
        return object
    end
    setmetatable(c, mt)
    return c
end

return class