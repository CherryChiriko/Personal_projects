<template>
  <div class="flex-standard">
    <div>
      <img :src="pokemonImage">
    </div>
    <div>
      <p>The next community day is: {{ displayLastDate() }}</p>
      <p>Featured pokémon: <span class="green-text">{{ pokemonName }}</span></p>
    </div>
  </div>
</template>

<style>
</style>

<script setup lang="ts">
import { ref, onMounted, type Ref } from 'vue';

interface ICommunityDay {
  bonuses: string[];
  boosted_pokemon: string[];
  community_day_number: number;
  end_date: string;
  event_moves: { move: string; move_type: string; pokemon: string }[];
  start_date: string;
}

const communityDayData : Ref<ICommunityDay[]> = ref([]);
const communityDate : Ref<string> = ref('');
const pokemonName : Ref<string> = ref('');
const pokemonImage : Ref<string> = ref('')
const loading = ref(true);

const fetchCommunityDayData = async () => {
    try {
      const response = await fetch('https://pogoapi.net/api/v1/community_days.json');
      const jsonData = await response.json();
      communityDayData.value = jsonData;
      loading.value = false;

      const L = communityDayData.value.length;
      pokemonName.value = communityDayData.value[L-1].boosted_pokemon[0];
      communityDate.value = communityDayData.value[L-1].start_date;

      const pokemonResponse = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonName.value.toLowerCase()}`)
      const jsonPokemonData = await pokemonResponse.json();
      pokemonImage.value = jsonPokemonData.sprites.front_default;

    } catch (error) {
      console.error('Error fetching data:', error);
      loading.value = false;
    }
  };

  onMounted(() => {
    fetchCommunityDayData();
  });

  const displayLastDate = () => {
    return communityDate.value.split('-').reverse().join(' / ')
  }

</script>
