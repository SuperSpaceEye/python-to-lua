test = require "range"
range = test.range

pystr = {}
setmetatable(pystr, {
    __call = function(_, t)
        local result = {}

        result._is_str = true

        result._data = ""

        if type(t) == "table" then
            if t._is_str then
                result = t
            else
                for _, v in ipairs(t) do
                    t = v
                    break
                end
            end
        end

        if type(t) == "table" then
            --error("unknown type")
        elseif type(t) == "string" then
            result._data = t
        else
            --error("Not a string")
            result._data = tostring(t)
        end

        -- private methods
        local pm = {}
        -- methods
        local m = {}

        pm.calc_key = function(key, give_error)
            give_error = give_error or true
            if key < 0 then
                key = m.len() + key + 1
                if key <= 0 then
                    if give_error then
                        error("IndexError: string index out of range")
                    else
                        key = 1
                    end
                end
                return key
            end
            if key > m.len() then
                if give_error then
                    error("IndexError: string index out of range")
                else
                    key = m.len()
                end
            end

            return key + 1
        end

        pm.one_index = function(key)
            if type(key) ~= "number" then
                error("TypeError: string indices must be integers")
            end

            key = pm.calc_key(key)
            if key > m.len() then
                error("IndexError: string index out of range")
            end

            return pystr(string.sub(result._data, key, key))
        end

        pm.two_index = function(start, stop)
            start = pm.calc_key(start)
            stop  = pm.calc_key(stop)
            return pystr(string.sub(result._data, start, stop-1))
        end

        pm.three_index = function(start, stop, step)
            local temp = {}
            local ii = 1

            for i in range(start, stop, step) do
                temp[ii] = result[i]()
                ii = ii+1
            end
            local temp_str = ""
            for _, chr in ipairs(temp) do
                temp_str = temp_str .. chr
            end

            return pystr(temp_str)
        end

        pm.index_access = function(v)
            local v1
            local v2
            local v3

            if type(v) == "table" then
                v1 = v[1]
                v2 = v[2]
                v3 = v[3]
            elseif type(v) == "number" then
                return pm.one_index(v)
            else
                error("Incorrect var type")
            end


            if v1 ~= nil and v2 ~= nil and v3 == nil or v3 == 1 then
                return pm.two_index(v1, v2)
            end


            if v1 ~= nil and v2 ~= nil and v3 ~= nil then
                return pm.three_index(v1, v2, v3)
            end
        end

        m.len = function()
            return string.len(result._data)
        end

        m.lower = function()
            return pystr(string.lower(result._data))
        end

        m.upper = function()
            return pystr(string.upper(result._data))
        end

        m.capitalize = function()
            local fistchar = result[0].upper()
            local other_str = result[{1, -1}].lower()
            return fistchar..other_str
        end

        m.casefold = function()
            return m.lower()
        end

        m.center = function(num, char)
            local len = #result._data
            if num <= len then
                return result
            end

            local tpad = num - len
            local rpad = math.floor(tpad/2)
            local lpad = tpad - rpad
            local pychar = pystr(char)

            return (pychar*lpad)..result..(pychar*rpad)
        end

        m.count = function(value, start, stop)
            value = pystr(value)

            start = start or 0
            stop = stop or m.len()

            start = pm.calc_key(start)
            stop  = pm.calc_key(stop)

            local count = 0
            local val_i = 0
            local i = 0
            local str = result[{start-1, stop-1}]

            while i <= stop-start-1 do
                if str[i] == value[val_i] then
                    val_i = val_i + 1
                end
                i = i + 1

                if val_i == value.len() then
                    count = count + 1
                    val_i = 0
                end
            end
            return count
        end

        m.encode = function(encoding, errors) error("Encoding not implemented") end

        m.endswith = function(value, start, stop)
            value = pystr(value)

            start = start or 0
            stop = stop or m.len()

            start = pm.calc_key(start)
            stop  = pm.calc_key(stop)

            -- if search boundary is less than value
            if stop - start < value.len() then return false end

            start = stop - value.len()

            local end_str = result[{start-1, stop-1}]
            return value == end_str
        end

        m.expandtabs = function(num)
            return pystr(string.gsub(result(), "\t", (pystr(" ")*num)()))
        end

        setmetatable(result, {
            __index = function(self, index)
                if type(index) == "string" then
                    return m[index]
                end
                return pm.index_access(index)
            end,

            __call = function(self, _)
                return self._data
            end,

            __add = function(self, v)
                return self._data..v
            end,

            __concat = function(self, v)
                if type(v) == "table" then
                    if v._is_str == true then
                        return pystr(self._data..v._data)
                    end
                    error("Concatenating table")
                elseif type(v) == "string" then
                    return pystr(self._data..v)
                elseif type(v) == "number" then
                    return pystr(self._data..v)
                end

            end,

            __mul = function(self, v)
                if type(v) == "number" then
                    local num = math.floor(v)

                    if num <= 0 then
                        return ""
                    end

                    return pystr(string.rep(self._data, num))
                end
                error("value not a number")
            end,

            __eq = function(self, v)
                return self() == pystr(v)()
            end,
        })

        return result
    end
})

a = pystr{"aBcDeFgH"}
print(a())
print(a[0](), a[1](), a[-1](), a[-2]())
print(a[{1, 5}](), a[{-5, -1}]())

print(a[{-1, -5, -2}]())
print(a[{1, 5, 2}]())
print(a[{1, 5}]())
print(a[{-5, -1}]())
print(a.capitalize()())
print(a.casefold()())
print(a.center(11, "0")())
print(a.count("cD"))

b = pystr{"ababacabad"}
print(b.count("aba"), b.count("ad"))

print(a.endswith("FgH"))
print(a.endswith("eFg", 2, -1))

b = pystr(a)
print(b())

a = pystr{"123"}
b = pystr{"123"}

print(a == b)

print(pystr{"a\tb\tc"}.expandtabs(5)())

return pystr