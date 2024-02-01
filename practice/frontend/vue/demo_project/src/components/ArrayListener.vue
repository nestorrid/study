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


<style scoped></style>