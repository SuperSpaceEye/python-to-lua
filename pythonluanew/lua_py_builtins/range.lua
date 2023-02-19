local pyobj = pyobj or require "pyobj"
local str = str or require "str"
local pytype = pytype or require "type"
local iter_obj_creator = iter_obj_creator or require "iter_obj_creator"
local class = class or require "class"

local range = class(function(range)
    range.___name = "range"

    function range.__init__(self, start, stop, step)
        if start == nil then error("") end
        if stop == nil then stop = start; start = 0 end
        if step == nil then step = 1 end
        -- TODO check for __index__
        if math.floor(step) ~= start then error("start should be integer") end
        if math.floor(step) ~= stop then error("stop should be integer") end
        if math.floor(step) ~= step then error("step should be integer") end
        if step == 0 then error("step can't be 0") end

        self.start = start
        self.stop = stop
        self.step = step
        self.___length = math.abs((stop - start) / step)
        if math.floor(self.___length) ~= self.___length then self.___length = self.___length + 1 end
        self.___length = math.floor(self.___length)
    end

    function range.__iter__(self)
        local iter = iter_obj_creator()
        iter.pos = self.start
        iter.stop = self.stop
        iter.step = self.step
        iter.__next__ = function(self)
            local pos = self.pos
            if self.step > 0 then
                if self.pos >= self.stop then return nil end
            else
                if self.pos <= self.stop then return nil end
            end
            self.pos = self.pos + self.step
            return pos
        end
        return iter
    end

    function range.__eq__(self, other)
        if pytype(self) ~= pytype(other) then return false end

        --https://stackoverflow.com/questions/35004162/why-is-range0-range2-2-2-true-in-python-3
        if rawequal(self, other) then return true end
        if self.___length ~= other.___length then return false end
        if self.___length == 0 then return true end
        if self.start ~= other.start then return false end
        if self.___length == 1 then return true end
        return self.step == other.step
    end

    function range.__contains__(self, num)
        if type(num) ~= "number" then return false end
        return num >= self.start and num < self.stop and (num - self.start) % self.step == 0
    end

    function range.__repr__(self)
        local s = "range("..self.start..", "..self.stop
        if self.step ~= 1 then s = s..", "..self.step end
        return str(s..")")
    end

    function range.count(self, num) if self.__contains__(num) then return 1 else return 0 end end

    function range.index(self, num)
        if not self.__contains__(num) then error(num.." is not in range") end
        return math.floor((num - self.start) / self.step)
    end

    return range
end, {pyobj})

return range