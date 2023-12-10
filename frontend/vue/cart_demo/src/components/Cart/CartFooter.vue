<script setup lang="ts">

import { computed } from 'vue';
import { Product } from './define';

const props = defineProps<{
    cartItems: Product[]
    thresholdPrice?: number
}>()

console.log(props.cartItems);

const totalCount = computed(() => {
    let count = 0
    for (let product of props.cartItems) {
        count += product.count ?? 0
    }
    return count
})

const totalPrice = computed(() => {
    let price = 0
    for (let product of props.cartItems) {
        price += product.curprice * (product.count ?? 0)
    }
    return price
})


</script>


<template>
    <div class="container">
        <div class="cartIcon">
            <svg xmlns="http://www.w3.org/2000/svg" height="32" width="36" viewBox="0 0 576 512">
                <path
                    d="M0 24C0 10.7 10.7 0 24 0H69.5c22 0 41.5 12.8 50.6 32h411c26.3 0 45.5 25 38.6 50.4l-41 152.3c-8.5 31.4-37 53.3-69.5 53.3H170.7l5.4 28.5c2.2 11.3 12.1 19.5 23.6 19.5H488c13.3 0 24 10.7 24 24s-10.7 24-24 24H199.7c-34.6 0-64.3-24.6-70.7-58.5L77.4 54.5c-.7-3.8-4-6.5-7.9-6.5H24C10.7 48 0 37.3 0 24zM128 464a48 48 0 1 1 96 0 48 48 0 1 1 -96 0zm336-48a48 48 0 1 1 0 96 48 48 0 1 1 0-96z" />
            </svg>
            <div class="badge" :class="totalCount > 0 ? 'active' : ''">{{ totalCount }}</div>
        </div>
        <div class="info">
            <div class="price">
                <div v-if="totalPrice > 0">商品总价: ${{ totalPrice.toFixed(2) }}</div>
                <div v-else>购物车还是空的~</div>
            </div>
            <div class="pay">
                <div v-if="totalPrice >= (props.thresholdPrice ?? 0)" class="settle">
                    <div>结 算</div>
                </div>
                <div v-else class="low">
                    <div>还差 <span>${{ (thresholdPrice! - totalPrice).toFixed(2) }}</span></div>
                    <div>起送</div>
                </div>
            </div>
        </div>
    </div>
</template>


<style scoped lang="scss">
.container {
    width: 100%;
    height: 100%;
    background-color: $highlight-color;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: space-between;

    .info {
        display: flex;
        height: 100%;
        align-items: center;

        .price {
            margin-right: 2rem;

            div {
                font-size: 1.5rem;
            }
        }

        .pay {
            height: 100%;
            width: 16rem;
            background-color: indigo;

            .settle {
                display: flex;
                height: 100%;
                justify-content: center;
                align-items: center;
                color: gold;
            }

            .low {
                display: flex;
                height: 100%;
                flex-direction: column;
                align-items: flex-end;
                justify-content: center;
                background-color: #666;

                div {
                    font-size: 1.5rem;
                    margin: 0.2rem 1rem;
                    color: #eee;

                    span {
                        font-size: 1.8rem;
                        color: gold;
                    }
                }
            }
        }
    }



    .cartIcon {
        box-sizing: content-box;
        border: 2px solid white;
        box-shadow: $base-shadow;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        background-color: indigo;
        position: relative;
        top: -20px;
        margin-left: 20px;

        .badge {
            position: absolute;
            background: red;
            border: 1px solid white;
            font-size: 1.4rem;
            height: 2rem;
            line-height: 2rem;
            padding: 0 1rem;
            border-radius: 1rem;
            right: -1rem;
            top: 0;
            visibility: hidden;
        }

        .active {
            visibility: visible;
        }

        svg {
            margin: 16px 10px;
            fill: $highlight-color;
        }
    }

}
</style>