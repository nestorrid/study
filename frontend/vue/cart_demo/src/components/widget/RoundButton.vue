<script setup lang="ts">

interface Props {
    size: number;
    type: 'plus' | 'minus';
}

const props = defineProps<Props>()

</script>


<template>
    <div :class="props.type" class="roundBtn"></div>
</template>


<style scoped lang="scss">
.roundBtn {
    border-radius: 50%;
}
</style>