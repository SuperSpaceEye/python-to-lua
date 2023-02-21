function iter_obj_creator() end
require("pylua_init")

function iter_obj_creator()
    return {
        ___is_pyobj = true,
        ___name = "iterator",
        __iter__ = function(self) return self end,
        __repr__ = function(self) return str("<"..self.___name.." object>") end,
        __str__ = function(self) return self.__repr__() end,
        __next__ = function(self) error("Iterator not implemented") end,
        __call = function(self) return self.__next__() end
    }
end

return iter_obj_creator