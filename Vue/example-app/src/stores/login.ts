import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useLoginStore = defineStore('login', () => {
  const username = ref('')
  const level = ref(0)

  function login(newUsername : string, newLevel: number) : void {
    username.value = newUsername;
    level.value = newLevel;
  }

  return { username, level, login }
})