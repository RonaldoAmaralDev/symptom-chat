<template>
  <div class="layout">
    <AppHeader />

    <main class="main">
      <router-view />
    </main>

    <AppFooter />
  </div>
</template>

<script setup>
import AppHeader from './components/layout/Header.vue'
import AppFooter from './components/layout/Footer.vue'
</script>