<template>
    <div class="flex-standard box-section">
    <div class="img">
      <img :src="pokemonImage">
    </div>
    <div>
      <p>Random pokémon: <span class="green-text">{{ pokemonName }}</span></p>
      <button class="btn"
      @click="fetchRandomPkmn">Change</button>
    </div>
  </div>
</template>

<style>
    .box-section{
        justify-content: space-around;
    }
</style>

<script setup lang="ts">
import { ref, onMounted, type Ref } from 'vue';


const pokemonName : Ref<string> = ref('');
const pokemonImage : Ref<string> = ref('');
const loading = ref(true);

const fetchRandomPkmn = async () => {
    try {
      const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${getRandomN()}`)
      const jsonData = await response.json();
      pokemonImage.value = jsonData.sprites.front_default;
      pokemonName.value = capitalizeFirstLetter(jsonData.species.name)
      console.log(jsonData)
      loading.value = false;
    } catch (error) {
      console.error('Error fetching data:', error);
      loading.value = false;
    }
  };

  onMounted(() => {
    fetchRandomPkmn();
  });

  function capitalizeFirstLetter(s: string) {
    return s.charAt(0).toUpperCase() + s.slice(1);
  }

  function getRandomN(){
    const MAX_PKMN = 1015;
    return Math.floor(Math.random() * MAX_PKMN + 1)
  }

</script>