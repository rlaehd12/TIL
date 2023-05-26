// App.vue

<template>
  <div id="app">
    <p>Counter: {{ $store.state.counter }}</p>
    <p>Counter x2: {{ $store.getters.counterDouble }}</p>
    <p></p>
    <button @click="$store.dispatch('stateIncrease')">increase +</button>
    <button @click="$store.dispatch('stateDncrease')">decrease -</button>
  </div>
</template>

<script>
export default {
  name: 'App', 
}
</script>

<style>
</style>