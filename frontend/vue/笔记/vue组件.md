---
title: vue组件
date: 2023-12-05 16:14:19 +08000
categories: [笔记, vue]
tags: [frontend, vue]
---

当使用构建步骤时，我们一般会将 Vue 组件定义在一个单独的 .vue 文件中，这被叫做单文件组件 (简称 SFC).

通常一个vue文件包含`template`, `script`, `style`三个部分.

```html
<script setup>
import { ref } from 'vue'

const count = ref(0)
</script>

<template>
  <button @click="count++">You clicked me {{ count }} times.</button>
</template>

<style scoped></style>
```

`scoped`关键字作用是限定样式的作用域, 使其仅在当前组件内部生效.

## 使用组件

在父组件中导入vue文件并通过标签直接使用即可.

```html
<script setup lang="ts">
import InputBindVue from './components/InputBind.vue';
</script>

<template>
  <InputBindVue></InputBindVue>
  <InputBindVue />
</template>


<style scoped></style>
```

## 注册全局组件

可以在项目生成的`main.ts`文件中进行全局组件的配置

```typescript
import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

import HeaderVue from './components/Header.vue'

const app = createApp(App)

app.component('header', HeaderVue)
app.mount('#app')
```

全局注册的组件可以在彼此之间相互调用, 但在使用方便的同时也会带来一些副作用:

* 没有被使用的全局注册组件不会再打包时移除
* 组件之间的依赖关系会变得混乱.

因此应当尽可能少的注册全局组件, 可以考虑对大量重用的基础组件进行全局注册, 比如自定义的Button, Input等元素. 或者所有页面的公共部分, 比如Header, Footer, Menu等.

## 组件的数据传递

不同的组件之间可以相互传递数据, 父组件可以向子组件传递数据, 但是子组件不能像父组件传递数据.

```html
<!-- child -->
<script setup lang="ts">

const props = defineProps({
    title: String,
    message: String
})

</script>


<template>
    <h1>组件数据传递</h1>
    <h3>{{ props.title }}</h3>
    <div>{{ props.message }}</div>
</template>
```

```html
<!-- parent -->
<script setup lang="ts">
import { ref } from 'vue';
import PropsDemoVue from './components/PropsDemo.vue';

const message = ref("")
const title = ref("")

</script>


<template>
  <div>
    <input type="text" v-model="title">
  </div>
  <div>
    <input type="text" v-model="message">
  </div>

  <PropsDemoVue :title="title" :message="message"></PropsDemoVue>
</template>


<style scoped></style>
```

在传递多个参数时可以直接将所有参数打包成一个对象, 然后通过`v-bind`命令一次性传递

```html
<script>
    const post = {
    id: 1,
    title: 'My Journey with Vue'
    }
</script>

<template>
    <BlogPost v-bind="post" />    
</template>
```

> * 所有的props默认都是可选的, 除非显示的声明其为`required: true`.
> * 当没有接受到参数时, 默认为`undefined`, 但Boolean类型的参数则是`false`.

### typescript的参数传递优化

虽然使用typescript可以兼容js传参语法, 但是typescript本身对于类型的限制更加严谨, 同时有更好的编译提示.

比如如下代码:

```html
<script setup lang="ts">
    const props = defineProps({
    foo: { type: String, required: true },
    bar: Number
    })

    props.foo // string
    props.bar // number | undefined
</script>
```

而在typescript中, 则可以将参数类型封装成接口, 并通过范型的形式进行声明.

```html
<script setup lang="ts">
    interface Props {
    foo: string
    bar?: number
    }

    const props = defineProps<Props>()
</script>
```

但是通过定义接口类型来声明参数会失去设置默认值的能力. 可以通过`withDefaults`宏来解决.

```html
<script>
    interface Props {
    msg?: string
    labels?: string[]
    }

    const props = withDefaults(defineProps<Props>(), {
    msg: 'hello',
    labels: () => ['one', 'two']
    })
</script>
```
