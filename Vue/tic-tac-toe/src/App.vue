<script setup lang="ts">
import GameBoard from './components/GameBoard.vue';
import { useGameStore } from '@/stores/game';

const gameStore = useGameStore();
const isCross = gameStore.isPlayer1; 
function reset() {    gameStore.reset()  }
</script>

<template>
  
  <div class="screen flex-center flex-column">
    <h1 class="mb-4 title">Tic-tac-toe game</h1>    
    <span class="mb-4">
      <h4>It's <span class="material-symbols-outlined" 
      :class="isCross ? 'cross' : 'circle'">
      {{isCross ? 'close' : 'circle'}}
      </span> 's turn</h4>
      
    </span>
    <GameBoard />
    <button class="btn mt-4 btn btn-outline-light"
    @click="reset">Reset</button>
  </div>
</template>

<style scoped>
.screen{  height: 100vh;}
.title { color: var(--vt-c-white-soft)}
</style>

