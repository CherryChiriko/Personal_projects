<script setup lang="ts">
  import { ref, onMounted } from 'vue';
  import { useLoginStore } from '@/stores/login';
import router from '@/router';

  const loginStore = useLoginStore();

  const levelData = ref([]);
  const loading = ref(true);

  // Fetch levelup XP data from the API
  const fetchLevelData = async () => {
    try {
      const response = await fetch('https://pogoapi.net/api/v1/player_xp_requirements.json');
      const jsonData = await response.json();
      levelData.value = jsonData;
      loading.value = false;
    } catch (error) {
      console.error('Error fetching data:', error);
      loading.value = false;
    }
  };

  onMounted(() => {
    fetchLevelData();
  });

  const username: string = loginStore.username
  const level: number = loginStore.level

  const displayXP = () => {
    return levelData.value[level]/1000
  }

  const redirectLogin = () => {
    router.push('/')
  }
</script>

<template>
    <section v-if="username">
      <h1>Hello {{ username }} !</h1>
      <p>Your current level is {{ level }}</p>
      <p>To the next level you need: {{ displayXP() }}k XP</p>
    </section>
    <section v-else class="flex-standard">
      <h1>Sorry!</h1>
      <p>Login to access this page</p>
      <button class="btn"
      @click="redirectLogin">Go to login</button>
    </section>
</template>

<style scoped>
  section {
    flex-direction: column;
  }
</style>