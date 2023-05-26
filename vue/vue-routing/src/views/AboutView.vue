<template>
  <div class="about">
    <h1>This is an about page</h1>
    <router-link :to="{name:'home'}">Home</router-link>|
    <button @click="toHome">tohome!!!</button>
    <input type="text" @keyup.enter="goToHello" v-model="inputData">
  </div>
</template>

<script>
export default {
  name:'AboutView',
  methods:{
    toHome(){
      this.$router.push({name:'home'})
    },
    goToHello(){
      this.$router.push({name: 'hello', params:{userName: this.inputData}})
    },
  },
  data(){
    return{
      inputData:null,
    }
  },
}
</script>