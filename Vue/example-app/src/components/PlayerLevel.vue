<template>
    <p>Your current level is {{ level }}</p>
    <p>To the next level you need: {{ displayXP() }} XP</p>
</template>
  
  <style>
  </style>
  
<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useLoginStore } from '@/stores/login';

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

  const level: number = loginStore.level

  const displayXP = () => {
    return levelData.value[level+1] < 1000 ?
    levelData.value[level+1] :
    (levelData.value[level+1]/1000).toString()+'k'
  }

</script>
  