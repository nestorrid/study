<template>
    <h1>属性绑定</h1>
    <p>{{ msg }}</p>
    <p>{{ num }}</p>
    <p>{{ myFunc() }}</p>
    <p>{{ isGood ? "Good" : "Emmm..." }}</p>
</template>

<script setup lang="ts">
let msg = "some text.";
let num = 10;
let isGood = true;

function myFunc() {
    return "my func called.";
}
</script>

<style></style>
