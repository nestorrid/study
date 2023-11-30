# -*- coding=utf-8 -*-
#
# @Project      : python_basic
# @Author       : nestor
# @File         : use_sqlite.py
# @Date         : 2023/11/5 18:31
#
# @Description  :
#

import sqlite3
import json
from pathlib import Path

data = json.loads(Path("json_data.json").read_text())
print(data)


def write_to_database():
    with sqlite3.connect("db.sqlite") as conn:
        sql = "insert into t_data values (?,?,?)"
        for d in data:
            conn.execute(sql, tuple(d.values()))
        conn.commit()


def read_from_database():
    with sqlite3.connect("db.sqlite") as conn:
        sql = "select * from t_data"
        cursor = conn.execute(sql)
        for row in cursor:
            print(row)

        lines = cursor.fetchall()
        print(lines)


read_from_database()
