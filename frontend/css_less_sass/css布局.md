---
title: css布局笔记
date: 2023-12-09 01:25:29 +08000
categories: [笔记, css]
tags: [frontend, css]
---

## css的盒子模型

在页面中, 每一个元素都被封装在一个盒子模型`box model`之中, 从外到内依次是:

* Margin
* Border
* Padding
* Content

默认情况下, 对元素大小的设置是对`content`的设置, 而添加边框则和内边距便会增加额外的尺寸.

可以通过`box-sizing`属性设定其尺寸的设置对象:

```css
.box {
    width: 100px;
    height: 100px;
    margin: 20px;
    padding: 8px;
    border: 5px solid red;
}
.box1 {
    box-sizing: content-box;
}

.box2 {
    box-sizing: border-box;
}
```

对于box1来说, 由于存在8px的内边距和5px的边框, 而尺寸是基于`content-box`来进行设置的, 最终的尺寸便是: `100 + 8*2 + 5*2 = 126px`.

而对于box2来说, 由于尺寸基于`border-box`来设置, 则最终尺寸就是固定的100px, 但由于存在边框和内边距, 最终`content-box`的尺寸则会对应的减小为: `100 - 8*2 - 5*2 = 74px`.

在页面中, 由于box1和box2两个元素相邻, 且同时设置了`margin`属性为`20px`, 则两个元素之间的间距便是20px, 而不是40px. 外边距属于两个元素的公共区域, 只要满足两边的要求即可, 相当于在多个边距属性中取最大值.  但是父元素的padding和子元素的margin在进行计算时会进行相加, 因为padding是包过`content`层的外部层, 而`margin`计算的是距离`content`层的边距.

通常来说, margin属性用于定义元素之间的间距, 相邻元素之间的margin会合并为一个. padding属性则是用来定义元素内容与边框之间的间距. 不同元素之间的padding相互独立, 不会被合并.

如果使用padding来调整元素间距, 当元素想临时便会出现额外距离的布局问题.

为了使所有页面元素都具有可以确定的几何尺寸, 可以通过通配符`*`设置所有元素的盒子尺寸为边框:

```css
*, *::before, *::after{
    box-sizing: border-box;
}
```

## 理解display属性

元素的`display`属性影响了元素在页面中的布局方式:

* block: 块元素, 每个元素占据完整的一行, 可以设置尺寸, 比如div, p等;
* inline: 行内元素, 行内元素不会主动换行, 当多个行内元素相连, 长度超过最大宽度时则会自动换行. 但行内元素自身没有宽高属性, 仅根据内容大小调整属性;
* inline-block: 行内块元素, 与行内元素唯一的区别就是具有宽高属性, 可以制定其几何大小;

## overflow属性

当内容超过元素的大小时通过`overflow`属性控制其显示方式:

* visible: 始终可见;
* hidden: 超出部分隐藏;
* scroll: 滚动条;
* auto: 仅当出现滚动内容时出现滚动条.

也可以使用`overflow-x`和`overflow-y`来分别设置x轴或y轴的滚动方式.

## css中的单位

绝对布局单位:

* px: 像素点;

在对某些与屏幕大小无关的属性进行设置时通常使用绝对单位, 比如边框粗细, 阴影属性等.

相对布局单位:

* %: 相对于父节点的百分比;
* vw: 视窗宽度, 如: 30vw代表视窗宽度的30%
* vh: 视窗高度;
* em: 相对字体大小;
* rem: 相对根字体大小;

默认情况下, 块元素的宽度为`100%`, 高度为`0`. 而`body`元素也是块元素, 所以默认大小便是0. 所以直接对页面内的元素设置`height`为100%本质上是继承了父元素的高度. 如果body本身没有内容, 则100%也同样是0.

> em和rem的区别:
>
> em是基于当前元素中`font-size`属性的大小进行计算, 如果没有设置则会根据继承属性进行计算. 也就可能会导致同样是`1em`在不同的元素中可能得到不同的大小.
> rem则是基于根元素(`:root`)的`font-size`属性的大小进行计算. 与所在元素无关, 默认情况下, 根元素字体大小为`16px`.
>
{: .prompt-info}

> 为了方便计算, 可以设置根元素字体大小为`62.5%`, 由于默认大小是16px, 设置后根元素字体大小便是`10px`. 此时无论在何处使用`1rem`均代表`10px`.
>
> ```css
> :root {
>   font-size: 62.5%;
> } 
> ```
>
{: .prompt-tip}

## position位置属性

通过`position`来调整元素的位置设置方式:

