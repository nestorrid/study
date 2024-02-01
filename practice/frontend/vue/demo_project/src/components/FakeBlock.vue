<script setup lang="ts">
import { ref } from 'vue';

const message = ref("some text")

function clickHandler() {
    message.value = "new text"
    const start = Date.now()
    while (Date.now() - start < 3000) { }
}

setTimeout(() => {
    console.log(1)
}, 0);

Promise.resolve().then(() => {
    console.log(2);
})

console.log(3);

</script>


<template>
    <p>{{ message }}</p>
    <button @click="clickHandler">refresh</button>
</template>

