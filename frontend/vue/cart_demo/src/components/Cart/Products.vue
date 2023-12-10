<script setup lang="ts">

import { Product } from './define';

const props = defineProps<{
    products: Product[]
}>()

const emits = defineEmits<{
    (e: "update:productCount", idx: number, count: number): void
}>()

function increase(idx: number) {
    emits("update:productCount", idx, 1)
}

function decrease(idx: number) {
    emits("update:productCount", idx, -1)
}

</script>


<template>
    <div class="product_list">
        <div class="product" v-for="(product, index) in props.products" :key="index.toFixed() + product.id">
            <div class="left">
                <div class="image">
                    <img :src="product.image" alt="">
                </div>
                <div class="origin">$ {{ product.price }}</div>
                <div class="current">$ {{ product.curprice.toFixed(2) }}</div>
                <div class="info">
                    <div>
                        <span>库存 </span><span>{{ product.inventory }}</span>
                    </div>
                </div>
            </div>
            <div class="right">
                <p class="name">{{ product.name }}</p>
                <div class="info">
                    <div>
                        <span>月销 </span><span>{{ product.sold }}</span>
                    </div>
                    <div>
                        <span>好评 </span><span>{{ product.score }}</span>
                    </div>

                </div>
                <p class="desc">{{ product.desc }}</p>
                <div class="controlls">
                    <div @click="increase(index)"><span>+</span></div>
                    <span :class="product.count ? '' : 'hidden'">{{ product.count ?? 0 }}</span>
                    <div :class="product.count ? '' : 'hidden'" @click="decrease(index)"><span>-</span></div>
                </div>
            </div>
        </div>
    </div>
</template>


<style scoped lang="scss">
.product_list {
    padding: 8px 12px;
    height: 100%;
    overflow-y: scroll;

    &::after {
        content: "~~~ end ~~~";
        margin-top: 2rem;
        display: block;
        height: 8rem;
        text-align: center;
        color: #bbb;
    }

    .product {
        display: flex;
        margin-bottom: 8px;
        border: 1px solid $color;
        padding: 0.8rem 1.2rem 0.4rem;
        border-radius: 8px;

        .info {
            display: flex;

            div {
                margin-right: 1rem;
            }

            span {
                font-size: 1.4rem;
                margin-right: 2px;
                white-space: nowrap;
                color: darken($color: $color, $amount: 15%);
            }
        }

        .right {
            display: flex;
            flex-direction: column;

            .name {
                margin-bottom: 0.4rem;
                font-size: 2rem;
                font-weight: bold;
                text-wrap: nowrap;
            }

            .desc {
                margin: 8px 0;
                display: -webkit-box;
                -webkit-box-orient: vertical;
                // line-clamp: 3;
                -webkit-line-clamp: 3;
                overflow: hidden;
                font-size: 1.5rem;
                text-overflow: ellipsis;
                color: #ddd;
            }

            .controlls {
                display: flex;
                flex-direction: row;
                flex-flow: row-reverse;

                ::selection {
                    background-color: rgba(0, 0, 0, 0);
                }

                &:hover {
                    cursor: pointer;
                }

                div {
                    width: 3rem;
                    height: 3rem;
                    border-radius: 1.5rem;
                    background-color: $highlight-color;
                    color: $color;

                    span {
                        border: none;
                        width: 3rem;
                        height: 3rem;
                        font-size: 2rem;
                        text-align: center;
                        line-height: 3rem;
                    }
                }

                .hidden {
                    visibility: hidden;
                }

                span {
                    margin: 0rem 1rem;
                    font-size: 1.5rem;
                    width: 6rem;
                    height: 3rem;
                    border: 1px solid white;
                    line-height: 3rem;
                    border-radius: 1.5rem;
                    text-align: center;
                }
            }
        }

        .left {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-right: 1.2rem;
            padding: 0 4px;

            .image {
                width: 6rem;
                height: 6rem;
            }

            img {
                widows: 6rem;
                height: 6rem;
                border: 2px solid white;
                margin-bottom: 0.4rem;
                border-radius: 50%;
            }

            div {
                margin: 4px 0;
            }

            .origin {
                text-decoration: line-through;
                font-size: 1.5rem;
                color: darken($color: $color, $amount: 30%);
            }

            .current {
                font-size: 1.6rem;
                color: gold;
            }

        }

    }
}
</style>