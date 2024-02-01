<script setup lang="ts">
import { ref } from 'vue';

const message = "Lorem ipsum dolor sit amet."

const style = ref({
    active: true,
    dark: true
})

function toggleStyle() {
    style.value.active = !style.value.active
    style.value.dark = !style.value.dark
}

</script>


<template>
    <h1>样式绑定</h1>
    <div :class="style">{{ message }}</div>

    <button @click="toggleStyle">Toggle Style</button>
</template>


<style scoped>
.active {
    font-size: 3rem;
}

.dark {
    color: darkred;
}
</style>