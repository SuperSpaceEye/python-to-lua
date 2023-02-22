frozenset = {}
class = class or require("class")
pyobj = pyobj or require("pyobj")

frozenset = class(function(frozenset)
    frozenset.___name = "frozenset"

    function frozenset.__init__(self)
        error("Not implemented")
    end

    return frozenset
end, {pyobj})

return frozenset