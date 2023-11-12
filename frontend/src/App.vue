<script setup lang="ts">
import { RouterView } from 'vue-router'
import { useAccountStore } from './stores/account';

const accountStore = useAccountStore()
accountStore.storeInit()

</script>

<template>
  <RouterView />
</template>

<style scoped>
</style>
