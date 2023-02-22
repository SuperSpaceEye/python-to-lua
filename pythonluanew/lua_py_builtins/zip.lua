--TODO add error handling instead of nil checking
function zip(iter1, iter2)
    if is_pyobj(iter1) and is_pyobj(iter2) then
        iter1 = iter1.__iter__()
        iter2 = iter2.__iter__()

        local i = 0
        return function()
            local res1 = iter1.__next__()
            local res2 = iter2.__next__()

            if res1 == nil or res2 == nil then
                return nil
            end

            i = i + 1

            return res1, res2
        end
    end
end

return zip