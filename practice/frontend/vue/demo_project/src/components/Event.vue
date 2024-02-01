<script setup lang="ts">
import { ref } from "vue";
const count = ref(0);

function clickHandler() {
    count.value += 1
}
</script>

<template>
    <h1>事件绑定</h1>
    <button @click="clickHandler">click count:{{ count }}</button>
    <button @click="count++">click count: {{ count }}</button>
</template>

<style scoped></style>
