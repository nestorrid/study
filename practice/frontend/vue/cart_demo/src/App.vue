<script setup lang="ts">
import Cart from "@/components/Cart/Cart.vue"
</script>


<template>
  <div class="container">
    <div class="mobile">
      <Cart></Cart>
    </div>
  </div>
</template>


<style scoped lang="scss">
.container {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>