<template>
    <input type="text" :name="txtName" :id="txtId" :disabled="isDisabled" :placeholder="placeholder" />
    <button v-bind="attrs">{{ btnName }}</button>
</template>


<script setup lang="ts">
import { ref } from 'vue';

let txtName = 'textfield';
let txtId = '0';
let placeholder = 'input something...';
let isDisabled = ref(false);

let btnName = 'Button';
let attrs = {
    id: "0",
    class: "btn"
}

</script>
