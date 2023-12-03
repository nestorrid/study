# vue3

MVVM架构

* model
* viewmodel
* view

## 环境搭建

* 安装[node.js](https://nodejs.org)
* 安装[nvm](https://github.com/nvm-sh/nvm)
  * 下载运行安装脚本

    ```bash
    wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash
    ```
  
  * 导出nvm环境变量
  
    ```bash
    export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
    ```

  * 验证安装

    ```bash
    nvm -v
    ```

## 通过Vite创建项目

通过Vite+Vue+TS构建项目.

```bash
npm init vite
cd [project_name]
npm install 
npm run dev
```

## vscode 必要插件

搜索`Volar`

* Vue Language Features (Volar)
* TypeScript Vue Plugin (Volar)
* Vue Volar extension Pack中有相关插件集合, 可以根据需要选装

