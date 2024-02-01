<script setup lang="ts">

function blockPage() {
    const start = Date.now();
    while (Date.now() - start < 3000) { }
}

</script>


<template>
    <div>
        <div class="ball ball1"></div>
        <div class="ball ball2"></div>
    </div>
    <button @click="blockPage" style="margin-top: 120px;">block</button>
</template>


<style scoped lang="scss">
.ball {
    width: 100px;
    height: 100px;
    background-color: red;
    margin-bottom: 10px;
    border-radius: 50%;
    left: 650px;

    &1 {
        animation: move1 1s infinite ease-in-out;
        animation-direction: alternate;
    }


    &2 {
        position: fixed;
        animation: move2 1s alternate infinite ease-in-out;
    }
}

@keyframes move1 {
    to {
        transform: translate(100px);
    }
}

@keyframes move2 {
    to {
        left: 750px;
    }
}
</style>