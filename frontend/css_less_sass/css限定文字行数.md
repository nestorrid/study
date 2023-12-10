---
title: css限定文字行数
date: 2023-12-10 03:03:48 +08000
categories: [速查, css]
tags: [frontend, css]
---

通过css限定元素内的文字显示行数, 并用`...`代替多余的内容.

```css
.desc {
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 3;
    overflow: hidden;
    text-overflow: ellipsis;
}
```
