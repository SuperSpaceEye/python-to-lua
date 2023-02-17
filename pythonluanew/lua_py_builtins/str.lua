require "class"
require "pyobj"
range = require "range"
operator_in = require "operator_in"

pystr = class(function(pystr)
    pystr.___name = "str"
    pystr.___d = ""
    pystr.___is_pystr = true

    -- TODO add encoding and errors??
    function pystr.__init__(self, object, encoding, errors)
        if object.___is_pyobj then
            --if object.___is_pystr then
            --    self = object
            --    return
            --end
            self.___d = object.__str__().___d
            return
        end

        self.___d = tostring(object)
    end

    --Lua has no way to actually get size of an object so "¯\_(:))_/¯"
    function pystr.__sizeof__(self)
        return #self.___d + 3 + 1
    end

    function pystr.__add__(self, other)
        if other.___is_pyobj then
            return pystr(self.___d .. other.__str__().___d)
        end
        return pystr(self.___d .. other)
    end

    function pystr.__mul__(self, n)
        if n.___is_pyobj then
            --TODO
            return pystr(string.rep(self.___d, n.__int__().___d))
        end
        return pystr(string.rep(self.___d, n))
    end

    function pystr.__str__(self) return self end

    function pystr.__len__(self)
        return #self.___d
    end

    function pystr.___calc_key(self, key, give_error)
        give_error = give_error or true
        if key < 0 then
            key = self.__len__() + key + 1
            if key <= 0 then
                if give_error then
                    error("IndexError: string index out of range")
                else
                    key = 1
                end
            end
            return key
        end
        if key > self.__len__() then
            if give_error then
                error("IndexError: string index out of range")
            else
                key = self.__len__()
            end
        end

        return key + 1
    end

    function pystr.___one_index(self, key)
        if type(key) ~= "number" then
            error("TypeError: string indices must be integers")
        end

        key = self.___calc_key(key)
        if key > self.__len__() then
            error("IndexError: string index out of range")
        end

        return pystr(string.sub(self.___d, key, key))
    end

    function pystr.___two_index(self, start, stop)
        start = self.___calc_key(start)
        stop  = self.___calc_key(stop)
        return pystr(string.sub(self.___d, start, stop-1))
    end

    function pystr.___three_index(self, start, stop, step)
        local temp = {}
        local ii = 1

        for i in range(start, stop, step) do
            temp[ii] = self[i].__str__().___d
            ii = ii+1
        end
        local temp_str = ""
        for _, chr in ipairs(temp) do
            temp_str = temp_str .. chr
        end

        return pystr(temp_str)
    end

    function pystr.__getattr__(self, key)
        local v1
        local v2
        local v3

        if type(key) == "table" then
            v1 = key[1]
            v2 = key[2]
            v3 = key[3]
        elseif type(key) == "number" then
            return self.___one_index(key)
        else
            print(key)
            error("Incorrect var type")
        end

        if v1 ~= nil and v2 ~= nil and v3 == nil or v3 == 1 then
            return self.___two_index(v1, v2)
        end

        if v1 ~= nil and v2 ~= nil and v3 ~= nil then
            return self.___three_index(v1, v2, v3)
        end
    end

    --TODO replace with string.find()
    function pystr.__contains__(self, o)
        if o.___is_pystr ~= true and type(o) ~= "string" then
            error("Search element should be pystr or lua str") end
        o = pystr(o)
        --print("deb", self.__len__(), o.__len__())

        local si = 0
        --print(self.__len__(), self.___d, o.__len__(), o.___d)
        for i in range(self.__len__()) do
            if self[i].__str__().___d == o[si].__str__().___d then
                si = si + 1
            end

            if si == o.__len__() then return true end
        end
        return false
    end

    function pystr.__eq__(self, o)
        if type(o) == "string" then return self.__str__() == o end
        if type(o) == "table" and o.___is_pystr then return self.__str__().___d == o.__str__().___d end
        return false
    end

    function pystr.__lt__(self, o)
        if type(o) == "string" then return self.__str__() < o end
        if type(o) == "table" and o.___is_pystr then return self.__str__().___d < o.__str__().___d end
        error("Cannot compare pystring and "..type(o))
    end

    function pystr.__le__(self, o)
        if type(o) == "string" then return self.__str__() <= o end
        if type(o) == "table" and o.___is_pystr then return self.__str__().___d <= o.__str__().___d end
        error("Cannot compare pystring and "..type(o))
    end

    function pystr.__repr__(self)
        return pystr("'"..self.__str__().___d.."'")
    end

    function pystr.__format__(self, format_spec)
        --string.format()
        error("python formatting is not implemented")
    end


    function pystr.lower(self) return pystr(string.lower(self.___d)) end
    function pystr.upper(self) return pystr(string.upper(self.___d)) end
    function pystr.capitalize(self)
        local fistchar = self[0].upper()
        local other_str = self[{1, -1}].lower()
        return fistchar+other_str
    end
    function pystr.casefold(self) return self.lower() end
    function pystr.center(self, num, char)
        local len = self.__len__()
        if num <= len then
            return self
        end

        local tpad = num - len
        local rpad = math.floor(tpad/2)
        local lpad = tpad - rpad
        local pychar = pystr(char)

        return (pychar*lpad)+self+(pychar*rpad)
    end
    function pystr.count(self, value, start, stop)
        value = pystr(value)

        start = start or 0
        stop = stop or self.__len__()

        start = self.___calc_key(start)
        stop  = self.___calc_key(stop)

        local count = 0
        local val_i = 0
        local i = 0
        local str = self[{start-1, stop-1}]

        while i <= stop-start-1 do
            if str[i] == value[val_i] then
                val_i = val_i + 1
            end
            i = i + 1

            if val_i == value.__len__() then
                count = count + 1
                val_i = 0
            end
        end
        return count
    end

    function pystr.encode(self, encoding, errors) error("Encoding not implemented") end

    function pystr.endswith(self, value, start, stop)
        value = pystr(value)

        start = start or 0
        stop = stop or self.__len__()

        start = self.___calc_key(start)
        stop  = self.___calc_key(stop)

        -- if search boundary is less than value
        if stop - start < value.__len__() then return false end

        start = stop - value.__len__()

        local end_str = self[{start-1, stop-1}]
        return value == end_str
    end

    function pystr.expandtabs(self, num)
        return pystr(string.gsub(self.___d, "\t", (string.rep(" ", num))))
    end

    function pystr.find(self, sub, start, stop)
        sub = pystr(sub)[{start, stop}]
        local res = string.find(self.___d, sub.___d)[1]
        if res == nil then return -1 else return res-1 end
    end

    function pystr.format(self, ...) return self.__format__(...) end
    function pystr.format_map(self, ...) return self.__format__(...) end

    function pystr.index(self, sub, start, stop)
        local res = self.find(sub, start, stop)
        if res == -1 then error("ValueError: No substring '"..pystr(sub).___d.."' in string '"..self.___d.."'")
        else return res end
    end

    function pystr.isalnum(self)
        if self.__len__() == 0 then return false end
        return self.isalpha() or self.isdecimal() or self.isdigit() or self.isnumeric()
    end

    function pystr.isalpha(self)
        if self.__len__() == 0 then return false end
        for i in range(self.__len__()) do
            local char = self[i].___d

            if ~((char >= "a" and char <= "z") or (char >= "A" and char <= "Z")) then
                return false
            end
        end
        return true
    end

    function pystr.isascii(self) return true end

    function pystr.isdecimal(self)
        if self.__len__() == 0 then return false end
        for i in range(self.__len__()) do
            local char = self[i].___d

            if ~(char >= "0" and char <= "9") then
                return false
            end
        end
        return true
    end

    function pystr.isdigit(self) return self.isdecimal() end

    -- TODO implement https://docs.python.org/3/reference/lexical_analysis.html#identifiers
    function pystr.isidentifier(self) error("isidentifier not implemented") end
    function pystr.islower(self)
        local has_cased = false

        for i in range(self.__len__()) do
            local char = self[i].___d
            if ((char >= "a" and char <= "z") or (char >= "A" and char <= "Z")) then
                has_cased = true
                break
            end
        end

        if has_cased == false then return false end

        return self == self.lower()
    end
    function pystr.isnumeric(self) return self.isdecimal() end

    function pystr.isprintable(self) return true end

    function pystr.isspace(self)
        if self.__len__() == 0 then return false end

        for i in range(self.__len__()) do
            local ch = self[i].___d
            if ~(ch >= "\0" and ch <= " ") then
                return false
            end
        end
        return true
    end

    --TODO implement
    function pystr.istitle(self) error("istitle not implemented") end

    function pystr.isupper(self)
        local has_cased = false

        for i in range(self.__len__()) do
            local char = self[i].___d
            if ((char >= "a" and char <= "z") or (char >= "A" and char <= "Z")) then
                has_cased = true
                break
            end
        end

        if has_cased == false then return false end

        return self == self.upper()
    end

    function pystr.join(iter)
        local ret = pystr()
        local add = false
        for item in operator_in(iter) do
            if add then
                ret = ret + self
                add = false
            end
            ret = ret + item
            add = true
        end
        return ret
    end

    function pystr.ljust(self, width, fillchar)
        fillchar = pystr(fillchar) or pystr(" ")

        if width <= self.__len__() then return self end
        fillchar = fillchar * (width - self.__len__())

        return self + fillchar
    end

    function pystr.lstrip(self, chars)
        chars = chars or "  \n"
        chars = pystr(chars)
        local left = 0
        for i in range(self.__len__()) do
            if operator_in(self[i], chars) then
                left = left + 1
            else break end
        end
        return self[{left, self.__len__()}]
    end

    function pystr.rstrip(self, chars)
        chars = chars or "  \n"
        chars = pystr(chars)
        local left = -1
        for i in range(self.__len__()) do
            if operator_in(self[-(i+1)], chars) then
                left = left - 1
            else break end
        end
        return self[{0, left+1}]
    end

    function pystr.strip(self, chars) return self.lstrip(chars).rstrip(chars) end

    function pystr.maketrans(x, y, z)
        error("Not implemented")
    end

    return pystr
end, {pyobj})

a = pystr("10")
b = pystr("20")
print(a[1].___d)
print((a + b).___d)
print(a > b)