* static: 默认位置, 基于dom元素的默认布局放置, 无法设置位置属性left,right,top,bottom;
* relative: 相对位置, 指的是相对于自身原本所处的位置进行相对位移. 可以设置`top,left`或者`bottom, right`两组属性, 即在对应的方位添加指定的像素距离. 但是即便设置了位移属性, dom元素依然视其在原本的位置, 并不会影响其他元素的布局.
* absolute: 绝对位置, 会找到第一个`position:relative`的父元素, 并给予其位置进行绝对布局. 比如`body>div.container>div.content`, 当设置content位绝对布局是, 如果container是`position:relative`, 则会给予container进行绝对位置计算, 否则就会基于body进行计算. *设为绝对布局的元素不在dom布局中, 其他元素的位置布局不会参考绝对位置的元素.*
* fixed: 固定位置, 基于屏幕进行位置计算, 比附`left:0;bottom:0`, 始终位于屏幕的左下角. `fixed`元素同样不会再常规的页面布局流之中.

> postion属性也可以用来设置元素的尺寸, 比如同时设置元素的`left:10px;right:10px`, 在指定元素宽度的情况下不会有任何作用, 但是如果同时设置`width:auto;`则元素便会基于屏幕尺寸自动调整宽度.
>
{: .prompt-tip}

## float属性

float属性用于设置元素为浮动元素, 通常值包含`left`,`right`, 即浮动至左侧或右侧.

对于两个连续的`div`, 如果想要使其水平布局, 可以设置其为`float:left`. 但float属性可能会影响布局.

> float元素的高度对齐父元素不可见!!
>
{: .prompt-danger}

例如以下样式:

```html

<style>
    .container {
        margin: 20px;
        border: 2px solid lightskyblue;
    }

    .container div {
        width: 100px;
        height: 100px;
        margin: 10px;
        background-color: plum;
        float: left;
    }
</style>

<div class="container">
    <div class="box1"></div>
    <div class="box2"></div>
    <div class="box3"></div>
    <p>some test</p>
</div>
```

虽然3个子div都有尺寸, 但是由于设置了float属性, 所以父元素`container`在进行计算布局时不会考虑这3个div的高度. 也就仅仅只有`p`元素的高度.

为了解决`float`引起的布局问题, 需要使用`clear:both;`属性来清楚左右两侧的浮动信息. 为了不影响原始页面的结构, 通常会使用css伪类来在包含浮动内容的元素末尾添加一个空元素.

```css
 .clearfix::after {
    content: "";
    display: block;
    clear: both;
}
```

此时在`container`容器上添加`clearfix`类, 便可以正常的计算内容高度了.

float属性本身属于基本被淘汰的布局属性, 对于新项目而言, 应当使用flex或grid来对其进行布局.

## flexbox布局

将子元素进行水平或垂直布局. 通过设置`display`属性为`flex`即可. `flex`元素对于父元素而言, 布局方式与`block`一样, 同属于块元素, 仅仅只是调整了内部的子元素布局方式.

默认情况下为水平布局, 可以通过`flex-direction`设置布局方向, 包括:

* row:              水平;
* column:           垂直;
* row-reverse:      水平倒序;
* column-reverse:   垂直倒序;

> 在flex布局的情况下, 相邻元素之间的margin属性不会合并!
>
{: .prompt-tip}

通过`justify-content`属性来调整主轴的对齐方式, row则主轴为横轴;

常用属性包括:

* start, end, center;
* space-around: 每个元素的左右margin相等, 且相邻的margin不重叠;
* space-between: 在首尾元素的首尾边距根据子元素的样式设定, 额外空间均分在元素之间的间距上;
* space-evenly: 所有元素以及边框之间的距离相等.

通过`align-items`来调整交叉轴对齐方式, row则交叉轴位纵轴;

当flex容器内的子元素数量增加, 并且无法被单行容纳时, 子元素的宽度会被压缩, 以保证子元素始终保持在单行之内. 可以通过`flex-warp:warp;`属性设置为换行. 当元素过多时便会自动换行, 同时保持原有宽度不变.

在进行多行元素的交叉轴方向对齐时, 使用`align-content`属性, 用法与`justify-content`想同.

即在水平布局时, `justify-content`和`align-content`分别处理水平方向的多列或垂直方向的多行的对齐方式.

```html
<style>
    .container {
        display: flex;
        height: 300px;
        justify-content: center;
        align-content: center;
        flex-wrap: wrap;
    }
    .container div {
        width: 300px;
    }
</style>

<div class="container">
    <div>1</div>
    <div>2</div>
    <div>3</div>
    <div>3</div>
    <div>3</div>
    <div>3</div>
</div>
```

> 在flex容器只有单行的情况下, 可以在子元素中添加属性`align-self`来独立调整特定元素的布局方式.
>
{: .prompt-tip}

