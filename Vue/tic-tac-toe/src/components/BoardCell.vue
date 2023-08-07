<template>
  <div class="cell cross flex-center" @click="update"
  :class="value ? 'cross' : (value === false)? 'circle' : ''"
  :style="{gridArea: `${x} / ${y}`}">
      <span class="material-symbols-outlined" 
      v-if="value">
      {{value ? 'close' : 'circle'}}
      </span>
  </div>
</template>

<script setup>
  import { useGameStore } from '@/stores/game';

  const gameStore = useGameStore();
  function reset() {    gameStore.reset()  }
  function update(){    ù
    console.log(x, y)
    // gameStore.update(x,y)  
  }

  // watch(() => {
  // const { modelValue } = props;
  // console.log(modelValue);
  // });

  const position = defineProps(['position']).position
  const [x, y] = position
  // const [x, y] = toRefs(props.position);


  // const [x, y] = [0,0]
  // const x = props.position.x;
  // Create a ref for the alias x

  // 
  // const { position } = toRef(props);

  // Convert props to reactive references
  // const [x, y] = toRefs(position);


  const value = gameStore.grid[y][x]; 
  // value in the cell position

  // const [x, y] = this.position;
  // function reset(){ gameStore.reset()}

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
.cross{    border: 3px solid aqua}
.circle { border: 3px solid orangered}

.cell{
  background-color: var(--vt-c-black-soft);
  border-radius: 10px;
  border: 3px solid azure;
}
</style>