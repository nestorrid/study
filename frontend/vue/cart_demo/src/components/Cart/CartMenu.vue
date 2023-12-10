<script setup lang="ts">
import { reactive, ref, watch } from 'vue';
import { Category } from './define';

const props = defineProps(['modelValue']);
const emit = defineEmits<{
    (e: 'selectMenuIndex', idx: number): void
}>()

const categories = reactive({ ...props.modelValue }) as Category[]
const currentCategory = ref(0)

watch(currentCategory, (value, oldValue) => {
    categories[oldValue ?? 0].isActive = false
    categories[value].isActive = true
    emit('selectMenuIndex', value)
}, { immediate: true });

function clickMenuItem(idx: number) {
    currentCategory.value = idx
}

</script>


<template>
    <div class="categoryMenu">
        <div class="menuItem" v-for="(item, index) in categories" :key="item.id.toFixed() + item.name"
            :class="item.isActive ? 'active' : ''" @click="clickMenuItem(index)">
            <p>{{ item.name }}</p>
        </div>
    </div>
</template>


<style scoped lang="scss">
.categoryMenu {
    height: 100%;
    overflow-y: scroll;
    overflow-x: hidden;
    background-color: lighten($color: $bg-color, $amount: 15%);

    .menuItem {
        padding: 16px 12px;
        border-bottom: 1px solid $bg-color;
        color: lighten($color: $highlight-color, $amount: 20%);

        p {
            overflow: hidden;
        }
    }

    .active {
        background-color: $bg-color;
        font-weight: bold;
        border-left: 4px solid $highlight-color;
    }

    &::after {
        content: "~end~";
        display: block;
        height: 8rem;
        margin-top: 2rem;
        text-align: center;
        color: #ccc;
    }
}
</style>