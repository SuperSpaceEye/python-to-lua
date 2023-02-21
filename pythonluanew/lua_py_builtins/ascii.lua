function ascii()  end
require("pylua_init")

function ascii(item)
    if not is_pyobj(item) then error("Not a pyobj") end

    local repr = item.__repr__()
    local escape_sequences = list({"\a", "\b", "\f", "\n", "\r", "\t", "\t", "\v", "\v", "\\", "\"", "\'"})
    local replacement_str  = list({"\\a", "\\b", "\\f", "\\n", "\\r", "\\t", "\\t", "\\v", "\\v", "\\\\", "\\\"", "\\'"})

    for escape, replacement in op_in(zip(escape_sequences, replacement_str)) do
        repr = repr.replace(escape, replacement)
    end

    return repr
end

return ascii