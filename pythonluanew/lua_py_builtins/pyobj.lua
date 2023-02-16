-- TODO use super().__init__ logic

function class(class_init, inherited)
    inherited = inherited or {}

    local c = {}
    c.__is_pyobj = true

    for i = #inherited, 1, -1 do
        for k, v in pairs(inherited[i]) do
            if k ~= "__bases" then
                c[k] = v
            end
        end
    end

    c.__bases = {}
    for i = #inherited, 1, -1 do c.__bases[i] = inherited[i] end

    c = class_init(c)

    c.super = function()
        if c.__bases[1] ~= nil then
            return c.__bases[1]
        else
            return {__init__ = function() end}
        end
    end

    local mt = getmetatable(c) or {}
    mt.__call = function(_, ...)
        local object = {}

        setmetatable(object, {
            __index = function(tbl, idx)
                local item = c[idx]
                if type(item) == "function" then
                    return function(...)
                        return c[idx](object, ...)
                    end
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
        })

        if type(object.__init__) == "function" then
            object.__init__(...)
        end

        return object
    end
    setmetatable(c, mt)
    return c
end

local function t_not_implemented(method, name)
    error("Not implemented: \""..method.."\" method is not implemented for \""..name.."\".")
end

local function t_not_impl_no_over(method, name)
    error(method.." is not implemented. do not overwrite this method in \""..name.."\" as this method requires special handling from python-to-lua compiler which is not implemented.")
end

