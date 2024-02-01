# 所需工具

```dash
    pip install setuptools wheel twine
```

# 管理依赖

# 添加Readme文件

添加文件`README.md`

# License选择

[协议下载网站 https://choosealicense.com](https://choosealicense.com)

# 打包

```python
# setup.py
from pathlib import Path
import setuptools

setuptools.setup(
        name="packagename",
        version=1.0,
        long_description=Path("README.md").read_text(encoding="utf-8"),
        packages=setuptools.find_packages(exclude=["directories", "you_dont_need"])
)
```

在终端执行打包命令:

```dash
python setup.py sdist bdist_wheel
```

# 上传

```dash
twine upload dist/*
```

这里需要提供[pypi.org](https://pypi.org)的用户名和密码

> 如果设置了二次验证,那么需要启动API Token来进行上传
> 用户名使用 `__token__`
>
> 密码是token值
> 也可以通过设置用户配置文件省略该步骤:

```dash
    vi ~/.pypirc
```

按照如下格式编辑配置文件:

```
[pypi]
username = __token__
password = your token 
```

保存退出后, 通过`twine`上传便不再需要填写用户名密码了