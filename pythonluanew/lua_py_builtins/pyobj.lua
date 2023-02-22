pyobj = {}
--require("pylua_init")

class = class or require("class")

local function t_not_implemented(method, name)
    error("Not implemented: \""..method.."\" method is not implemented for \""..name.."\".")
end

local function t_not_impl_no_over(method, name)
    error(method.." is not implemented. do not overwrite this method in \""..name.."\" as this method requires special handling from python-to-lua compiler which is not implemented.")
end

--TODO add python errors ???
pyobj = class(function(pyObject)
    pyObject.___name = "pyObject"
    function pyObject.__new__(cls, other) end
    function pyObject.__init__(self, other) print("Base init") end
    function pyObject.__del__(self) end
    --function pyObject.__call__(self) t_not_implemented("__call__", self.___name) end

    --function pyObject.__pos__(self) t_not_implemented("__pos__", self.___name) end
    --function pyObject.__neg__(self) t_not_implemented("__neg__", self.___name) end
    --function pyObject.__abs__(self) t_not_implemented("__abs__", self.___name) end
    --function pyObject.__invert__(self) t_not_implemented("__invert__", self.___name) end
    --function pyObject.__round__(self, n) t_not_implemented("__round__", self.___name) end
    --function pyObject.__floor__(self) t_not_implemented("__floor__", self.___name) end
    --function pyObject.__ceil__(self) t_not_implemented("__ceil__", self.___name) end
    --function pyObject.__trunc__(self) t_not_implemented("__trunc__", self.___name) end

    -- TODO think of a way to add augmented assignments

    --function pyObject.__int__(self) t_not_implemented("__int__", self.___name) end
    --function pyObject.__float__(self) t_not_implemented("__float__", self.___name) end
    --function pyObject.__complex__(self) t_not_implemented("__complex__", self.___name) end
    --function pyObject.__oct__(self) t_not_implemented("__oct__", self.___name) end
    --function pyObject.__hex__(self) t_not_implemented("__hex__", self.___name) end
    --function pyObject.__index__(self) t_not_implemented("__index__", self.___name) end
    --function pyObject.__trunc__(self) t_not_implemented("__trunc__", self.___name) end
    --function pyObject.__coerce__(self, other) t_not_implemented("__coerce__", self.___name) end

    function pyObject.__str__(self) return self.__repr__() end
    function pyObject.__repr__(self) return str(tostring(self)) end
    --function pyObject.__unicode__(self) t_not_implemented("__unicode__", self.___name) end
    --function pyObject.__format__(self, formatstr) t_not_implemented("__format__", self.___name) end
    pyObject.__hash__ = None
    --function pyObject.__nonzero__(self) t_not_implemented("__nonzero__", self.___name) end
    -- TODO implement __dir__
    --function pyObject.__dir__(self) t_not_implemented("__dir__", self.___name) end
    --function pyObject.__sizeof__(self) t_not_implemented("__sizeof__", self.___name) end

    --function pyObject.__getattr__(self, name) error("AttributeError: '"..self.___name.."' object has no attribute '"..name.."'.") end
    function pyObject.__setattr__(self, name, value) rawset(self, name, value) end
    --function pyObject.__delattr__(self, name) t_not_implemented("__delattr__", self.___name) end

    --function pyObject.__add__(self, other) t_not_implemented("__add__", self.___name) end
    --function pyObject.__sub__(self, other) t_not_implemented("__sub__", self.___name) end
    --function pyObject.__mul__(self, other) t_not_implemented("__mul__", self.___name) end
    --function pyObject.__floordiv__(self, other) t_not_implemented("__floordiv__", self.___name) end
    --function pyObject.__div__(self, other) t_not_implemented("__div__", self.___name) end
    --function pyObject.__truediv__(self, other) t_not_implemented("__truediv__", self.___name) end
    --function pyObject.__mod__(self, other) t_not_implemented("__mod__", self.___name) end
    --function pyObject.__divmod(self, other) t_not_implemented("__divmod__", self.___name) end
    --function pyObject.__pow__(self, other, modulo) t_not_implemented("__pow__", self.___name) end
    --function pyObject.__lshift__(self, other) t_not_implemented("__lshift__", self.___name) end
    --function pyObject.__rshift__(self, other) t_not_implemented("__rshift__", self.___name) end
    --function pyObject.__and__(self, other) t_not_implemented("__and__", self.___name) end
    --function pyObject.__or__(self, other) t_not_implemented("__or__", self.___name) end
    --function pyObject.__xor__(self, other) t_not_implemented("__xor__", self.___name) end

    --function pyObject.__radd__(self, other) t_not_implemented("__radd__", self.___name) end
    --function pyObject.__rsub__(self, other) t_not_implemented("__rsub__", self.___name) end
    --function pyObject.__rmul__(self, other) t_not_implemented("__rmul__", self.___name) end
    --function pyObject.__rfloordiv__(self, other) t_not_implemented("__rfloordiv__", self.___name) end
    --function pyObject.__rdiv__(self, other) t_not_implemented("__rdiv__", self.___name) end
    --function pyObject.__rtruediv__(self, other) t_not_implemented("__rtruediv__", self.___name) end
    --function pyObject.__rmod__(self, other) t_not_implemented("__rmod__", self.___name) end
    --function pyObject.__rdivmod(self, other) t_not_implemented("__rdivmod__", self.___name) end
    --function pyObject.__rpow__(self, other, modulo) t_not_implemented("__rpow__", self.___name) end
    --function pyObject.__rlshift__(self, other) t_not_implemented("__rlshift__", self.___name) end
    --function pyObject.__rrshift__(self, other) t_not_implemented("__rrshift__", self.___name) end
    --function pyObject.__rand__(self, other) t_not_implemented("__rand__", self.___name) end
    --function pyObject.__ror__(self, other) t_not_implemented("__ror__", self.___name) end
    --function pyObject.__rxor__(self, other) t_not_implemented("__rxor__", self.___name) end

    --function pyObject.__lt__(self, other) t_not_implemented("__lt__", self.___name) end
    --function pyObject.__le__(self, other) t_not_implemented("__le__", self.___name) end
    --function pyObject.__eq__(self, other) t_not_implemented("__eq__", self.___name) end
    function pyObject.__ne__(self, other) return ~self.__eq__(other) end
    function pyObject.__gt__(self, other) return ~self.__lt__(other) end
    function pyObject.__ge__(self, other) return ~self.__lt__(other) or self.__eq__(other) end

    --function pyObject.__next__(self) t_not_implemented("__next__", self.___name) end
    --function pyObject.__anext__(self) t_not_implemented("__anext__", self.___name) end
    --
    --function pyObject.__len__(self) t_not_implemented("__len__", self.___name) end
    --function pyObject.__iter__(self) t_not_implemented("__iter__", self.___name) end
    --function pyObject.__reversed__(self) t_not_implemented("__reversed__", self.___name) end
    pyObject.__contains__ = nil
    function pyObject.__missing__(self, key) return nil end

    function pyObject.__doc__(self) return nil end
    -- TODO somehow generate
    --function pyObject.__name__(self) return self.___name end
    --function pyObject.__qualname__(self) t_not_impl_no_over("__qualname__", self.___name) end
    --TODO
    function pyObject.__file__(self) t_not_impl_no_over("__file__", self.___name) end
    function pyObject.__module__(self)   t_not_impl_no_over("__module__", self.___name) end
    function pyObject.__defaults__(self) t_not_impl_no_over("__defaults__", self.___name) end
    function pyObject.__code__(self) t_not_impl_no_over("__code__", self.___name) end
    function pyObject.__globals(self) t_not_impl_no_over("__globals__", self.___name) end
    function pyObject.__closure__(self) t_not_impl_no_over("__closure__", self.___name) end
    -- TODO add tuple https://stackoverflow.com/questions/13964764/lua-how-to-avoid-circular-requires
    function pyObject.__annotations__(self) return {} end
    function pyObject.__kwdefaults__(self) t_not_impl_no_over("__kwdefaults__", self.___name) end
    function pyObject.__instancecheck__(self, instance) t_not_impl_no_over("__instancecheck__", self.___name) end
    function pyObject.__subclasscheck__(self, subclass) t_not_impl_no_over("__subclasscheck__", self.___name) end
    function pyObject.__reduce__(self) t_not_impl_no_over("__reduce__", self.___d) end
    function pyObject.__reduce_ex__(self, protocol) t_not_impl_no_over("__reduce__", self.___d) end
    --TODO special handling for __dict__
    --TODO add type checks
    --function pyObject.__dict__(self, key, value)
    --    if value == nil then
    --        return self[key]
    --    else
    --        rawset(self, key, value)
    --    end
    --end

    return pyObject
end, {})

return pyobj