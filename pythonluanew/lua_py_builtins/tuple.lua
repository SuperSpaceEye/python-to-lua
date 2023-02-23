tuple = {}
class = class or require("class")
list = list or require("list")

tuple = class(function(tuple)
    tuple.___name = "tuple"
    tuple.___left_bracket = "("
    tuple.___right_bracket = ")"
    tuple.___d = {}
    tuple.___size = 0

    function tuple.__init__(self, obj, straight_copy)
        self.___d = {}
        straight_copy = straight_copy or false

        if is_pyobj(obj) then
            if obj.___name == "tuple" then self = obj
            else
                local i
                for i, item in op_in(enumerate(obj)) do
                    self.___d[i+1] = item
                end
                self.___size = i
            end
        elseif type(obj) == "table" then
            if straight_copy then self.___d = obj; self.___size = #self.___d; return end
            local i = 1
            while obj[i] do
                self.___d[i] = obj[i]
                i = i + 1
            end
            self.___size = i-1
        end
    end

    function tuple.__setattr__(self, key, value)
        if type(key) == "string" and self[key] ~= nil then rawset(self, key, value) return end

        error("Tuple doesn't support item assignment")
    end

    function tuple.__add__(self, other)
        local copy = {}
        for i, item in op_in(enumerate(self)) do
            copy[i+1] = item
        end
        for i, item in op_in(enumerate(other)) do
            copy[i+1+self.__len__()] = item
        end
        return tuple(copy, true)
    end

    function tuple.__mul__(self, mul)
        if type(mul) ~= "number" then error("Not a number") end
        if mul <= 0 then return tuple() end

        local copy = {}

        for i in op_in(range(mul)) do
            for item in op_in(self) do
                copy[#copy+1] = item
            end
        end

        return tuple(copy, true)
    end

    tuple.append = nil
    tuple.extend = nil
    tuple.insert = nil
    tuple.remove = nil
    tuple.pop = nil
    tuple.clear = nil
    tuple.sort = nil
    tuple.reverse = nil
    tuple.copy = nil

    return tuple end, {list})


return tuple