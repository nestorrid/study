---
title: css预处理器-less基础
date: 2023-12-05 21:24:00 +08000
categories: [笔记, css]
tags: [frontend, css, less]
---

预处理器是对css的扩展, 使其可以使用变量, 循环, 继承, 自定义方法等特性. 以提高原生css的可维护性和开发效率. 主流的预处理器包括`less`和`sass`等.

## [less](https://lesscss.org) | [less中文网](https://lesscss.cn/)

安装:

```bash
npm install -g less
```

推荐vs扩展: `Easy LESS`

### 注释

在`.less`文件中可以使用两种注释:

* `//` 不会出现在便后的css文件中
* `/*...*/` 会出现在编译后的css文件中

### 使用less变量

通过`@arg-name`声明一个变量, 可以在任意位置使用. 变量可以是选择器变量, 属性变量, url变量等.

#### 选择器变量

与一般变量的语法相同, 但是值是css选择器, 才使用时需要通过`@{name}`进行调用

```css
@target: wrap;

#@{target} {
    width: @width;
    height: @height;
}
```

#### 属性变量

```css
@bg-color: lightgray;
@bg: background-color;

body {
    @{bg}: @bg-color;
}
```

#### url变量

```css
@base-image-url: "../img";

#@{target} {
    background-image: url("@{base-image-url}/test.png");
}
```

#### 声明变量

类似于css函数, 将一组css属性进行整体封装. 通过`@name: {...}`进行声明, 通过`@name()`进行调用.

```css
@bg-color: #1E2A3B;
@theme: {
    background-color: @bg-color;
    color: @color;
}

body {
    @theme();
}
```

#### 变量运算

已经定义的变量可以进行数学运算.

```css
@theme: {
    background-color: @bg-color - #111;
    color: @color;
    width: @width - 10;
    height: @height - 10;
    margin: auto;
}
```

#### 用变量定义变量

可以使用一个变量的名字作为另一个变量的值, 比如`@arg: "other"`, 在使用`arg`变量的时候就可以通过两个`@`读取到`other`变量的值.

```css
@light-bg-color: white;
@dark-bg-color: #1E2A3B;

@current-theme: "light";

@theme-bg-color: %("%s-bg-color", @current-theme);

.box {
    background-color: @@theme-bg-color;
    width: 100px;
    height: 100px;
}
```

### less嵌套

主要用来处理html元素的嵌套. 假设html的层级结构如下:

```html
        <div id="wrap">
            <div class="box">box</div>
            <div class="content">
                <div class="element">
                    <ul>
                        <li>a</li>
                        <li>b</li>
                        <li>c</li>
                    </ul>
                    <ol>
                        <li>1</li>
                        <li>2</li>
                        <li>3</li>
                    </ol>
                </div>
            </div>
        </div>
```

则可以通过less嵌套对wrap下的所有元素进行统一的样式设置:

```css
@bg-color: #1E2A3B;

body {
    background-color: @bg-color;
    color: white;
}

#wrap {
    background-color: @bg-color - #111;
    color: white;
    width: 800px;
    height: 600px;

    &:hover {
        background-color: @bg-color + #111;
    }

    .box {
        background-color: deeppink;
        width: 100%;
        height: 100px;
        margin: 0;
    }

    .content {
        background-color: deepskyblue;

        .element {
            padding: 15px 0;

            ul {
                color: red;
                margin-top: 0;
            }

            ol {
                color: green;
                margin-top: 0;
            }
        }
    }
}
```

> **&的用法**
>
> 在进行嵌套时, 内部的选择器会与外层选择器之间存在一个空格. 如`#wrap{ .box{}}`就会被解析成:`#warp{}`和`#warp .box{}`, 但是对伪类或伪元素(pseudo-class/element)即`:`和`::`的样式进行定义式, 额外的空格便会时选择器失效.
>
> 此时通过`&`链接伪选择器, 便可以解决问题, 即`#wrap{ &:hover{}}`解析后得到便是`#wrap:hover{}`.
>
{: .prompt-tip}
