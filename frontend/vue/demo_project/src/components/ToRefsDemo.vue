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


<style scoped></style>