<template>
    <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/community">Community Day</RouterLink>
    </nav>
    <RouterView />
</template>

<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
    nav {
    width: 100%;
    font-size: 12px;
    text-align: center;
    position: fixed; 
    top: 0; left: 0;
    display: flex;
    justify-content: flex-end;
    padding: 1rem;
    background-color: var(--vt-c-divider-light-1);
    }

    nav a.router-link-exact-active {
    color: var(--color-text);
    }

    nav a.router-link-exact-active:hover {
    background-color: transparent;
    }

    nav a {
    display: inline-block;
    padding: 0 1rem;
    border-left: 1px solid var(--color-border);
    }

    nav a:first-of-type {
    border: 0;
    }
</style>