<template>
  <div id="app">

    <h1>동영상 보여줄거임</h1>
    <!-- <iframe src="" frameborder="0"></iframe> -->
    <input type="text" v-model="search_keyword" @keyup.enter="SearchYoutube">
    <br>
    <br>
    <div v-if="video_lst">
      <VideoItem
      v-for="(video, index) in video_lst" :key="index"
      :video=video
      />
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import VideoItem from '@/components/VideoItem.vue'


export default {
  name: 'App',
  data(){
    return{
      video:null,
      search_keyword:null,
      video_lst:null,
    }
  },
  components:{
    VideoItem
  },
  created(){
    console.log(process.env);
  },
  methods:{
    SearchYoutube(){
      const apikey = process.env.VUE_APP_YOUTUBE_API_KEY;
      const query = this.search_keyword
      this.search_keyword = null
      const apiUrl = `https://www.googleapis.com/youtube/v3/search?key=${apikey}&part=snippet&q=${query}&type=video`;
      
      // this.video_lst = response.data.items
      // console.log(this.video_lst[0].id.videoId)

      axios({
        methods:'get',
        url:apiUrl
      })
      .then((response)=>{
        // console.log(response.data.items);
        const video_lst = response.data.items
        this.video_lst = video_lst
      })
    },
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
