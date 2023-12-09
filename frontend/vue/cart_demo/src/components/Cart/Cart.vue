<script setup lang="ts">

import { reactive } from "vue";
import jsonData from "./data.json";

console.log(jsonData);

// interface Product {
//     id: Number,
//     name: String,
//     desc: String,
//     price: Number,
//     curprice: Number,
//     sold: Number,
//     score: Number,
//     inventory: Number,
//     image: String
// }

interface Category {
    id: Number,
    category: String,
}

const categories = reactive(new Array<Category>());

for (let item of jsonData) {
    categories.push({
        id: item.id,
        category: item.category
    })
}


</script>


<template>
    <div class="mobile">
        <div class="menu">
            menu
        </div>
        <div class="products">
            prodducts
        </div>
        <div class="footer">
            footer
        </div>
    </div>
</template>


<style scoped lang="scss">
.menu {
    position: absolute;
    top: 0;
    left: 0;
    width: $mobile-menu-width;
    bottom: $mobile-footer-height;
    height: auto;
    background-color: $bg-color;
}

.products {
    position: absolute;
    background-color: blue;
    height: auto;
    top: 0;
    left: $mobile-menu-width;
    bottom: $mobile-footer-height;
    right: 0;
}


.footer {
    position: absolute;
    width: 100%;
    height: $mobile-footer-height;
    bottom: 0;
    left: 0;
    background-color: red;
}
</style>