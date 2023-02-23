str = {}
helper_functions = helper_functions or require("helper_functions")
class = class or require("class")
pyobj = pyobj or require("pyobj")
staticmethod = staticmethod or require("staticmethod")
local is_pyobj = helper_functions.is_pyobj
local calc_key = helper_functions.calc_key
local is_whitespace = helper_functions.is_whitespace

str = class(function(str)
    str.___name = "str"
    str.___d = ""

    -- TODO add encoding and errors??
    function str.__init__(self, object, encoding, errors)
        object = object or ""
        if is_pyobj(object) then
            if pytype(self) == pytype(object) then
                self = object
                return
            end
            self.___d = object.__str__().___d
            return
        end

        self.___d = tostring(object)
    end

    --Lua has no way to actually get size of an object so "¯\_(:))_/¯"
    function str.__sizeof__(self)
        return #self.___d + 3 + 1
    end

    function str.__add__(self, other)
        if is_pyobj(other) then
            return str(self.___d .. other.__str__().___d)
        end
        return str(self.___d .. other)
    end

    function str.__mul__(self, n)
        if is_pyobj(n) then
            --TODO
            return str(string.rep(self.___d, n.__int__().___d))
        end
        return str(string.rep(self.___d, n))
    end

    function str.__str__(self) return self end

    function str.__len__(self)
        return #self.___d
    end

    function str.___one_index(self, key)
        if type(key) ~= "number" then
            error("TypeError: string indices must be integers")
        end

        key = calc_key(#self.___d, key)
        if key > #self.___d then
            error("IndexError: string index out of range")
        end

        return str(string.sub(self.___d, key, key))
    end

    function str.___two_index(self, start, stop)
        start = calc_key(#self.___d, start)
        stop  = calc_key(#self.___d, stop)
        return str(string.sub(self.___d, start, stop-1))
    end

    function str.___three_index(self, start, stop, step)
        local temp = {}
        local ii = 1

        for i in op_in(range(start, stop, step)) do
            temp[ii] = self[i].___d
            ii = ii+1
        end
        local temp_str = ""
        for _, chr in ipairs(temp) do
            temp_str = temp_str .. chr
        end

        return str(temp_str)
    end

    function str.__getattr__(self, key)
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
    function str.__contains__(self, o)
        if not is_pyobj(o) and type(o) ~= "string" then
            error("Search element should be pyobj or lua str") end
        o = str(o)

        if o.__len__() == 0 then return false end

        local si = 0
        for i in op_in(range(#self.___d)) do
            --print(i, #self.___d, si, o.__len__())
            if self[i].___d == o[si].___d then
                si = si + 1
            end

            if si == o.__len__() then return true end
        end
        return false
    end

    function str.__eq__(self, o)
        if type(o) == "string" then return self.___d == o end
        if is_pyobj(o) then return self.___d == o.__str__().___d end
        return false
    end

    function str.__lt__(self, o)
        if type(o) == "string" then return self.___d < o end
        if is_pyobj(o) then return self.___d < o.__str__().___d end
        error("Cannot compare pystring and "..type(o))
    end

    function str.__le__(self, o)
        if type(o) == "string" then return self.___d <= o end
        if is_pyobj(o) then return self.___d <= o.__str__().___d end
        error("Cannot compare pystring and "..type(o))
    end

    function str.__repr__(self)
        return str("'"..self.___d.."'")
    end

    function str.__format__(self, format_spec)
        --string.format()
        error("python formatting is not implemented")
    end

    function str.__iter__(self)
        local iter = iter_obj_creator()
        iter.i = 0
        iter.max_pos = #self.___d
        iter.str = self
        iter.__next__ = function(self)
            if self.i < self.max_pos then
                self.i = self.i + 1
                return self.str[self.i-1]
            else
                return nil
            end
        end
        return iter
    end

    function str.__reversed__(self)
        local iter = iter_obj_creator()
        iter.i = #self.___d-1
        iter.min_pos = 0
        iter.str = self
        iter.__next__ = function(self)
            if self.i >= self.max_pos then
                self.i = self.i - 1
                return self.str[self.i+1]
            else
                return nil
            end
        end
        return iter
    end

    function str.lower(self) return str(string.lower(self.___d)) end
    function str.upper(self) return str(string.upper(self.___d)) end
    function str.capitalize(self)
        local fistchar = self[0].upper()
        local other_str = self[{1, -1}].lower()
        return fistchar+other_str
    end
    function str.casefold(self) return self.lower() end
    function str.center(self, num, char)
        local len = #self.___d
        char = char or " "

        if num <= len then
            return self
        end

        local tpad = num - len
        local rpad = math.floor(tpad/2)
        local lpad = tpad - rpad
        local pychar = str(char)

        return (pychar*lpad)+self+(pychar*rpad)
    end
    function str.count(self, value, start, stop)
        value = str(value)

        start = start or 0
        stop = stop or #self.___d

        start = calc_key(#self.___d, start)
        stop  = calc_key(#self.___d, stop)

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

    function str.encode(self, encoding, errors) error("Encoding not implemented") end

    function str.endswith(self, value, start, stop)
        value = str(value)

        start = start or 0
        stop = stop or #self.___d

        start = self.calc_key(#self.___d, start)
        stop  = self.calc_key(#self.___d, stop)

        -- if search boundary is less than value
        if stop - start < value.__len__() then return false end

        start = stop - value.__len__()

        local end_str = self[{start-1, stop-1}]
        return value == end_str
    end

    function str.expandtabs(self, num)
        return str(string.gsub(self.___d, "\t", (string.rep(" ", num))))
    end

    function str.find(self, sub, start, stop)
        start = start or 0
        stop = stop or #self.___d
        sub = str(sub)
        self = self[{start, stop}]
        local res = string.find(self.___d, sub.___d)[1]
        if res == nil then return -1 else return res-1 end
    end

    function str.format(self, ...) return self.__format__(...) end
    function str.format_map(self, ...) return self.__format__(...) end

    function str.index(self, sub, start, stop)
        start = start or 0
        stop = stop or #self.___d
        local res = self.find(sub, start, stop)
        if res == -1 then error("ValueError: No substring '".. str(sub).___d.."' in string '"..self.___d.."'")
        else return res end
    end

    function str.isalnum(self)
        if #self.___d == 0 then return false end
        return self.isalpha() or self.isdecimal() or self.isdigit() or self.isnumeric()
    end

    function str.isalpha(self)
        if #self.___d == 0 then return false end
        for i in op_in(range(#self.___d)) do
            local char = self[i].___d

            if not ((char >= "a" and char <= "z") or (char >= "A" and char <= "Z")) then
                return false
            end
        end
        return true
    end

    function str.isascii(self) return true end

    function str.isdecimal(self)
        if #self.___d == 0 then return false end
        for i in op_in(range(#self.___d)) do
            local char = self[i].___d

            if not (char >= "0" and char <= "9") then
                return false
            end
        end
        return true
    end

    function str.isdigit(self) return self.isdecimal() end

    -- TODO implement https://docs.python.org/3/reference/lexical_analysis.html#identifiers
    function str.isidentifier(self) error("isidentifier not implemented") end
    function str.islower(self)
        local has_cased = false

        for i in op_in(range(#self.___d)) do
            local char = self[i].___d
            if ((char >= "a" and char <= "z") or (char >= "A" and char <= "Z")) then
                has_cased = true
                break
            end
        end

        if has_cased == false then return false end

        return self == self.lower()
    end
    function str.isnumeric(self) return self.isdecimal() end

    function str.isprintable(self) return true end

    function str.isspace(self)
        if #self.___d == 0 then return false end

        for i in op_in(range(#self.___d)) do
            local ch = self[i].___d
            if not (ch >= "\0" and ch <= " ") then
                return false
            end
        end
        return true
    end

    --TODO implement
    function str.istitle(self) error("istitle not implemented") end

    function str.isupper(self)
        local has_cased = false

        for i in op_in(range(#self.___d)) do
            local char = self[i].___d
            if ((char >= "a" and char <= "z") or (char >= "A" and char <= "Z")) then
                has_cased = true
                break
            end
        end

        if has_cased == false then return false end

        return self == self.upper()
    end

    function str.join(self)
        local ret = str()
        local add = false
        for item in op_in(self) do
            if add then
                ret = ret + self
                add = false
            end
            ret = ret + item
            add = true
        end
        return ret
    end

    function str.ljust(self, width, fillchar)
        fillchar = fillchar or " "
        fillchar = str(fillchar)

        if width <= #self.___d then return self end
        fillchar = fillchar * (width - #self.___d)

        return self + fillchar
    end

    function str.rjust(self, width, fillchar)
        fillchar = fillchar or " "
        fillchar = str(fillchar)

        if width <= #self.___d then return self end
        fillchar = fillchar * (width - #self.___d)

        return fillchar + self
    end

    function str.lstrip(self, chars)
        chars = chars or "  \n"
        chars = str(chars)
        local left = 0
        for i in op_in(range(#self.___d)) do
            if op_in(self[i], chars) then
                left = left + 1
            else break end
        end
        return self[{left, #self.___d}]
    end

    function str.rstrip(self, chars)
        chars = chars or "  \n"
        chars = str(chars)
        local left = -1
        for i in op_in(range(#self.___d)) do
            if op_in(self[-(i+1)], chars) then
                left = left - 1
            else break end
        end
        return self[{0, left+1}]
    end

    function str.strip(self, chars) return self.lstrip(chars).rstrip(chars) end

    function str.maketrans(x, y, z)
        print(x, y, z)
        error("Not implemented")
    end

    str.maketrans_DECORATOR = str.maketrans; str.maketrans = staticmethod(str.maketrans_DECORATOR)

    function str.partition(self, sep)
        local idx = self.find(sep)
        if idx == -1 then return { self, str(), str()} end

        error("Not implemented")
    end

    function str.rpartition(self, sep)
        error("Not implemented")
    end

    function str.removeprefix(self, prefix)
        prefix = str(prefix)
        if self[{0, prefix.__len__()}] == prefix then return self[{prefix.__len__(), #self.___d}] else return self end
    end

    function str.removesuffix(self, suffix)
        suffix = str(suffix)
        if self[{-suffix.__len__(), #self.___d}] == suffix then return self[{0, #self.___d-suffix.__len__()}] else return self end
    end

    function str.replace(self, old, new, count)
        if count == nil then
            return str(self.___d.gsub(old, new))
        else
            return str(self.___d.gsub(old, new, count))
        end
    end

    function str.rfind(self, sub, start, stop)
        start = start or 0
        stop = stop or #self.___d
        sub = str(sub)
        self = self[{start, stop}]
        local _, res = string.find(self.___d, "^.*("..sub.___d..")")
        if _ == nil then return -1 else return res-1-sub.__len__() end
    end

    function str.rindex(self, sub, start, stop)
        start = start or 0
        stop = stop or #self.___d
        local res = self.rfind(sub, start, stop)
        if res == -1 then error("ValueError: No substring '".. str(sub).___d.."' in string '"..self.___d.."'")
        else return res end
    end

    --TODO refactor/rework
    local function split_with_separator(self, sep, maxsplit, list)
        sep = str(sep)
        local sep_len = sep.__len__()

        maxsplit = maxsplit or #self.___d
        if maxsplit < 0 then maxsplit = #self.___d end
        local chars = str()
        local splited = list()

        local pos = 0
        local max_pos = #self.___d


        while maxsplit > 0 and pos < max_pos do
            --local chr = self[pos]
            print(self[{pos, pos+sep_len}].___d, sep.___d, chars.___d, self[{pos, pos+sep_len}].___d == sep.___d)
            if pos+sep_len+1 > max_pos then break end
            if self[{pos, pos+sep_len}] == sep then
                splited.append(chars)
                chars = str()
                maxsplit = maxsplit - 1
                pos = pos + sep_len - 1
            else
                chars = chars + self[pos]
            end

            pos = pos + 1
        end

        chars = chars + self[{pos, max_pos}]

        if chars.__len__() > 0 then splited.append(chars) end

        return splited
    end

    --TODO refactor/rework
    local function split_whitespace(self, maxsplit, list)
        maxsplit = maxsplit or #self.___d
        if maxsplit < 0 then maxsplit = #self.___d end
        local chars = str()
        local splited = list()

        local pos = 0
        local max_pos = #self.___d

        while maxsplit > 0 and pos < max_pos do
            --local chr = self[pos]
            if is_whitespace(self[pos].___d) then
                if chars.__len__() > 0 then
                    splited.append(chars)
                    chars = str()
                    maxsplit = maxsplit - 1
                    --pos = pos + 1
                end
            else
                chars = chars + self[pos]
            end

            pos = pos + 1
        end

        chars = chars + self[{pos, max_pos}].lstrip()

        if chars.__len__() > 0 then splited.append(chars) end

        return splited
    end

    function str.split(self, sep, maxsplit)
        local list = require "list"

        if sep ~= nil then return split_with_separator(self, sep, maxsplit, list) end
        return split_whitespace(self, maxsplit, list)
    end

    function str.rsplit(self, sep, maxsplit)
        return str.split(self.__reversed__(), sep, maxsplit)
    end

    function str.splitlines(keepends)
        keepends = keepends or false
    end

    function str.startswith(self, prefix, start, stop)
        start = start or 0
        stop = stop or #self.___d
    end

    function str.swapcase(self) end

    function str.title(self)

    end

    function str.translate(self, table)

    end

    function str.zfill(self, width)
        if width <= #self.___d then return self end
        local has_leading = str()
        local fill_num = width - #self.___d
        local str
        if self[0].___d == "+" or self[0].___d == "-" then
            has_leading = self[0]
            fill_num = fill_num - 1
            str = self[{1, #self.___d}]
        else
            str = self
        end

        return has_leading + (str("0")*fill_num) + str
    end

    return str
end, {pyobj})

return str