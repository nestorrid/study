---
title: Vue响应式数据
date: 2023-12-05 16:13:34 +08000
categories: [笔记, vue]
tags: [frontend, vue]
---

通过`ref()`函数可以把任意类型的数据变为响应式数据.

响应式数据的本质就是在页面与数据之间进行双向绑定, 当数据发生变化时页面进行重新渲染, 而页面执行操作时数据同步变化.

```html
<script setup lang="ts">
import { ref } from 'vue';

const count = ref(0)
const random = ref(Math.random())

setInterval(() => {
    random.value = Math.random()
}, 1000)

</script>


<template>
    <p>Random value: {{ random }}</p>
    <button @click="count++">{{ count }}</button>
</template>


<style scoped></style>
```

> 通过`ref()`函数包裹的原始数据本质上已经变成了一个代理对象, 所有对其数据进行的修改都需要通过`.value`属性来完成.
>
> 但在模板中vue进行了优化, 可以直接对变量本身进行操作. 如上述代码的`@click="count++"`

## reactive和ref

除了ref, vue还提供了另外一个函数用来定义响应式数据, `reactive()`. 与`ref()`不同的是:

* reactive 只能作用于对象, 不能是基本类型的数据, 如number, bool, string等.
* reactive 是使目标对象直接变为响应式, 而不是封装到代理对象内, 也就不需要使用`.value`对原始值进行操作.

无论是reactive还是ref对象, 在进行解构后都会丢失响应式属性.

```html
<script setup lang="ts">
import { reactive, ref } from 'vue';

const activeUser = reactive({
    username: "张三",
    age: 20
})

const refUser = ref({
    username: "张三",
    age: 20
})

setInterval(() => {
    activeUser.age++
    refUser.value.age++
}, 1000)

const { username, age } = activeUser

</script>


<template>
    <div>active user:{{ activeUser }}</div>
    <div>ref user:{{ refUser }} </div>
    <div>{{ username }} {{ age }}</div>
</template>
```

## 获取响应式的解构成员

在处理复杂的响应式对象时可以通过`toRef()`方法来获取对象的特定成员, 并使其成为响应式对象.

所获取的响应式成员仍然属于源对象, 并且直接对其进行操作也会影响到原始对象.

```html
<script setup lang="ts">
import { reactive, ref, toRef } from 'vue';

const activeUser = reactive({
    username: "张三",
    age: 20
})

const refAge = toRef(activeUser, 'age')

setInterval(() => {
    refAge.value++
}, 1000)


</script>


<template>
    <div>active user:{{ activeUser }}</div>
    <div>ref age: {{ refAge }}</div>
</template>
```

同时, 也可以用`toRefs()`函数一次性解构对象的所有成员, 并通过`toRef`封装成员的值, 将所有成员的响应式对象打包成为一个普通对象.

```html
<script setup lang="ts">
import { reactive, toRefs, isProxy, isRef } from 'vue';


const user = reactive({
    username: '张三',
    age: 20
})

const userAsRefs = toRefs(user)

setInterval(() => {
    user.age++
    userAsRefs.age.value += 5
}, 1000)

</script>


<template>
    <div>{{ user }} </div>
    <div>user is proxy? {{ isProxy(user) }}</div>
    <div>user.username is proxy? {{ isProxy(user.username) }}</div>
    <div>user is ref? {{ isRef(user) }}</div>
    <div>user.username is ref? {{ isRef(user.username) }}</div>
    <hr>
    <div>{{ userAsRefs }}</div>
    <div>userAsRefs is proxy? {{ isProxy(userAsRefs) }}</div>
    <div>userAsRefs.username is proxy? {{ isProxy(userAsRefs.username) }}</div>
    <div>userAsRefs is ref? {{ isRef(userAsRefs) }}</div>
    <div>userAsRefs.username is ref? {{ isRef(userAsRefs.username) }}</div>
</template>
```

运行结果:

```text
{ "username": "张三", "age": 20 }
user is proxy? true
user.username is proxy? false
user is ref? false
user.username is ref? false
{ "username": "张三", "age": 20 }
userAsRefs is proxy? false
userAsRefs.username is proxy? false
userAsRefs is ref? false
userAsRefs.username is ref? true
```

## 浅层响应式对象

在使用`ref()`函数式, 创建的是深层响应式对象, 即原始对象的成员对象也会成为响应式对象. 但在处理大型的数据结构或对象时可能会出现效率问题.

而`shallowRef()`则是创建浅层响应式对象. 即只对`.value`属性指向的对象进行响应式处理, 对象内部成员的变化不会触发页面渲染, 仅当`.value`指向新的对象时才会重新渲染页面.

```html
<script setup lang="ts">
import { shallowRef } from 'vue';


const john = shallowRef({
    username: 'john',
    age: 20
})

const will = shallowRef({
    username: 'will',
    age: 20
})

setInterval(() => {
    john.value.age++
    will.value = {
        username: 'will',
        age: Math.random()
    }
}, 1000)
</script>


<template>
    <div>{{ john }}</div>
    <div>{{ will }}</div>
</template>


<style scoped></style>
```

> 在上面的例子中`john.value.age++`是对浅层响应式对象内部的成员进行修改, 虽然值改变了, 但是并不会引起页面渲染, 只是把值保存在了内存中.
>
> 而`will.value = {...}`则是直接让浅层响应式对象的`.value`指向了一个新的对象. 这一操作则会触发页面的更新. 而页面更新的同时由于`john`的内部成员数据也发生了改变, 所以更新时也会被一并更新.
>
{: .prompt-info}

