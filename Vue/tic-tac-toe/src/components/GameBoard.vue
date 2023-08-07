<template>
    <div class="board">
        <!-- {{grid.map((row, rowIdx) =>
            row.map((cell, colIdx) => (
              // We put the colIdx first because that is our X-axis value
              // and the rowIdx second because that is our Y-axis value
              // Getting in the habit makes using 2d grids much easier
              <BoardCell key={`${colIdx}-${rowIdx}`} cell={cell} />
            ))
          )}} -->
        <BoardCell v-for="index in 9" :key="index"
        :position = "getPosition(index-1)"/>
        <!-- <BoardCell />
        <BoardCell />

        <BoardCell />
        <BoardCell />
        <BoardCell />
        
        <BoardCell />
        <BoardCell />
        <BoardCell /> -->
        <!-- <BoardCell :player="1" :key=""/> -->
        <!-- <BoardCell v-for="(cellValue, index) in propValues" :key="index" :index="index"/> -->
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