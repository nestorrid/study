<script setup lang="ts">
import { ref } from 'vue';


const message = ref("")

function divClick() {
    message.value += 'div clicked.<br/>';
}

function btnClick() {
    message.value += 'btn clicked.<br/>';
}

</script>


<template>
    <div @click.right.capture.prevent>
        <h1>事件修饰符</h1>
        <div @click="divClick">
            <button @click="btnClick">sample button</button>
        </div>
        <div @click.capture.stop="divClick">
            <button @click="btnClick">div captured</button>
        </div>
        <div @click="divClick">
            <button @click.stop="btnClick">button.stop</button>
        </div>
        <button @click="btnClick" @click.right.prevent>disable right click</button>
        <p v-html="message"></p>
    </div>
</template>


<style scoped></style>