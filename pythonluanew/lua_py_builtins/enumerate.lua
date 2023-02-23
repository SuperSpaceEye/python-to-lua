function enumerate(t, start)  end
helper_functions = helper_functions or require("helper_functions")
local is_pyobj = helper_functions.is_pyobj

--function enumerate(t, start)
--    start = start or 0
--
--    if t == nil then error("nil object")
--    elseif type(t) == "function" then
--        local i, v = start - 1, t()
--        return function()
--            local index, value = i, v
--            i, v = i+1, t()
--            if v == nil then
--                return nil
--            end
--
--            return index + start - 1, value
--        end
--    elseif is_pyobj(t) then
--        local iter = t.__iter__()
--        local i = -1
--        return function()
--            local val = iter.__next__()
--            i = i + 1
--            if val ~= nil then
--                return i + start - 1, val
--            else
--                return nil
--            end
--        end
--    end
--end

function enumerate(t, start)
    start = start or 0

    if t == nil then error("nil object")
    elseif type(t) == "function" then
        --local i, v = start - 1, t()
        local iter = iter_obj_creator()
        iter.i = start-1
        iter.v = t()
        iter.t = t
        iter.start = start

        iter.__next__ = function(self)
            local index, value = self.i, self.v
            self.i, self.v = self.i+1, self.t()
            if self.v == nil then
                return nil
            end

            return index + self.start - 1, value
        end

        return iter
    elseif is_pyobj(t) then
        local iter = iter_obj_creator()
        iter.t = t.__iter__()
        iter.i = 0
        iter.start = start
        iter.__next__ = function(self)
            local val = self.t.__next__(self.t)
            self.i = self.i + 1
            if val ~= nil then
                return self.i + self.start - 1, iterable_unpacker(val)
            else
                return nil
            end
        end

        return iter
    end
end

return enumerate