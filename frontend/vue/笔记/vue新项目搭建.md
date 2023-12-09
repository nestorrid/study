---
title: vue新项目搭建
date: 2023-12-08 01:26:57 +08000
categories: [笔记, vue]
tags: [frontend, vue, vite]
---

## 使用vite创建项目

```bash
npm init vite@latest
```

根据提示执行操作:

1. 输入项目名称;
2. 选择框架: vue;
3. 选择语言: TypeScript;
4. 进入项目目录: ```cd project_name```;
5. 初始化安装: ```npm install```;

## 安装额外依赖

主要包括sass支持, 相关的类型依赖等基础内容:

```bash
npm install --save-dev sass @types/node
```

## 配置vite.config.js

1. 使`@`指向项目的`src目录`;
2. 添加全局sass文件导入;

```javascript
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

import path from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve:{
    alias:{
      '@': path.resolve(__dirname, './src'),
    }
  },
  css:{
    preprocessorOptions:{
      scss: {
        additionalData: `
          @import "@/style/_variables.scss";
          @import "@/style/_functions.scss";
          @import "@/style/_mixin.scss";
        `,
      }
    }
  }
})
```

> 通过`vite.config.js`进行全局导入的scss文件无需再通过`main.scss`导入便可以直接使用.
>
{: .prompt-tip}

## 添加vscode插件

* 路径提示插件: `Path Intellisense`, 添加vscode相关插件配置:

```json
{
    "path-intellisense.mappings": {
        "@": "${workspaceFolder}/src"
    },
}
```

* 添加sass变量扫描插件: `vue-scss-variable-scan`, 可以在vue文件中提示全局导入的变量名;
* sass智能提示插件: `SCSS IntelliSense`;

## 添加normalize.css

用于统一跨浏览器的视觉效果, 修正bug等.

下载[normalize.css](https://github.com/necolas/normalize.css/)文件, 并在`main.ts`中进行全局导入即可.
