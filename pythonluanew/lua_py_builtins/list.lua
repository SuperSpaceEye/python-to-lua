list = {}
setmetatable(list, {
    __call = function(_, t)
        local result = {}

        result._is_list = true

        result._data = {}
        for _, v in ipairs(t) do
            table.insert(result._data, v)
        end

        local methods = {}

        methods.append = function(value)
            table.insert(result._data, value)
        end

        methods.extend = function(iterable)
            for value in iterable do
                table.insert(result._data, value)
            end
        end

        methods.insert = function(index, value)
            table.insert(result._data, index, value)
        end

        methods.remove = function(value)
            for i, v in ipairs(result._data) do
                if value == v then
                    table.remove(result._data, i)
                    break
                end
            end
        end

        methods.pop = function(index)
            index = index or #result._data
            local value = result._data[index]
            table.remove(result._data, index)
            return value
        end

        methods.clear = function()
            result._data = {}
        end

        methods.index = function(value, start, end_)
            start = start or 1
            end_ = end_ or #result._data

            for i = start, end_, 1 do
                if result._data[i] == value then
                    return i
                end
            end

            return nil
        end

        methods.count = function(value)
            local cnt = 0
            for _, v in ipairs(result._data) do
                if v == value then
                    cnt = cnt + 1
                end
            end

            return cnt
        end

        methods.sort = function(key, reverse)
            key = key or nil
            reverse = reverse or false

            table.sort(result._data, function(a, b)
                if reverse then
                    return a < b
                end

                return a > b
            end)
        end

        methods.reverse = function()
            local new_data = {}
            for i = #result._data, 1, -1 do
                table.insert(new_data, result._data[i])
            end

            result._data = new_data
        end

        methods.copy = function()
            return list(result._data)
        end

        local iterator_index = nil

        setmetatable(result, {
            __index = function(self, index)
                if type(index) == "number" then
                    if index < 0 then
                        index = #result._data + index
                    end
                    return rawget(result._data, index + 1)
                end

                return methods[index]
            end,
            __newindex = function(self, index, value)
                result._data[index] = value
            end,
            __call = function(self, _, idx)
                if idx == nil and iterator_index ~= nil then
                    iterator_index = nil
                end

                local v = nil
                iterator_index, v = next(result._data, iterator_index)

                return v
            end,
        })

        return result
    end,
})