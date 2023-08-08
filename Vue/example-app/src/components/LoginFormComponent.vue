<template>
<form @submit.prevent="handleLogin">
    <label> Username:
    <input v-model="newUsername" type="text" required />
    </label>
    <br />
    <label> Level:
    <input v-model.number="newLevel" type="number" required 
        min="0" max="50"/>
    </label>
    <br />
    
    <div class="gender-switch">
        <label class="switch">
        <input type="checkbox" 
        v-model="newFemale" />
        <span class="slider round"></span>
        </label>
        <span>{{ newFemale ? 'Female' : 'Male' }}</span>
    </div>
    
    <br />
    <button type="submit">Login</button>
    </form>
</template>

<script setup lang="ts">
import router from '@/router';    
import { ref } from 'vue';
import { useLoginStore } from '@/stores/login';

    const newUsername = ref('');
    const newLevel = ref(0);
    const newFemale = ref(false);

    const loginStore = useLoginStore();

    const handleLogin = () => {
    if (newUsername.value) {        
        loginStore.login(newUsername.value, newLevel.value, newFemale.value);
        router.push('/home');
    }
    };
</script>

<style scoped>
button {
    margin: 1rem
}
.switch {
  position: relative;
  display: inline-block;
  width: 3rem;
  height: 1.5rem;
}

/* Hide the default checkbox */
.switch input {
  opacity: 0;  width: 0;  height: 0;
}

/* The slider (the round part) */
.slider {
  position: absolute;
  cursor: pointer;
  top: 0;  left: 0;  right: 0;  bottom: 0;
  background-color: #ccc;
  -webkit-transition: 0.4s;
  transition: 0.4s;
  border-radius: 1.5rem; 
}

.slider:before {
  position: absolute;
  content: '';
  height: 1.1rem;   width: 1.1rem; 
  left: 0.2rem;   bottom: 0.2rem;
  background-color: white;
  -webkit-transition: 0.4s;
  transition: 0.4s;
  border-radius: 50%;
}

input:checked + .slider {
  background-color: var(--light-green);
}

input:checked + .slider:before {
  -webkit-transform: translateX(.9rem); 
  -ms-transform: translateX(.9rem);
  transform: translateX(.9rem);
}

/* Rounded sliders with text */
.slider.round {
  border-radius: 1.5rem; 
}

.slider.round:before {
  border-radius: 50%;
}

span{
    margin-left: .5rem;
}
input {
    margin-bottom: .3rem;
}
.gender-switch{
    margin: .5rem auto;
}
</style>