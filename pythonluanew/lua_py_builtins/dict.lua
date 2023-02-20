local dict = {}
package.loaded[...] = dict

local pyobj = require "pyobj"
local class = require "class"
local is_pyobj = (require "helper_functions").is_pyobj

dict = class(function(dict)
    dict.___name = "dict"
    dict.___d = {}

    function dict.__init__(self, obj)
        self.___d = {}

        if is_pyobj(obj) then

        elseif type(obj) == 'table' then

        end
        error("")
    end

    return dict
end, {pyobj})

return dict