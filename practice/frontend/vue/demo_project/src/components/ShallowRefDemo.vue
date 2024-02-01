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


<style scoped lang="scss"></style>