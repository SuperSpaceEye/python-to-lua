function len(item)
    if type(item) == "string" then
        return string.len(item)
    end
    if type(item) == "table" then
        if item._is_list == true then

        elseif item._is_dict == true then

        elseif item._is_str then

        else
            return #item
        end
    end
end