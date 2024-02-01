---
title: vue基础知识
date: 2023-12-05 16:14:41 +08000
categories: [笔记, vue]
tags: [frontend, vue]
---

Vue (发音为 /vjuː/，类似 view) 是一款用于构建用户界面的 JavaScript 框架。它基于标准 HTML、CSS 和 JavaScript 构建，并提供了一套声明式的、组件化的编程模型，帮助你高效地开发用户界面。无论是简单还是复杂的界面，Vue 都可以胜任。

[官方文档地址](https://cn.vuejs.org/guide/introduction.html)

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

## VUE 语法

在vue里使用文本插值语法, 官方叫做`mustache`语法.

Vue文件本身是一个完全符合html语言规范的文件, 其中包含三个核心部分, 即:

* script: js或ts代码.
* template: html模板
* style: 组件内样式定义.

```html
<template>

</template>

<script setup lang="ts">

</script>

<style>

</style>
```

### 模板语法

```html
<template>

    <p>{{ msg }}</p>
    <p>{{ num }}</p>
    <p>{{ myFunc() }}</p>
    <p>{{ isGood ? "Good" : "Emmm..." }}</p>

    <!-- 在{{}}中可以使用任何可以获得返回值的表达式, 或者调用有返回值的函数. 但是不能进行逻辑判断,循环等代码段的操作. -->
</template>

<script setup lang="ts">

let msg = 'some text.'
let num = 10
let isGood = true

function myFunc(){
    return 'my func called.'
}

</script>

<style>

</style>
```

其中`<script setup lang="ts">`为vue3的语法, 在vue2中需要通过`export default{}`导出一个js对象来对模板进行操作. 而vue3则可以直接将setup代码段看做一个独立的js模块来进行常规编码. 极大的提高了编码的便利性和可读性. 在vue的官方命名中分别将vue2和vue3的语法成为`选项是API`和`组合式API`.

### 属性绑定

在html标签的属性中不能通过`{{ }}`直接进行设置, 如果希望设定特定标签的属性, 需要通过属性绑定命令`v-bind:attr`来完成, 比如`v-bind:class`.

通常来说, `v-bind`关键字可以进行省略, 直接在常规属性前加上`:`即可变为绑定属性.

也可以通过`v-bind`来绑定一个对象, 一次性绑定多个属性.

```html
<template>
    <input type="text" 
        :name="txtName" 
        :id="txtId"  
        :disabled="isDisabled"
        :placeholder="placeholder"/>
    <button v-bind="attrs">{{ btnName }}</button>
</template>


<script setup lang="ts">

let txtName = 'textfield';
let txtId = '0';
let placeholder = 'input something...';
let isDisabled = false;

let btnName = 'Button';
let attrs = {
    id: "0",
    class: "btn"
}

</script>
```

### 条件渲染

通过html标签属性`v-if`,`v-else-if`,`v-else`来进行条件判断.

也可以通过属性`v-show`来控制元素是否被显示.

```html
<template>
    <div v-show="flag">你看不见我</div>
    <div v-if="flag">你能看见我吗?</div>
    <div v-if="age < 18">未成年</div>
    <div v-else>成年</div>
</template>

<script setup lang="ts">
let flag = true;
let age = 20;
</script>

<style></style>
```

> 通过`v-show`和`v-if`来控制显示的区别:
>
> * `v-show`: 始终会将元素渲染到dom对象中, 仅通过布尔值来控制是否显示, 在切换显示状态时具有更高的效率, 但在初始渲染时有额外开销;
> * `v-if`: 在条件为假时, 不做任何渲染, 初始渲染时有更高的效率, 但是对于频繁切换显示与隐藏的场景则会产生额外的开销.

### vue循环语法

通过`v-for`语句来进行循环操作.

```html
<script setup lang="ts">
let names = ["张三", "李四", "王五", "赵六"];
let items = [
    { id: "0", name: "张三", age: 15 },
    { id: "1", name: "李四", age: 17 },
    { id: "2", name: "王五", age: 19 },
];
</script>

<template>
    <h1>vue 循环</h1>
    <ul>
        <li v-for="name in names">{{ name }}</li>
    </ul>

    <ul>
        <li v-for="(item, index) in items" :id="item.id">
            {{ index + " " + item.name + " " + item.age }}
        </li>
    </ul>

    <ul>
        <li v-for="(item, index) in items">
            {{ index }}
            <ul>
                <li v-for="(value, key, index) in item">
                    {{ key + ": " + value + "-" + index }}
                </li>
            </ul>
        </li>
    </ul>
</template>

<style scoped></style>
```

> * 可以使用`for...in`循环, 也可以使用`for...of`循环, vue并不遵循js基本语法. 在底层进行了适配.
> * 在`v-for`语句的参数列表顺序是固定的, 即`(value,index)`, `(value,key,index)`

#### 通过key属性管理状态

本质是vue的diff算法的解决方案, 对于没有key属性元素, 在数据发生改变时无论变动内容是什么, 都会使用新的数据进行重新渲染.

比如: [1,2,3]变更为[1,3,2].

在变更前后仅有两个元素发生了顺序变动, 而dom内容本质上没有改变, 此时重新渲染就会消耗额外的性能.

而在添加key之后, 则是根据变动项进行渲染.

通常来说, 可以用数字或字符串来作为`:key`的值, 推荐使用数据对象的唯一id, 而不是数字索引来作为`:key`.

如果使用数字索引, 在插入新数据的时候同样有可能造成额外的性能消耗, 比如在头部插入新数据, 那么所有数据的索引都发生了改变, 也就相当于进行了整个内容的重新渲染. 而实际上其他数据并没有发生变化.

```html
<script setup lang="ts">
let names = ["张三", "李四", "王五", "赵六"];
let items = [
    { id: "0", name: "张三", age: 15 },
    { id: "1", name: "李四", age: 17 },
    { id: "2", name: "王五", age: 19 },
];
</script>

<template>
    <h1>vue 循环</h1>
    <ul>
        <li v-for="(name, index) in names" 
            :key="index">{{ name }}</li>
    </ul>

    <ul>
        <li v-for="(item, index) in items" :key="item.id">
            {{ index + " " + item.name + " " + item.age }}
        </li>
    </ul>
</template>
```

### 事件处理

通过vue指令`v-on:event`来绑定元素的事件, 比如`v-on:click`.

也可以将其简写成`@click`. 其值可以是内联的js语句, 也可以是函数.

```html
<script setup lang="ts">
import { ref } from "vue";
const count = ref(0);

function clickHandler() {
    count.value += 1
}
</script>

<template>
    <button @click="clickHandler">click count:{{ count }}</button>
    <button @click="count++">click count: {{ count }}</button>
</template>

<style scoped></style>
```

#### 事件传参

在绑定事件后可以向函数动态的传递参数

```html
<script setup lang="ts">
import { ref } from 'vue';

const names = ['accept', 'cancel']
const message = ref("")

function clickHandler(name: string): void {
    message.value = `clicked on ${name}`
}

function listObject(e: any) {
    let str = "";
    for (let key in e) {
        str += key + ": " + e[key] + '<br/>'
    }
    return str;
}

function withEvent(e: Event) {
    message.value = listObject(e)
}

function withArgsAndEvent(arg: string, event: Event) {
    message.value += arg + '<br/>' + listObject(event)
}

</script>


<template>
    <h1>事件传参</h1>
    <button v-for="name in names" @click="clickHandler(name)">{{ name }}</button>
    <br>
    <button @click="withEvent">event</button>
    <button @click="withArgsAndEvent('arg', $event)">args and event</button>
    <div v-html="message"></div>
</template>
```

#### 事件修饰符

vue可以在标签事件绑定时使用多种修饰符以进行多种额外操作, 比如阻止默认事件, 防止冒泡, 按键检测等等.

```html
<script setup lang="ts">
import { ref } from 'vue';


const message = ref("")

function divClick() {
    message.value += 'div clicked.<br/>';
}

function btnClick() {
    message.value += 'btn clicked.<br/>';
}

</script>


<template>
    <h1>事件修饰符</h1>
    <div @click="divClick">
        <button @click="btnClick">sample button</button>
    </div>
    <div @click.capture.stop="divClick">
        <button @click="btnClick">div captured</button>
    </div>
    <div @click="divClick">
        <button @click.stop="btnClick">button.stop</button>
    </div>
    <button @click="btnClick" @click.right.prevent>disable right click</button>
    <p v-html="message"></p>
</template>


<style scoped></style>
```

事件修饰符可以连用, 比如`@click.right.prevent`便是阻止了默认的右击事件.

`@click.right.capture.prevent`则可以阻止所有子元素的右键点击事件.

常用的事件修饰符包括:

* .stop - 阻止事件传递
* .prevent - 阻止默认事件
* .capture - 事件捕获, 在子元素处理事件前先由父元素处理
* .self - 只监听触发该元素的事件
* .once - 只触发一次
* .left - 左键事件
* .right - 右键事件
* .middle - 中间滚轮事件

完整的事件修饰符说明详见[文档](https://cn.vuejs.org/guide/essentials/event-handling.html#event-modifiers)

### 检测数据源变化

vue会自动检测响应式数据源的变化, 并在发生变化时重新渲染界面.

```html
<script setup lang="ts">
import { ref } from 'vue';

const arr = ref([1, 2, 3, 4, 5])

function addNum() {
    arr.value.push(10)
    arr.value.concat([1, 2, 3])
    console.log('add')
}

</script>


<template>
    <h1>监听数组变化</h1>
    <div>
        <span v-for="(item, index) in arr" :key="index">{{ item }}</span>
    </div>
    <button @click="addNum">Add</button>
</template>
```

> 由于`push`方法是向数组中添加新元素, 使原始数组发生了变动, 所以会触发UI更新
> 但`concat`方法只是读取了数组数据, 并将其与其他数组合并产生一个新的数组. 原始数组本身并没有发生变换, 所以UI不会因为`concat`方法而更新.

### 计算属性

当`{{ }}`表达式中包含多种逻辑时, 比如三元运算符等. 可以使用计算属性来对这些逻辑进行封装. 在使模板内容更加清晰的同时还可以进行性能提升.

```html
<script setup lang="ts">
import { computed, ref } from 'vue';

const arr = ref([1, 2, 3, 4, 5])

const sum = computed(() => {
    return arr.value.reduce((a, n) => a + n)
})

function addNumToArray() {
    let num = Math.round(Math.random() * 100)
    arr.value.push(num)
}

</script>


<template>
    <h1>计算属性</h1>
    <div><span v-for="(num, index) in arr" :key="index">{{ num + ' ' }}</span></div>
    <button @click="addNumToArray">Add num</button>
    <div>{{ sum }}</div>
</template>


<style scoped></style>
```

> 计算属性本身也是一个js函数, 但是在实现上进行了优化. 在数据源没有发生变化的情况下计算属性会对结果进行缓存, 多次读取仅进行一次计算, 仅在数据源更新时才会进行重新计算.
>
> 而函数则是每次调用都会进行计算.

### 样式绑定

与属性绑定不同, vue对元素的样式绑定进行了增强. 除了绑定具体的值之外, 还可以绑定对象或者数组.

```html
<script setup lang="ts">
import { ref } from 'vue';

const message = "Lorem ipsum dolor sit amet."

const style = ref({
    active: true,
    dark: true
})

function toggleStyle() {
    style.value.active = !style.value.active
    style.value.dark = !style.value.dark
}

</script>


<template>
    <h1>样式绑定</h1>
    <div :class="style">{{ message }}</div>

    <button @click="toggleStyle">Toggle Style</button>
</template>


<style scoped>
.active {
    font-size: 3rem;
}

.dark {
    color: darkred;
}
</style>
```

> 当同一个样式在页面中被多次使用时也可以通过计算属性获得样式.
>
> 除了可以通过`:class`进行css类绑定之外, 也可以通过`:style`来进行内联样式绑定, 语法基本类似, 详情可以查看[文档](https://cn.vuejs.org/guide/essentials/class-and-style.html#binding-inline-styles)

### 侦听器

侦听器用于处理响应式对象发生变动时的对应操作. 比如在修改文本框内容时, 根据文本框的内容向服务器发送异步请求. 而获得请求结果则需要一定的等待时间.

```html
<script setup lang="ts">
import { ref, watch } from 'vue'

const question = ref('')
const answer = ref('Questions usually contain a question mark. ;-)')
const img = ref(null)

// 可以直接侦听一个 ref
watch(question, async (newQuestion) => {
    if (newQuestion.indexOf('?') > -1) {
        answer.value = 'Thinking...'
        try {
            const res = await fetch('https://yesno.wtf/api')
            const json = (await res.json())
            answer.value = json.answer
            img.value = json.image

        } catch (error) {
            answer.value = 'Error! Could not reach the API. ' + error
        }
    }
})
</script>

<template>
    <p>
        Ask a yes/no question:
        <input v-model="question" />
    </p>
    <img v-if="img" :src="img" style="{width: 400;}" alt="answer" />
    <p>{{ answer }}</p>
</template>
```

### 输入绑定

通过`v-mode`命令可以将各种`input`元素与数据源进行双向绑定. 一方发生改变时另一方同步发生改变.

```html
<script setup lang="ts">
import { ref } from 'vue';

const inputText = ref("")
const checked = ref(false)
const options = ["A", "B", "C", "D"]
const checkedOptions = ref([])
const picked = ref(null)
const selected = ref(null)

</script>


<template>
    <h1>表单输入绑定</h1>
    <div class="container">
        <div>input text:{{ inputText }}</div>
        <div><input type="text" v-model="inputText"></div>
    </div>
    <div class="container">
        <div>{{ checked }}</div>
        <input type="checkbox" id="checkbox" v-model="checked">
        <label for="checkbox">选项框</label>
    </div>
    <div class="container">
        <div>多选结果:{{ checkedOptions }}</div>
        <span v-for="(item, index) in options" :key="index">
            <input type="checkbox" :id="'option' + index" v-model="checkedOptions" :value="item">
            <label :for="'option' + index">{{ item }}</label>
        </span>
    </div>
    <div class="container">
        <div>单选结果: {{ picked }}</div>
        <span v-for="(item, index) in options" :key="index">
            <input type="radio" :id="'radio' + index" :value="item" v-model="picked">
            <label :for="'radio' + index">{{ item }}</label>
        </span>
    </div>
    <div class="container">
        <div>下拉列表: {{ selected }} </div>
        <select v-model="selected">
            <option disabled value="">select one</option>
            <option v-for="(item, index) in options" :value="item" :key="index">{{ item }}</option>
        </select>
    </div>
</template>


<style scoped>
.container {
    margin-bottom: 1.5rem;
}
</style>
```
