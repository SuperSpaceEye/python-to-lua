# from .translator import Translator
from pathlib import Path

def make_relative(dot_path:str):
    dot_path = ""+dot_path.replace(".", "/")
    Path(dot_path).parent.mkdir(parents=True, exist_ok=True)
    return dot_path+".lua"

def construct(source_path, output_path, translator):
    with open(source_path, mode="r") as file: py_code = file.read()
    lua_code = translator.translate(py_code)
    with open(make_relative(output_path), mode="w") as file: file.write(lua_code)