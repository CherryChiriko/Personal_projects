<template>
    <div class="board">
        <BoardCell 
        v-for="index in 9" :key="index"
        :position = "getPosition(index-1)"
        />
    </div>
</template>

<script setup lang="ts">
import BoardCell from './BoardCell.vue';

function getPosition(i: number) : number[]{
    // get the position in coordinates from the index of the cell
    return [ Math.floor(i/3), i % 3]
}

</script>

<style scoped>

.board{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(3, 1fr);
  gap: 10px;

  height: 300px; width: 300px;
  background-color: var(--vt-c-divider-light-1);
  border-radius: 25px !important;
  border: 3px solid azure;
  padding: 1rem;
}
</style>