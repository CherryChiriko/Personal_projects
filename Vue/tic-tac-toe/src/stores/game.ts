import { ref, type Ref } from 'vue'
import { defineStore } from 'pinia'

function generateGrid(rows : number, columns: number) : null[][] {
    // Generate an empty grid for the board at the beginning of the game
    const grid: null[][] = [];

    for (let i = 0; i < rows; i++) {
        const row: null[] = [];
        for (let j = 0; j < columns; j++) {
            row.push(null);
        }
        grid.push(row);
    }

    return grid; 
}

function getInitialState() : Array<Array<boolean | null>>{
    return generateGrid(3,3)
}
function updateGrid(grid: Array<Array<boolean | null>>, x: number, y: number, newValue: boolean){
    if (x >= 0 && x < grid.length && y >= 0 && y < grid[x].length){
        if (!grid[y][x]) { grid[y][x] = newValue} 
    }
    else console.log("Invalid coordinates")
    return grid;
    // return grid[y][x] ? grid : grid.map(row => { col => grid[row][col]}) 
}


export const useGameStore = defineStore('game', () => {
    const grid : Ref<Array<Array<(null | boolean)>>> = ref(generateGrid(3,3));
    const isPlayer1 : Ref<boolean> = ref(true);

    const reset = () => (
        grid.value = generateGrid(3,3)
    )

    const update = (x: number, y: number) => {
        if (!grid.value[y][x]){
            grid.value[y][x] = isPlayer1.value;
            isPlayer1.value = !isPlayer1.value
        }
    }

    return { grid, isPlayer1, reset, update }
})