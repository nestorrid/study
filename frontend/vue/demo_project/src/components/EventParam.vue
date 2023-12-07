<script setup lang="ts">
import { ref } from 'vue';

const names = ['accept', 'cancel']
const message = ref("")

function clickHandler(name: string): void {
    message.value = `clicked on ${name}`
}

function listObject(e: any) {
    let str = "";
    for (let key in e) {
        str += key + ": " + e[key] + '<br/>'
    }
    return str;
}

function withEvent(e: Event) {
    message.value = listObject(e)
}

function withArgsAndEvent(arg: string, event: Event) {
    message.value += arg + '<br/>' + listObject(event)
}

</script>


<template>
    <h1>事件传参</h1>
    <button v-for="name in names" @click="clickHandler(name)">{{ name }}</button>
    <br>
    <button @click="withEvent">event</button>
    <button @click="withArgsAndEvent('arg', $event)">args and event</button>
    <div v-html="message"></div>
</template>


<style scoped></style>