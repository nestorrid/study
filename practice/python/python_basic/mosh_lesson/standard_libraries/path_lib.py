# -*- coding=utf-8 -*-
#
# @Project      : python_basic
# @Author       : nestor
# @File         : path_lib.py
# @Date         : 2023/11/5 17:46
#
# @Description  :
#

from pathlib import Path

p = Path.home()
print(p)
p = p / "Workspace"
print(p)
print(p.exists())
print(p.is_dir())
print(p.is_file())
print(p.name)
p = Path("path_lib.py")
print(p.name)  # path_lib.py
print(p.stem)  # path_lib
print(p.suffix)  # .py
print(p.parent)  # .
print(p.absolute())

p = Path()
print(p.absolute())

for sub in p.iterdir():
    print("sub:", sub)

p = Path("./test")
p.mkdir(exist_ok=True)
with open("./test/test.md", "w") as f:
    f.write("# test")

p = Path(".")
pys = [p for p in p.glob("*.py")]
print(pys)
pys = [p for p in p.glob("**/*.py")]
print(pys)
pys = [p for p in p.rglob("*.py")]
print(pys)
