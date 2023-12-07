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


<style scoped></style>