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