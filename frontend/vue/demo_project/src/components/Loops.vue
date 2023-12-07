<script setup lang="ts">
let names = ["张三", "李四", "王五", "赵六"];
let items = [
    { id: "0", name: "张三", age: 15 },
    { id: "1", name: "李四", age: 17 },
    { id: "2", name: "王五", age: 19 },
];
</script>

<template>
    <h1>vue 循环</h1>
    <ul>
        <li v-for="(name, index) in names" :key="index">{{ name }}</li>
    </ul>

    <ul>
        <li v-for="(item, index) in items" :id="item.id">
            {{ index + " " + item.name + " " + item.age }}
        </li>
    </ul>

    <ul>
        <li v-for="(item, index) in items">
            {{ index }}
            <ul>
                <li v-for="(k, v, i) in item">
                    {{ k + ": " + v + "-" + i }}
                </li>
            </ul>
        </li>
    </ul>
</template>

<style scoped></style>
