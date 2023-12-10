<script setup lang="ts">

import { reactive, ref } from "vue";

import jsonData from "./data.json";
import { Product, Category } from "./define";

import CartMenuVue from "./CartMenu.vue";
import ProductsVue from "./Products.vue";
import CartFooterVue from "./CartFooter.vue";

const categories = reactive(new Array<Category>());
let products = ref(new Array<Product>());
const cartItems = reactive(new Array<Product>);

for (let category of jsonData) {
    categories.push({
        id: category.id,
        name: category.category,
    });
}

function load_products(catIdx: number): Array<Product> {
    const arr = new Array<Product>()
    for (let product of jsonData[catIdx].products) {
        arr.push(product)
    }
    return arr
}

function menu_selected(index: number) {
    products.value = load_products(index)
}

function cart_index_of_product(product: Product): number {
    return cartItems.findIndex((el) => el.id == product.id && el.name == product.name)
}

function add_product_to_cart(index: number) {
    const product = products.value[index]

    if (product.count! == 0) {
        let idx = cart_index_of_product(product)
        if (idx !== -1)
            cartItems.splice(idx, 1)
    } else {
        if (cart_index_of_product(product) === -1)
            cartItems.push(product)
    }
}

function update_product_count(index: number, count: number) {
    products.value[index].count = products.value[index].count ?? 0
    products.value[index].count! += count
    add_product_to_cart(index)
}

</script>


<template>
    <div class="mobile">
        <div class="menu">
            <CartMenuVue v-model="categories" @select-menu-index="menu_selected"></CartMenuVue>
        </div>
        <div class="products">
            <ProductsVue v-model:products="products" @update:product-count="update_product_count"></ProductsVue>
        </div>
        <div class="footer">
            <CartFooterVue v-model:cartItems="cartItems" :threshold-price="30"></CartFooterVue>
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
    background-color: $bg-color;
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