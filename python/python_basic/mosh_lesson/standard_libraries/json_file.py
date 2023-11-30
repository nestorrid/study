# -*- coding=utf-8 -*-
#
# @Project      : python_basic
# @Author       : nestor
# @File         : json_file.py
# @Date         : 2023/11/5 18:25
#
# @Description  :
#

import json
from pathlib import Path

data = [
    {"id": 1, "title": "test 1", "year": 2000},
    {"id": 2, "title": "test 2", "year": 2001}
]

jdata = json.dumps(data)
Path("json_data.json").write_text(jdata)

data = Path("json_data.json").read_text()
j = json.loads(data)
print(j)
