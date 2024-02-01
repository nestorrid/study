# -*- coding=utf-8 -*-
#
# @Project      : python_basic
# @Author       : nestor
# @File         : zip_files.py
# @Date         : 2023/11/5 18:07
#
# @Description  :
#

from pathlib import Path
from zipfile import ZipFile

with ZipFile("file.zip", "w") as zip:
    for p in Path("test").rglob("*.*"):
        zip.write(p)

with ZipFile("file.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("test/test.md")
    print(info)
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("extract")
