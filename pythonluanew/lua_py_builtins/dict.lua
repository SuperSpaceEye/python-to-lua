dict = {}
require("pylua_init")
local is_pyobj = helper_functions.is_pyobj

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