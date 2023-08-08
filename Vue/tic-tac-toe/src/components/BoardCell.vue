<template>
  <div 
  class="cell cross flex-center" 
  :style="{gridArea: `${x} / ${y}`}"
  :class="value ? 'cross' : (value === false)? 'circle' : ''"
  @click="update">
      <span 
      v-if="value"
      class="material-symbols-outlined">
      {{value ? 'close' : 'circle'}}
      </span>
  </div>
</template>

<script setup lang="ts">
  import { useGameStore } from '@/stores/game';
  import { toRefs, watch } from 'vue'

  const props = defineProps<{
    position: number[],
  }>();

  const { position } = toRefs(props);

  watch(position, () => {console.log(position)})

  const gameStore = useGameStore();
  function update(){
    console.log(position)
    // console.log(x, y)
    // gameStore.update(x,y)  
  }


  // const position = defineProps(['position']).position
  // const [x, y] = position
  // const [x, y] = toRefs(props.position);


  // const [x, y] = [0,0]
  // const x = props.position.x;
  // Create a ref for the alias x

  // 
  // const { position } = toRef(props);

  // Convert props to reactive references
  // const [x, y] = toRefs(position);


  
  // value in the cell position

  // const [x, y] = this.position;
  // function reset(){ gameStore.reset()}
  // const props = defineProps({
  //   position: Array
  // })
  // const [x, y] = toRefs(props).position

  // watch(position, () => {})
  // console.log(toRefs(props).position)
  const [x, y] = [0,0]
  const value = gameStore.grid[y][x]; 

  // const props = defineProps({
  //   show: Boolean,
  //   position: Array
  // })
  // const { show, position } = toRefs(props)

  // watch(show, () => {})
  // watch(position, () => {})
  // console.log(position)
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