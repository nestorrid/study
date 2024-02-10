数据库操作
================================================

环境准备
------------------------------------------------

- 数据库驱动
    使用Flask链接MySQL需要安装对应的驱动程序.

    mysqlclient
        基于C语言编写, 执行效率高. 也是默认的数据库驱动, 在进行数据库URI配置时无需编写额外驱动信息.

        .. code-block:: bash
        
            pipenv install mysqlclient
        

        .. note:: mysqlclient 安装问题

            在使用pipenv安装mysqlclient时有可能会出现错误:

                RuntimeError: Failed to lock Pipfile.lock!
            
            该错误的原因是本机缺少一个依赖库`pkg-config`, 该库可以通过`apt-get`安装, 如果是Mac系统, 可以通过brew进行安装:

            .. code-block:: bash
                
                # Linux
                sudo apt-get install pkg-config

                # Mac OS
                # - Install brew
                /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
                
                # - install pkg-config use brew
                brew install pkg-config


        

    pymysql
        基于纯python编写, 与Python3.x无缝衔接, 兼容性更好.

        .. code-block:: bash
        
            pipenv install pymysql

        .. note:: 

            使用 `pymysql` 作为驱动时, 需要在URI中添加驱动信息: 

            `mysql+pymysql://scott:tiger@localhost/foo`
        

    两者选其一即可.

- orm 框架
    安装 `flask-sqlalchemy` 框架

    .. code-block:: bash
    
        pipenv install flask-sqlalchemy

- 数据库迁移工具
    安装 `flask-migrate`, 能够自动生成数据库的迁移脚本, 提供方便的数据库版本管理.

    .. code-block:: bash
    
        pipenv install flask-migrate