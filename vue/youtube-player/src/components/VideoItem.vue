<template>
  <div>


    {{video.snippet.title}}
    <br>
    <iframe
          width="560"
          height="315"
          :src="'https://www.youtube.com/embed/' + video.id.videoId"
          frameborder="0"
          allowfullscreen
    ></iframe>
    <hr>

  </div>
</template>

<script>
export default {
  name:'VideoItem',
  props:{
    video:Object
  }

}
</script>

<style>

</style>