class = require "class"
pyobj = require "pyobj"
operator_in = require "operator_in"
str = str or require "str"
local helper_functions = (require "helper_functions")
local calc_key = helper_functions.py_calc_key
local is_pyobj = helper_functions.is_pyobj
local del = require "del"
local None = require "none"
local zip = require "zip"


list = class(function(list)
    list.___name = "list"
    list.___d = {}
    list.___is_pylist = true
    list.___size = 0
    list.___had_repr = false
    list.___had_str = false

    function list.__init__(self, obj)
        self.___d = {}
        self.___size = 0
        self.___had_repr = false
        self.___had_str = false

        if type(obj) == "table" and obj.___is_pyobj then
            if obj.___is_pylist then self = obj
            else
                for item in operator_in(obj) do
                    self.append(item)
                end
            end
        elseif type(obj) == "table" then
            local i = 1
            while obj[i] do
                self.___d[i] = obj[i]
                i = i + 1
            end
            --print("===")
            self.___size = i-1
        end
    end

    function list.__setattr__(self, key, value)
        if type(key) == "string" and self[key] ~= nil then rawset(self, key, value) return end

        if type(key) ~= "number" then error("Key not a number") end
        key = calc_key(self.__len__(), key)
        if key < self.___size and key >= 0 then
            self.___d[key+1] = value
        else
            error("IndexError: index out of range")
        end
    end

    function list.___slice_access(self, key)
        if key[1] == None or key[1] == nil then key[1] = 0 end
        if key[2] == None or key[2] == nil then key[2] = self.__len__() end
        if key[3] == None or key[3] == nil then key[3] = 1 end

        local slice = list()

        for item in range(key[1], key[2], key[3]) do
            slice.append(item)
        end

        return slice
    end

    function list.__getattr__(self, key)
        if type(key) == "string" and rawget(self, key) ~= nil then return rawget(self, key) end

        if type(key) == "table" then return self.___slice_access(key) end
        key = calc_key(self.__len__(), key)
        if type(key) ~= "number" then error("Key not a number") end
        if key >= self.___size or key < 0 then error("Out of bounds access") end
        return self.___d[key+1]
    end

    function list.__len__(self) return self.___size end

    function list.__sizeof__(self) return self.___size end

    function list.__iter__(self)
        return {
            i = 0,
            max_pos = self.__len__(),
            _list = self,
            __next__ = function(self)
                if self.i < self.max_pos then
                    self.i = self.i + 1
                    return self._list[self.i-1]
                else
                    return nil
                end
            end
        }
    end

    function list.__reversed__(self)
        return {
            i = self.__len__()-1,
            min_pos = 0,
            _list = self,
            __next__ = function(self)
                if self.i >= self.max_pos then
                    self.i = self.i - 1
                    return self._list[self.i+1]
                else
                    return nil
                end
            end
        }
    end

    function list.__str__(self)
        if self.___had_str then
            self.___had_str = false
            return str("[...]")
        end

        self.___had_str = true
        local str = str("[")
        local add = false
        for item in operator_in(self) do
            if add then str = str + ", " end
            if type(item) == "table" and item.___is_pyobj then
                str = str + item.__repr__()
                add = true
            elseif type(item) == "number" or type(item) == "string" then
                str = str + item
                add = true
            else
                error("Niooo")
            end
        end
        str = str + "]"
        self.___had_str = false
        return str
    end

    function list.__repr__(self)
        if self.___had_repr then
            self.___had_repr = false
            return str("[...]")
        end
        self.___had_repr = true
        local ret = self.__str__()
        self.___had_repr = false
        return ret
    end

    function list.__contains__(self, x)
        if is_pyobj(x) then
            if x.__eq__ ~= nil then
                for item in operator_in(self) do if x == item then return true end end
            else
                for item in operator_in(self) do if x.__repr__() == item then return true end end
            end
        else
            for item in operator_in(self) do if rawequal(x, item) then return true end end
        end
        return false
    end

    function list.__eq__(self, o)
        if not is_pyobj(o) then return false end
        if not o.___is_pylist then return false end
        if self.__len__() ~= o.__len__() then return false end

        for it1, it2 in zip(self, o) do
            if it1 ~= it2 then return false end
        end
        return true
    end

    function list.__format__(self, format_spec)
        error("Not implemented")
    end

    function list.__le__(self, other)  end
    function list.__lt__(self, other)  end

    function list.__add__(self, other)
        local copy = self.copy()
        copy.extend(other)
        return copy
    end

    function list.__mul__(self, mul)
        if type(mul) ~= "number" then error("Not a number") end
        if mul <= 0 then return list() end

        local copy = self.copy()
        if mul == 1 then return copy end
        for _ in range(mul-1) do
            copy.extend(self)
        end
        return copy
    end

    function list.append(self, item)
        self.___size = self.___size + 1
        self[self.___size-1] = item
    end

    function list.extend(self, iter)
        for item in operator_in(iter) do
            self.append(item)
        end
    end

    function list.insert(self, i, x)
        i = calc_key(self.__len__(), i, false)
        self.___size = self.___size + 1
        for _i in range(self.__len__()-1, i, -1) do
            self[_i] = self[_i-1]
        end
        self[i] = x
    end

    function list.remove(self, x)
        for i, item in enumerate(operator_in(self)) do
            if rawequal(item, x) then
                for _i in range(self.__len__()-1, i, -1) do
                    self[_i-1] = self[_i]
                end
                del(self[self.__len__()-1])
                self[self.__len__()-1] = nil
                return
            end
        end
        error("ValueError:")
    end

    function list.pop(self, i)
        i = i or (self.__len__()-1)
        i = calc_key(self.__len__(), i, false)

        local item = self[i]

        for _i in range(self.__len__()-1, i, -1) do
            self[_i-1] = self[_i]
        end
        self[self.__len__()-1] = nil
        self.___size = self.___size - 1

        return item
    end

    function list.clear(self)
        for item in operator_in(self) do
            del(item)
        end
        self.___d = {}
        self.___size = 0
    end

    function list.index(self, x, start, stop)
        start = start or 0
        stop = stop or self.__len__()
        start = calc_key(self.__len__(), start, false)
        stop =  calc_key(self.__len__(), stop, false)

        local slice
        if start == 0 and stop == self.__len__()-1 then
            slice = self
        else
            slice = self[{start, stop, None}]
        end
        if is_pyobj(x) then
            if x.__eq__ ~= nil then
                for i, item in enumerate(operator_in(slice)) do if x == item then return i end end
            else
                for i, item in enumerate(operator_in(slice)) do if x.__repr__() == item then return i end end
            end
        else
            for i, item in enumerate(operator_in(slice)) do if rawequal(x, item) then return i end end
        end

        error("ValueError:")
    end

    function list.count(self, x)
        local num = 0
        if is_pyobj(x) then
            if x.__eq__ ~= nil then
                for item in operator_in(self) do if x == item then num = num + 1 end end
            else
                for item in operator_in(self) do if x.__repr__() == item then num = num + 1 end end
            end
        else
            for item in operator_in(self) do if rawequal(x, item) then num = num + 1 end end
        end
        return num
    end

    function list.sort(self, key, reverse)
        key = key or function(left, right) return left < right end
        reverse = reverse or false

        if reverse then
            local k = key
            key = function(l, r) return not k(l, r) end
        end

        table.sort(self.___d, key)
    end

    function list.reverse(self)
        for i in range(0, math.floor(self.__len__()/2)) do
            print(i, -(i+1))
            self[i], self[-(i+1)] = self[-(i+1)], self[i]
        end
    end

    function list.copy(self) 
        local copy = list()
        copy.extend(self)
        return copy 
    end

    return list
end, {pyobj})

--local b = list({3, 4, 5, 6, 7})
--
--print(b.__str__().___d)

return list