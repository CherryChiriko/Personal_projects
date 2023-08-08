<template>
    <section class="flex-standard">
      <h2>Login</h2>
      <p>Use your pokémon GO credentials</p>
      <LoginFormComponent />
    </section>
</template>
  
<script setup lang="ts">
import LoginFormComponent from '@/components/LoginFormComponent.vue';   
</script>

<style scoped>
section {
    flex-direction: column;
    border: 1px solid var(--vt-c-white-soft);
    padding: 1rem;
    border-radius: 15px;
    width: 80%;
}
</style>