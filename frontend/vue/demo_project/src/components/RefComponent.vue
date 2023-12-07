<script setup lang="ts">
import { reactive, ref, toRef } from 'vue';

const count = ref(0)
const random = ref(Math.random())

const activeUser = reactive({
    username: "张三",
    age: 20
})

const refUser = ref({
    username: "张三",
    age: 20
})

setInterval(() => {
    random.value = Math.random()
    activeUser.age++
    refUser.value.age++
}, 1000)

const { username, age } = activeUser

const refAge = toRef(activeUser, 'age')

setInterval(() => {
    refAge.value++
}, 1000)

</script>


<template>
    <div>active user:{{ activeUser }}</div>
    <div>ref user:{{ refUser }} </div>
    <div>{{ username }} {{ age }}</div>
    <div>ref age: {{ refAge }}</div>
    <button @click="count++">{{ count }}</button>
</template>


<style scoped></style>