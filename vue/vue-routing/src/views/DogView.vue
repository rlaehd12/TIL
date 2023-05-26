<template>
  <div>
    <p v-if="!imgSrc">{{message}} </p>
    <img :src="imgSrc" alt="" v-if="imgSrc">
    <br>
    <button @click="uppp">uppp</button>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name:'DogView',
  data(){
    return{
      imgSrc: null,
      message: '로딩중........',
      test:0,
      time_now : null
    }
  },
  methods:{
    getDogImage(){
      const breed = this.$route.params.breed
      const dogImageSearchURL = `https://dog.ceo/api/breed/${breed}/images/random`

      axios({
        method:'get',
        url:dogImageSearchURL,
      })
      .then((response)=>{
        console.log(response);
        const imgSrc = response.data.message
        this.imgSrc = imgSrc
      })
      .catch(()=>{
        // console.log(error);
        // this.message = `${this.$route.params.breed}는 없는 품종입니다`
        this.$router.push('/404')
      })
    },
    uppp(){
      this.test+=1
      // const date = new Date()
      // const a = date.getSeconds()
      // this.time_now = date.getSeconds()
      console.log(this.computedTest);
    }
  },
  computed:{
    computedTest(){
      const data = new Date() // 객체 
      const a = data.getSeconds()
      // eslint-disable-next-line
      const b = this.test
      // console.log(b);
      return a
    }
  },
  created(){
    this.getDogImage()
  },
}
</script>

<style>

</style>