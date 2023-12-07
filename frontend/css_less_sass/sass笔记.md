---
title: sass预处理器笔记
date: 2023-12-06 13:54:12 +08000
categories: [笔记, css]
tags: [frontend, css, sass]
---

同样是css预处理器, css的超集. 可以使用变量, 函数, 继承, 模块化等编程范式, 似的css代码的可扩展性和可维护性增强. 通常来说sass文件有两种格式:

* `.sass`: 没有`{}`和`;`的语法
* `.scss`: 标准css语法

从功能上来讲两者没有任何区别, 使用何种格式皆可, 但是`scss`更为多见, 因为更贴近于css代码, 可阅读性更强.

[sass中文网](https://www.sass.hk)
[sass官网](https://sass-lang.com)

## 安装

sass是基于Ruby语言开发, 因此需要安装`Ruby`, mac自带Ruby所以不需要额外安装.

```bash
npm install -g sass
```

## 编译sass文件

浏览器无法直接使用`sass`或`scss`文件, 可以使用`Live Sass Compiler`插件来进行编译.

可以在插件配置中添加以下配置内容:

```json
{
    "liveSassCompile.settings.rootIsWorkspace": true,
    "liveSassCompile.settings.useNewCompiler": true,
    "liveSassCompile.settings.formats": [
        {
            "format": "compressed",
            "extensionName": ".min.css",
            "savePath": "~/../css", //sass文件当前路径的上一级路径下的css文件夹
            "savePathReplacementPairs": null
        }
    ],
    "liveSassCompile.settings.excludeList": [
        "/**/node_modules/**",
        "/.vscode/**"
    ],
    // 正常编译不会显示输出信息
    "liveSassCompile.settings.showOutputWindowOn": "Warning",
}
```

也可以使用`sass`自带的命令行工具进行sass的实时编译, 或者其他的编译工具, 如`考拉`, `node-sass`, `gulp`等, 根据实际需要选择即可.

## sass组件

官方命名为`Partials`, 以`_`开头的sass文件. 指包含部分sass内容, 会被其他文件应用, 但不需要单独进行编译. sass中文网翻译为...分音...本来挺好理解的概念让他整迷糊了. 还不如直接叫组件来的简单直接.

在使用组件文件时可以通过`@import`或者`@use`关键字.

```scss
/* _var.scss */
$color: red;
$bgColor: #1e1e1e;

/* main.scss */
@import "base/var";
@import "base/base";

body {
    background-color: $bgColor;
    color: $color;
}
```

在使用`@import`导入其他文件时可以省略`_`和扩展名, 如上述`base/var`文件的实际名称是`_var.scss`.

在导入多个文件时, 后倒入的文件可以使用先导入的文件中定义的内容.

即`_base.scss`文件内可以直接引用`_var.scss`文件中定义的变量. 基本的脚本从上而下的运行顺序.

### 常见的sass文件结构

为了使sass文件便于维护, 通常会根据功能不同将sass文件拆分为多个部分, 并最终组合到`index.scss`之中进行统一编译. 大体可以遵循`7-1`的模式:

* variables: 基础变量
* functions: 自定义函数
* base: 通用配置
* layout: 布局
* colors: 颜色
* components: UI组件
* utilities: 工具, 如margin, padding, opacity等.

也可以更具项目实际需求进行拆分.

## 变量

在sass中通过`$`定义变量:

```scss
$color: #1e1e1e;

div {
    color: $color;
}
```

## 嵌套语法

使用嵌套语法编辑html元素:

```html
<div class="card">
    <div class="card-title">This is a card</div>
    <div class="card-body">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia,
        saepe quis! <a href="#">Quas</a> non excepturi obcaecati
        quibusdam id molestiae perferendis suscipit.
    </div>
</div>
```

在队类似的嵌套html结构编写css是, 通常的代码如下:

```css
.card {}
.card .card-title {}
.card .card-title a {}
```

但是通过sass则可以更为简洁清晰的进行设置:

```scss
.card {
    max-width: 400px;
    border: $base-border;
    border-radius: $radius-md;
    padding: $base-padding;
    box-shadow: $base-shadow;
    color: white;

    &-title {
        font-size: $font-size-xxl;
        font-weight: bold;
        margin-bottom: $base-margin;
    }

    &-body {
        font-size: $font-size-lg;
        line-height: $base-line-height;

        a {
            color: $link-color;
            &:hover{
                color: mix($link-color, #ddd);;
            }
        }
    }
}
```

## 使用数学计算定义变量

以字体为例, 可以定义一个基础字体大小, 然后通过计算得到一组字体大小:

```scss
$base-font-size: 1rem;
$font-size-sm: $base-font-size * 0.75;
$font-size-lg: $base-font-size * 1.5;
$font-size-xl: $base-font-size * 2;
$font-size-xxl: $base-font-size * 3;
```

但是并非所有运算都可以直接进行, 比如除法运算, 需要使用sass内建的math库来进行计算

```scss
@use "sass:math";

$base-radius: 20px;
$radius-sm: math.div($base-radius, 4);
$radius-md: math.div($base-radius, 2);
```

数学运算和颜色运算等常用库详见文档:

* [sass:color](https://sass-lang.com/documentation/modules/color/)
* [sass:math](https://sass-lang.com/documentation/modules/math/)
* [其他内建模块](https://sass-lang.com/documentation/modules/)
* [菜鸟教程文档](https://www.runoob.com/sass/sass-functions.html)

## sass总结

作为非专业的css开发人员, 并不需要完全掌握sass, 毕竟很少需要自己从头到尾搭建一套css框架. 而是使用类似`Bootstrap`, `element-ui`, `ant-design`等框架.

熟练使用现有框架的基本功能, 同时能够根据需求进行自定义更为实际, 把大量的时间放在重复开发上没有什么意义.

基本够用的了解程度大致包括:

* 变量
* 嵌套语法
* mixin
* extend
* functions
* map
* @each, @if, @for
* @media
