<template>
  <div 
  class="cell flex-center" 
  :class="cellClass"
  @click="update">
      <span 
      class="material-symbols-outlined">
      {{ playerSymbols }}
      </span>
  </div>
</template>

<!-- v-if="value" -->
<script setup lang="ts">
  import { useGameStore } from '@/stores/game';
  import { ref, toRefs, watch, type Ref, computed } from 'vue'

  const props = defineProps<{
    position: number[],
  }>();

  const { position } = toRefs(props);
  const [x, y] = position.value;

  const gameStore = useGameStore();
  function update(){
    gameStore.update(x,y);
  }

  
  var value : Ref<boolean | null>= ref(null);
  watch(gameStore.grid, () => {
    value.value = gameStore.grid[y][x];
  });

  const playerSymbols = computed(() => {
    if (value.value === true) {
      return 'close';
    } else if (value.value === false) {
      return 'circle';
    } else {
      return '';
    }
  });
  const cellClass = computed(() => {
    if (value.value === true) {
      return 'cross';
    } else if (value.value === false) {
      return 'circle';
    } else {
      return '';
    }
  });

</script>
<style scoped>

.material-symbols-outlined {
  font-size: 50px;
  font-variation-settings:
  'FILL' 0,
  'wght' 700,
  'GRAD' 0,
  'opsz' 48
}
.cross{    border: 3px solid aqua !important}
.circle { border: 3px solid orangered !important}

.cell{
  background-color: var(--vt-c-black-soft);
  border-radius: 10px;
  border: 3px solid azure;
}
</style>