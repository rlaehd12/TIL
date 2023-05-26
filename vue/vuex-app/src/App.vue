<template>
  <div id="app">
    <h1>{{ message }} </h1>
    <h2>{{messageLength}}</h2>
    <h2>{{doubleLength}}</h2>

    <input type="text" @keyup.enter="changeMessage" v-model="inputData">
  </div>
</template>

<script>

export default {
  name: 'App',
  data(){
    return{
      inputData:null,
    }
  },
  methods:{
    changeMessage(){
      const newMessage = this.inputData
      // dispatch('action 이름', )
      this.$store.dispatch('changeMessage', newMessage)
      this.inputData = null
    }
  },
  components: {
  },
  computed:{
    message(){
      return this.$store.state.messsage
    },
    messageLength(){
      return this.$store.getters.messageLength
    },
    doubleLength(){
      return this.$store.getters.doubleLenght
    }
  },

}
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
