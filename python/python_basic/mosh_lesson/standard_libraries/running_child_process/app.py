# -*- coding=utf-8 -*-
#
# @Project      : python_basic
# @Author       : nestor
# @File         : app.py
# @Date         : 2023/11/5 20:04
#
# @Description  :
#

import subprocess

result = subprocess.run(['python', 'child.py'],
                        capture_output=True,
                        text=True)
print(result)
print(result.args)
print(result.returncode)
print(result.stderr)
print(result.stdout)
