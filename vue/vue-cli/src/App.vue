<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <MyComponent/>
    <MyComponent/>
    <MyComponent/>
    <MyComponent/>
    <HelloWorld id="aaa" msg="Welcome to Your Vue.js App"/>

  </div>
</template>

<script>
// @ src파일 의미
import HelloWorld from './components/HelloWorld.vue'
import MyComponent from '@/components/MyComponent.vue'

export default { // 등록하는 곳
  name: 'App',
  components: {
    HelloWorld,
    MyComponent,
  }
}
const aaa = document.querySelector('#aaa')
console.log(aaa);
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
