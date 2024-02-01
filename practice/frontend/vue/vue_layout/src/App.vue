<script setup lang="ts">
import AsideVue from './components/Aside.vue';
import FooterVue from './components/Footer.vue';
import MainVue from './components/Main.vue';
</script>


<template>
  <div class="container">
    <Header class="header"></Header>
    <AsideVue class="aside"></AsideVue>
    <FooterVue class="footer"></FooterVue>
    <MainVue class="main"></MainVue>
  </div>
</template>


<style scoped>
.container {
  width: 100vw;
  height: 100vh;
  display: grid;
  grid-template-rows: 200px auto 200px;
  grid-template-columns: 300px auto;
  grid-template-areas:
    "aside header"
    "aside main"
    "aside footer";
  gap: 3px;
}

.header {
  grid-area: header;
}

.footer {
  grid-area: footer;
}

.main {
  grid-area: main;
}

.aside {
  grid-area: aside;
}
</style>