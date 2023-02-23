# from .translator import Translator
from pathlib import Path

def make_relative(dot_path:str):
    dot_path = ""+dot_path.replace(".", "/")
    return dot_path

def construct(source_path, output_path, translator, minify=False):
    with open(source_path, mode="r") as file: py_code = file.read()
    translator.config.src_filename=Path(source_path).name.split(".")[0]
    lua_code = translator.translate(py_code)
    if minify:
        import js2py
        context = js2py.EvalJs(enable_require=True)

        with open("luamin_/luamin.js", mode="r") as file:
            jscript = file.read()

        context.execute(jscript)
        lua_code = context.luamin.minify(lua_code)
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path+".lua", mode="w") as file: file.write(lua_code)