local None = {}
package.loaded[...] = None
local class = require "class"
local pyobj = require "pyobj"
local str = require "str"

None = class(function(None)
    None.___name = "NoneType"
    function None.__setattr__(self, key, value) end
    function None.__str__(self) return str("None") end
    function None.__eq__(other) return other.___name == "None" end
    function None.__init__(self) error("None can't have an instance") end

    return None
end, {pyobj})

return None