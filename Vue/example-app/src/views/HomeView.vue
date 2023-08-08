<template>
    <section v-if="username" class="flex-standard">
      <div>
        <div class="title flex-standard">
          <h1>Hello <span class="green-text">{{ username }}</span> !</h1>
        </div>
        <div class="pic">
          <img :src="getPicture()" alt="Character picture"
          class="character-img"
          :class="isFemale ? 'bordered-img' : ''">
        </div>
      </div>
      
      <div>
        <div class="home-card">
          <PlayerLevel />
        </div>
        <div class="home-card">
          <CommunityDay/>
        </div>
        <div class="home-card">
          <RandomPokemon/>
        </div>
      </div>
      

    </section>
    <section v-else class="flex-standard">
      <h1>Sorry!</h1>
      <p>Login to access this page</p>
      <button class="btn"
      @click="redirectLogin">Go to login</button>
    </section>
</template>

<style scoped>
  section {    gap: 1rem;  }
  .title {    color: azure;  }
  img {    max-height: 30rem;  }
  .bordered-img {
    border: 1px solid var(--light-green);}
  .character-img{
    margin-top: .5rem;
  }
  .home-card{
    border: 1px solid var(--vt-c-white-soft);
    border-radius: 5px;
    padding: 0.3rem 1rem;    margin: .75rem;
  }
</style>

<script setup lang="ts">
  import { useLoginStore } from '@/stores/login';
  import router from '@/router';
  import CommunityDay from '@/components/CommunityDay.vue';  
  import PlayerLevel from '@/components/PlayerLevel.vue';
  import RandomPokemon from '@/components/RandomPokemon.vue';

  const loginStore = useLoginStore();

  const username: string = loginStore.username
  const isFemale : boolean = loginStore.isFemale

  const redirectLogin = () : void => {
    router.push('/')
  }

  const getPicture = () : string => {
    return isFemale? 
    'https://pbs.twimg.com/media/C4zAOKcWIAAk-w_.jpg' :
    'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/268ae75f-f709-4288-97f8-fc0f202c8d36/ddto5ok-9a85550d-0770-4ad4-9a9f-1d04cacc96f6.png/v1/fit/w_828,h_1698/pokemon_go___male_trainer_by_cssobral2013_ddto5ok-414w-2x.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjYyNCIsInBhdGgiOiJcL2ZcLzI2OGFlNzVmLWY3MDktNDI4OC05N2Y4LWZjMGYyMDJjOGQzNlwvZGR0bzVvay05YTg1NTUwZC0wNzcwLTRhZDQtOWE5Zi0xZDA0Y2FjYzk2ZjYucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.Np_QDBssuVuRfoWcfaHV8rczdIVCDzbSQPYsCLllcKs'
  }
</script>