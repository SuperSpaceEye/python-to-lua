class = class or require("class")
pyobj = pyobj or require("pyobj")

float = class(function(float)
    float.___name = "float"

    function float.__init__(self)
        error("Not implemented")
    end

    return float
end, {pyobj})

return float