frozenset = {}
require("pylua_init")

frozenset = class(function(frozenset)
    frozenset.___name = "frozenset"

    function frozenset.__init__(self)
        error("Not implemented")
    end

    return frozenset
end, {pyobj})

return frozenset