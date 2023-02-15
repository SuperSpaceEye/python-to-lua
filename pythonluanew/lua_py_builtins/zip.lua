-- TODO
function zip(iter1, iter2)
    if type(iter1) == "table" and type(iter2) == "table" then
        local l1 = len(iter1)
        local l2 = len(iter2)
        local boundary = min(l1, l2)
        local i = 0

        return function()
            local res1 = iter1[i]
            local res2 = iter2[i]

            if res1 == nil or res2 == nil then
                return nil
            end

            i = i + 1

            return res1, res2
        end
    end
end