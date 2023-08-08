import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useLoginStore = defineStore('login', () => {
  const username = ref('')
  const level = ref(0)
  const isFemale = ref(false)

  function login(newUsername : string, newLevel: number, newFemale: boolean) : void {
    username.value = newUsername;
    level.value = newLevel;
    isFemale.value = newFemale;
  }

  return { username, level, isFemale, login }
})