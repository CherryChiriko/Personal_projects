<template>
    <section class="flex-standard">
      <h2>Login</h2>
      <p>Use your pokémon GO credentials</p>
      <form @submit.prevent="handleLogin">
        <label>
          Username:
          <input v-model="newUsername" type="text" required />
        </label>
        <br />
        <label>
          Level:
          <input v-model.number="newLevel" type="number" required 
          min="0" max="50"/>
        </label>
        <br />
        <button type="submit">Login</button>
      </form>
    </section>
</template>
  
<script setup lang="ts">
    import router from '@/router';    
    import { ref } from 'vue';
    import { useLoginStore } from '@/stores/login';

    const newUsername = ref('');
    const newLevel = ref(0);

    const loginStore = useLoginStore();

    const handleLogin = () => {
    if (newUsername.value && newLevel.value) {        
        loginStore.login(newUsername.value, newLevel.value);
        router.push('/home');
    }
    };
</script>

<style scoped>
section {
    flex-direction: column;
    border: 1px solid var(--vt-c-white-soft);
    padding: 1rem;
    border-radius: 15px;
    width: 80%;
}
button {
    margin: 1rem
}
</style>