### 调整flex子元素的大小

可以通过三个属性来控制flex子元素的大小:

* flex-basis: 在主轴方向上的大小, 水平布局下会替换元素原有的width属性;
* flex-grow: 当主轴方向有额外的空间时是的变化方式, 默认为0, 即尺寸不变, 仅当值大于0时变化. 变化的算法是:
  > `当前元素宽度 = 额外空间 / 所有元素的flex-grow总和 * 当前元素的flex-grow值`;
  > 比如有3个元素的flex-grow分别是, 2,1,1; 额外的容器宽度为100px. 则第一个元素增加50px, 另外两个元素分别增加25px;
* flex-shrink: 主轴方向空间不足时的缩小方式. 默认为为1, 即等比缩小, 所有元素缩小相同尺寸. 如果设置为0, 则表示该元素在空间不足时尺寸不变. 数值越大, 缩小的比例越大.
* flex: 快捷属性, 可以同时设置上述三个属性.

## grid布局

类似于flex的布局属性, 容器对外依然是`block`类型, 对内部子元素进行网格布局. 通过设置`display:grid`属性开启网格布局.

```css
.container{
    display: grid;
    grid-template-columns: 100px 100px 100px;
    grid-template-rows: 100px 100px;
}
```

如果网格尺寸相同, 可以使用`repeat`函数来重构设置:

```css
grid-template-columns: repeat(3, 100px);
grid-template-rows: repeat(2, 100px);
```

可以使用快捷属性`grid-template`来同时设置行和列:

```css
grid-template: repeat(2,100px) / repeat(3, 100px);
```

### 网格内元素的布局方式

通过`justify-items`和`align-items`属性调节内部元素的布局方式, 默认情况下, 两个属性的值均为`stretch`拉伸, 在子元素的宽高属性为`auto`时会自动调整尺寸, 填满整个网格.

也可以使用其他属性, 如`start`, `end`, `center`等.

`justify-content`属性, 则是用来对`grid`容器的`content`盒进行水平布局. 属于盒子模型的内容, grid容器作为一个block类型的html元素, 同样包含`margin-border-padding-content`四个层, `content`便是最内层实际显示的内容. 容器本身占据100%的视图宽度, `justify-content:center`便是使容器内部元素整体水平居中.

同理, `align-content`属性则是调整容器整体内容的垂直方向布局. 在未设置容器高度的情况下, 容器的高度是基于内容的高度计算的, 属性也就没有作用.

### 网格布局的单位

网格的大小可以使用多种单位:

* px: 固定大小
* %: 相对于容器的百分比, 但是在网格布局中不常用, 因为参照系是父容器, 当内部发生变化时无法做出对应的调整
* auto: 根据网格内所显示的内容进行自动调整
* em,rem: 相对于字体的大小
* fr: 相对于剩余可用空间的大小, 计算方式与`flex-grow`的方式类似, 属于权重属性

```css
grid-template-columns: 150px 3fr 2fr auto;
```

在这条定义中, 网格布局被分为4列, 假设总宽度为1200px, 则最终会先计算第四列的宽度, 比如其内部包含一个100px的元素.

则已经使用的宽度便是`150px + 100px = 250px`

剩余宽度为`1200px - 250px = 950px`

中间两列一共为5fr, 则每个fr的宽度便是`950px / 5 = 190px`

最终得到第二列宽度为`570px`, 第三列宽度为`380px`;

### 网格间距

通过`gap`属性可以调整网格间距, 也可以通过`row-gap`和`column-gap`分别设置行与列间距.

在网格元素与容器之间不存在`gap`间距.

### 放置元素

默认情况下, grid容器会从上而下读取子元素, 然后从左到右依次放入每一行的网格中.

要设置某个具体的元素放置在哪个网格中, 需要在子元素中设置属性:

```css
grid-column: 1 / span 2;
grid-row: 1 / span 3;
```

`span n`代表跨n个网格.

为了使网格布局更容易维护, 可以通过`grid-template-areas`属性来为每个网格进行命名.

```css
grid-template-columns: repeat(2, 100px);
grid-template-rows: repeat(3, 100px);
grid-template-areas: 
    "header header" 
    "menu main" 
    "menu footer";
```

在这个三行两列的网格布局中, 第一行的两个网格都属于`header`, 第二行和第三行的第一列都属于`menu`, 第二行的第二列属于`main`, 第三行的第二列属于`footer`.

此时在子元素中便可以直接通过别名设置布局区域:

```css
grid-area: header;
```

> 在设置子元素的`grid-area`属性时不能使用字符串, 直接使用别名即可, 否则不会生效.
>
{: .prompt-tip}
