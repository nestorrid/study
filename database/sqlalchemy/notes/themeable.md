---
title: Typora Themeable
author: John Hildenbiddle
description: >
  A clean, customizable, typography-focused theme
  for the markdown editor Typora
---

# Typora Themeable

> # bookmark

> ## bookmark

> ### bookmark

> #### bookmark

> ##### bookmark
> 

> ###### bookmark

# Heading 1

Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes.

## Heading 2

Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes.

### Heading 3

Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes.

#### Heading 4

Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes.

##### Heading 5

Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes.

###### Heading 6

Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes.



> # Bookmark
>
> Asdfasdf

## Text Styles

Body text

*Italic text*

**Bold text**

~~Strikethrough~~

==Highlight text==

<u>Underline Text</u>

<pre>Preformatted text</pre>

<small>Small Text</small>

This is ^superscript^ text

This is ~subscript~ text

## Blockquotes

> Cras aliquet nulla quis metus tincidunt, sed placerat enim cursus. Etiam turpis nisl, posuere eu condimentum ut, interdum a risus. Sed non luctus mi. Quisque malesuada risus sit amet tortor aliquet, a posuere ex iaculis. Vivamus ultrices enim dui, eleifend porttitor elit aliquet sed.
>
> \- Quote Source

## Links

[Inline link](https://google.com "This is an optional title")

[Reference link][link1]

www.some-domain.com

person@email.com

[link1]: https://google.com "This an optional title"

## Lists

### Ordered

1. Ordered 1
1. Ordered 2
   1. Ordered 2a
   1. Ordered 2b
1. Ordered 3

### Unordered

- Unordered 1
- Unordered 2
  - Unordered 2a
  - Unordered 2b
- Unordered 3

## Task Lists

- [x] Task 1
- [ ] Task 2
  - [x] Subtask A
  - [x] Subtask B
- [x] Task 3

## Tables

| Left Align | Center Align | Right Align | Non&#8209;Breaking&nbsp;Header |
| :--------- | :----------: | ----------: | ------------------------------ |
| A1         |      A2      |          A3 | A4                             |
| B1         |      B2      |          B3 | B4                             |
| C1         |      C2      |          C3 | C4                             |

## Code

This is `inline code` and this is a [`linked inline code`](https://google.com).

```css
:root {
  --color-primary: var(--sky-600);
}

.my-class {
  margin: 1em;
  background: url('path/to/image.png');
}

@keyframes spinning {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
```

```javascript
// Mergician - https://jhildenbiddle.github.io/mergician/
import mergician from 'mergician';

const obj1 = { a: [1, 1], b: { c: 1, d: 1 } };
const obj2 = { a: [2, 2], b: { c: 2 } };
const obj3 = { e: 3 };

const mergedObj = mergician({
    skipKeys: ['d'],
    appendArrays: true,
    dedupArrays: true,
    filter({ depth, key, srcObj, srcVal, targetObj, targetVal }) {
        if (key === 'e') {
            targetObj['hello'] = 'world';
            return false;
        }
    }
})(obj1, obj2, obj3);

console.log(mergedObj);

// Output: { a: [1, 2], b: { c: 2 }, hello: 'world' }
```

```html
<!doctype html>
<html lang="">
<head>
  <meta charset="utf-8">
  <title>My Site</title>
  <meta name="description" content="My web site">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <div id="app">Loading...</p>
  <script src="js/app.js"></script>
</body>
</html>
```

## HTML

<p>
  This is an HTML block. Click to edit.
</p>
<!-- This is an HTML comment -->

<br>

## Horizontal Rule

---

## Footnotes

Lorem ipsum dolor sit amet [^footnote].

[^footnote]: This is a *footnote* with **bold text**.

## Keyboard

<kbd>a</kbd><kbd>b</kbd><kbd>c</kbd><kbd>1</kbd><kbd>2</kbd><kbd>3</kbd>

<kbd>F1</kbd><kbd>F2</kbd><kbd>F3</kbd>

<kbd>&#8984; Command</kbd><kbd>Z</kbd>

<kbd>&uarr;</kbd> Arrow Up

<kbd>&darr;</kbd> Arrow Down

<kbd>&larr;</kbd> Arrow Left

<kbd>&rarr;</kbd> Arrow Right

<kbd>&#8682;</kbd> Caps Lock

<kbd>&#8984;</kbd> Command

<kbd>&#8963;</kbd> Control

<kbd>&#9003;</kbd> Delete

<kbd>&#8998;</kbd> Delete (Forward)

<kbd>&#8600;</kbd> End

<kbd>&#8996;</kbd> Enter

<kbd>&#9099;</kbd> Escape

<kbd>&#8598;</kbd> Home

<kbd>&#8997;</kbd> Option / Alt

<kbd>&#8629;</kbd> Return

<kbd>&#8679;</kbd> Shift

<kbd>&#9251;</kbd> Space

<kbd>&#8677;</kbd> Tab

<kbd>&#8676;</kbd> Tab + Shift

## Images

### Inline

![alt text](https://source.unsplash.com/1600x900?nature "Provided by unsplash.com")

### Reference

![alt text][logo]

[logo]: https://source.unsplash.com/1600x900?animals "Provided by unsplash.com"

## Math

$$
\mathbf{V}_1 \times \mathbf{V}_2 =  \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
\frac{\partial X}{\partial u} &  \frac{\partial Y}{\partial u} & 0 \\
\frac{\partial X}{\partial v} &  \frac{\partial Y}{\partial v} & 0 \\
\end{vmatrix}
$$

## Diagrams

### Flow

```flow
st=>start: Start
op=>operation: Your Operation
cond=>condition: Yes or No?
e=>end

st->op->cond
cond(yes)->e
cond(no)->op
```

### Mermaid

#### Class Diagram

```mermaid
classDiagram
  Animal <|-- Duck
  Animal <|-- Fish
  Animal <|-- Zebra
  Animal : +int age
  Animal : +String gender
  Animal: +isMammal()
  Animal: +mate()
  class Duck{
    +String beakColor
    +swim()
    +quack()
  }
  class Fish{
    -int sizeInFeet
    -canEat()
  }
  class Zebra{
    +bool is_wild
    +run()
  }
```

#### Flowchart

```mermaid
graph TD;
A-->B;
A-->C;
B-->D;
C-->D;
```

#### GANNT

```mermaid
%% Example with slection of syntaxes
gantt
dateFormat  YYYY-MM-DD
title Sample GANTT Chart

section A section
Completed task:done,   des1, 2014-01-06,2014-01-08
Active task   :active, des2, 2014-01-09, 3d
Future task   :        des3, after des2, 5d
Future task2  :        des4, after des3, 5d

section Critical tasks
Completed task in the critical line:crit, done, 2014-01-06,24h
Implement parser and jison         :crit, done, after des1, 2d
Create tests for parser            :crit, active, 3d
Future task in critical line       :crit, 5d
Create tests for renderer          :2d
Add to mermaid                     :1d

section Documentation
Describe gantt syntax              :active, a1, after des1, 3d
Add gantt diagram to demo page     :after a1  , 20h
Add another diagram to demo page   :doc1, after a1  , 48h

section Last section
Describe gantt syntax              :after doc1, 3d
Add gantt diagram to demo page     : 20h
Add another diagram to demo page   : 48h
```

#### Pie Chart

```mermaid
pie title Chart Title
  "A" : 1
  "B" : 1
  "C" : 1
  "D" : 1
  "E" : 1
  "F" : 1
  "G" : 1
  "H" : 1
  "I" : 1
```

#### Sequence Diagram

```mermaid
sequenceDiagram
  participant A as Alice
  participant B as Bob
  A->>B: Hello John, how are you?
  Note right of B: Bob thinks
  B-->>A: I am good thanks
```

### Sequence

```sequence
Alice->Bob: Hello Bob, how are you?
Note right of Bob: Bob thinks
Bob-->Alice: I am good thanks
```

## Embeds

### Iframe

<iframe height='400' scrolling='no' title='CSS Device Frames - Demo' src='http://codepen.io/jhildenbiddle/embed/zYzmzqX/?theme-id=0&default-tab=result&embed-version=2' frameborder='no' allowtransparency='true'></iframe>

### Audio

<audio src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/123941/Yodel_Sound_Effect.mp3" />

### Video

<video src="http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4" />
