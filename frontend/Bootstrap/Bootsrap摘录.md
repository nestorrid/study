---
title: Bootstrap摘录
date: 2023-12-12 02:03:31 +08000
categories: [笔记, bootstrap]
tags: [frontend, bootstrap]
---

## 全局颜色主题

通过 `data-bs-theme` 属性来设置bootstrap的颜色模式, 可选值包括:

* light
* dark

当在html或body标签上设置该属性时便可以实现全局颜色模式切换.

## 比较有用的工具类

记录一下比较有用但有些偏门的工具类, 完整的工具类[在线文档](https://getbootstrap.com/docs/5.3/utilities/api/)

### Interaction

可以控制用户的交互方式, 控制用户能否选中文字内容, 通过 `user-select-*` 来控制文本选择方式.

* `user-select-all`: 点击文本时自动选中全部内容;
* `user-select-auto`: 默认方式, 根据用户拖动进行文本选择;
* `user-select-none`: 不能选中内部的文本;

### Flex

可以通过`d-flex`快速实现简单的流式布局. 基本的调整与`display:flex`方式相同, 均已`flex-*`开头的类来进行直接控制.

自动间距则可以快速的实现两侧布局, 通过在子元素上添加`.me-auto`或`.ms-auto`来实现.

可以使用`order-[0:5]`来改变子项的顺序.

```html
<div class="d-flex mb-3">
  <div class="p-2">Flex item</div>
  <div class="p-2">Flex item</div>
  <div class="p-2">Flex item</div>
</div>

<div class="d-flex mb-3">
  <div class="me-auto p-2">Flex item</div>
  <div class="p-2">Flex item</div>
  <div class="p-2">Flex item</div>
</div>

<div class="d-flex mb-3">
  <div class="p-2">Flex item</div>
  <div class="p-2">Flex item</div>
  <div class="ms-auto p-2">Flex item</div>
</div>
```

### position

css中position属性的工具类, 可以使用`translate-middle[-x|y]`来调整锚点.

```html
<div class="position-relative">
  <div class="position-absolute top-0 start-0 translate-middle"></div>
  <div class="position-absolute top-0 start-50 translate-middle"></div>
  <div class="position-absolute top-0 start-100 translate-middle"></div>
  <div class="position-absolute top-50 start-0 translate-middle"></div>
  <div class="position-absolute top-50 start-50 translate-middle"></div>
  <div class="position-absolute top-50 start-100 translate-middle"></div>
  <div class="position-absolute top-100 start-0 translate-middle"></div>
  <div class="position-absolute top-100 start-50 translate-middle"></div>
  <div class="position-absolute top-100 start-100 translate-middle"></div>
</div>
```

### clearfix

可以直接使用bs提供的`clearfix`类来清除内容的浮动属性以保持布局.

## sass自定义Bootstrap

Bootstrap变量都包含`!default`定义, 如果已经为某个变量设置了值, Bootstrap不会修改其值. 但修改变量需要提前引入`functions.scss`, 定义自定义变量之后在引入其他的sass文件.

官方给出的自定义示例:

```scss
// Required
@import "../node_modules/bootstrap/scss/functions";

// Default variable overrides
$body-bg: #000;
$body-color: #111;

// Required
@import "../node_modules/bootstrap/scss/variables";
@import "../node_modules/bootstrap/scss/variables-dark";
@import "../node_modules/bootstrap/scss/maps";
@import "../node_modules/bootstrap/scss/mixins";
@import "../node_modules/bootstrap/scss/root";

// Optional Bootstrap components here
@import "../node_modules/bootstrap/scss/reboot";
@import "../node_modules/bootstrap/scss/type";
// etc
```

### 添加自定义颜色

在对主题颜色添加新内容时, 需要新建一个`map`, 然后将该`map`合并到`$theme-colors`之中.

```css
// Create your own map
$custom-colors: (
  "custom-color": #900
);

// Merge the maps
$theme-colors: map-merge($theme-colors, $custom-colors);
```
