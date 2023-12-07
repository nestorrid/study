<script setup lang="ts">
import { ref } from 'vue';

const inputText = ref("")
const checked = ref(false)
const options = ["A", "B", "C", "D"]
const checkedOptions = ref([])
const picked = ref(null)
const selected = ref(null)

</script>


<template>
    <h1>表单输入绑定</h1>
    <div class="container">
        <div>input text:{{ inputText }}</div>
        <div><input type="text" v-model="inputText"></div>
    </div>
    <div class="container">
        <div>{{ checked }}</div>
        <input type="checkbox" id="checkbox" v-model="checked">
        <label for="checkbox">选项框</label>
    </div>
    <div class="container">
        <div>多选结果:{{ checkedOptions }}</div>
        <span v-for="(item, index) in options" :key="index">
            <input type="checkbox" :id="'option' + index" v-model="checkedOptions" :value="item">
            <label :for="'option' + index">{{ item }}</label>
        </span>
    </div>
    <div class="container">
        <div>单选结果: {{ picked }}</div>
        <span v-for="(item, index) in options" :key="index">
            <input type="radio" :id="'radio' + index" :value="item" v-model="picked">
            <label :for="'radio' + index">{{ item }}</label>
        </span>
    </div>
    <div class="container">
        <div>下拉列表: {{ selected }} </div>
        <select v-model="selected">
            <option disabled value="">select one</option>
            <option v-for="(item, index) in options" :value="item" :key="index">{{ item }}</option>
        </select>
    </div>
</template>


<style scoped>
.container {
    margin-bottom: 1.5rem;
}
</style>