--TODO add python errors ???
local pyObject = class(function(pyObject)
    pyObject.__name = "pyObject"
    function pyObject.__new__(cls, other) end
    function pyObject.__init__(self, other) print("Base init") end
    function pyObject.__del__(self) end

    function pyObject.__pos__(self) t_not_implemented("__pos__", self.__name) end
    function pyObject.__neg__(self) t_not_implemented("__neg__", self.__name) end
    function pyObject.__abs__(self) t_not_implemented("__abs__", self.__name) end
    function pyObject.__invert__(self) t_not_implemented("__invert__", self.__name) end
    function pyObject.__round__(self, n) t_not_implemented("__round__", self.__name) end
    function pyObject.__floor__(self) t_not_implemented("__floor__", self.__name) end
    function pyObject.__ceil__(self) t_not_implemented("__ceil__", self.__name) end
    function pyObject.__trunc__(self) t_not_implemented("__trunc__", self.__name) end

    -- TODO think of a way to add augmented assignments

    function pyObject.__int__(self) t_not_implemented("__int__", self.__name) end
    function pyObject.__float__(self) t_not_implemented("__float__", self.__name) end
    function pyObject.__complex__(self) t_not_implemented("__complex__", self.__name) end
    function pyObject.__oct__(self) t_not_implemented("__oct__", self.__name) end
    function pyObject.__hex__(self) t_not_implemented("__hex__", self.__name) end
    function pyObject.__index__(self) t_not_implemented("__index__", self.__name) end
    function pyObject.__trunc__(self) t_not_implemented("__trunc__", self.__name) end
    function pyObject.__coerce__(self, other) t_not_implemented("__coerce__", self.__name) end

    function pyObject.__str__(self) t_not_implemented("__str__", self.__name) end
    function pyObject.__repr__(self) t_not_implemented("__repr__", self.__name) end
    function pyObject.__unicode__(self) t_not_implemented("__unicode__", self.__name) end
    function pyObject.__format__(self, formatstr) t_not_implemented("__format__", self.__name) end
    function pyObject.__hash__(self) t_not_implemented("__hash__", self.__name) end
    function pyObject.__nonzero__(self) t_not_implemented("__nonzero__", self.__name) end
    function pyObject.__dir__(self) t_not_implemented("__dir__", self.__name) end
    function pyObject.__sizeof__(self) t_not_implemented("__sizeof__", self.__name) end

    function pyObject.__getattr__(self, name) error("AttributeError: '"..self.__name.."' object has no attribute '"..name.."'.") end
    function pyObject.__setattr__(self, name, value) rawset(self, name, value) end
    function pyObject.__delattr__(self, name) self[name]=nil end

    function pyObject.__add__(self, other) t_not_implemented("__add__", self.__name) end
    function pyObject.__sub__(self, other) t_not_implemented("__sub__", self.__name) end
    function pyObject.__mul__(self, other) t_not_implemented("__mul__", self.__name) end
    function pyObject.__floordiv__(self, other) t_not_implemented("__floordiv__", self.__name) end
    function pyObject.__div__(self, other) t_not_implemented("__div__", self.__name) end
    function pyObject.__truediv__(self, other) t_not_implemented("__truediv__", self.__name) end
    function pyObject.__mod__(self, other) t_not_implemented("__mod__", self.__name) end
    function pyObject.__divmod(self, other) t_not_implemented("__divmod__", self.__name) end
    function pyObject.__pow__(self, other, modulo) t_not_implemented("__pow__", self.__name) end
    function pyObject.__lshift__(self, other) t_not_implemented("__lshift__", self.__name) end
    function pyObject.__rshift__(self, other) t_not_implemented("__rshift__", self.__name) end
    function pyObject.__and__(self, other) t_not_implemented("__and__", self.__name) end
    function pyObject.__or__(self, other) t_not_implemented("__or__", self.__name) end
    function pyObject.__xor__(self, other) t_not_implemented("__xor__", self.__name) end

    function pyObject.__radd__(self, other) t_not_implemented("__radd__", self.__name) end
    function pyObject.__rsub__(self, other) t_not_implemented("__rsub__", self.__name) end
    function pyObject.__rmul__(self, other) t_not_implemented("__rmul__", self.__name) end
    function pyObject.__rfloordiv__(self, other) t_not_implemented("__rfloordiv__", self.__name) end
    function pyObject.__rdiv__(self, other) t_not_implemented("__rdiv__", self.__name) end
    function pyObject.__rtruediv__(self, other) t_not_implemented("__rtruediv__", self.__name) end
    function pyObject.__rmod__(self, other) t_not_implemented("__rmod__", self.__name) end
    function pyObject.__rdivmod(self, other) t_not_implemented("__rdivmod__", self.__name) end
    function pyObject.__rpow__(self, other, modulo) t_not_implemented("__rpow__", self.__name) end
    function pyObject.__rlshift__(self, other) t_not_implemented("__rlshift__", self.__name) end
    function pyObject.__rrshift__(self, other) t_not_implemented("__rrshift__", self.__name) end
    function pyObject.__rand__(self, other) t_not_implemented("__rand__", self.__name) end
    function pyObject.__ror__(self, other) t_not_implemented("__ror__", self.__name) end
    function pyObject.__rxor__(self, other) t_not_implemented("__rxor__", self.__name) end

    function pyObject.__lt__(self, other) t_not_implemented("__lt__", self.__name) end
    function pyObject.__le__(self, other) t_not_implemented("__le__", self.__name) end
    function pyObject.__eq__(self, other) t_not_implemented("__eq__", self.__name) end
    function pyObject.__ne__(self, other) t_not_implemented("__ne__", self.__name) end
    function pyObject.__gt__(self, other) t_not_implemented("__gt__", self.__name) end
    function pyObject.__ge__(self, other) t_not_implemented("__ge__", self.__name) end

    function pyObject.__next__(self) t_not_implemented("__next__", self.__name) end
    function pyObject.__anext__(self) t_not_implemented("__anext__", self.__name) end

    function pyObject.__len__(self) t_not_implemented("__len__", self.__name) end
    function pyObject.__iter__(self) t_not_implemented("__iter__", self.__name) end
    function pyObject.__reversed__(self) t_not_implemented("__reversed__", self.__name) end
    pyObject.__contains__ = nil
    function pyObject.__missing__(self, key) return nil end

    function pyObject.__doc__(self) return nil end
    -- TODO somehow generate
    --function pyObject.__name__(self) return self.__name end
    --function pyObject.__qualname__(self) t_not_impl_no_over("__qualname__", self.__name) end
    --TODO
    function pyObject.__file__(self) t_not_impl_no_over("__file__", self.__name) end
    function pyObject.__module__(self)   t_not_impl_no_over("__module__", self.__name) end
    function pyObject.__defaults__(self) t_not_impl_no_over("__defaults__", self.__name) end
    function pyObject.__code__(self) t_not_impl_no_over("__code__", self.__name) end
    function pyObject.__globals(self) t_not_impl_no_over("__globals__", self.__name) end
    function pyObject.__closure__(self) t_not_impl_no_over("__closure__", self.__name) end
    -- TODO add tuple https://stackoverflow.com/questions/13964764/lua-how-to-avoid-circular-requires
    function pyObject.__annotations__(self) return {} end
    function pyObject.__kwdefaults__(self) t_not_impl_no_over("__kwdefaults__", self.__name) end
    function pyObject.__instancecheck__(self, instance) t_not_impl_no_over("__instancecheck__", self.__name) end
    function pyObject.__subclasscheck__(self, subclass) t_not_impl_no_over("__subclasscheck__", self.__name) end
    --TODO special handling for __dict__
    --TODO add type checks
    function pyObject.__dict__(self, key, value)
        if value == nil then
            return self[key]
        else
            rawset(self, key, value)
        end
    end
    
    return pyObject
end, {})

local Test1 = class(function(Test1)
    Test1.__name = "Test1"
    function Test1.__init__(self)
        print("deb test1", self.super().__name)
        Test1.super().__init__(self)
        self.test = 10
        print("Test1 initialized")
    end

    function Test1.print_test(self)
        print(self.test)
    end
    return Test1
end, {pyObject})

print(Test1)

local Test2 = class(function(Test2)
    Test2.__name = "Test2"
    function Test2.__init__(self)
        print("Test2 initialization start")
        Test2.super().__init__(self)
        self.test = 20
        print("Test2 initialized")
    end

    function Test2.print_test(self)
        print(self.test)
    end
    return Test2
end, {Test1})

a = Test1()
a.print_test()

b = Test2()
b.print_test()