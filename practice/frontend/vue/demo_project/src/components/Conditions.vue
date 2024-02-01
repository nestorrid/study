<template>
    <h1>条件判断</h1>
    <div v-show="flag">你看不见我</div>
    <div v-if="flag">你能看见我吗?</div>
    <div v-if="age < 18">未成年</div>
    <div v-else>成年</div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

let flag = ref(true);
let age = 20;
</script>

<style lang="scss" scoped>
h1 {
    color: $color;
}
</style>
