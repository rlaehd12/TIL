<template>
  <div id="app">


    <div class="d-flex">
      <SideBar
      class="col-3 border border-2 border-secondary text-center m-2"/>
      <router-view
      class="col-8 border border-2 border-secondary m-2"/>
      <!-- <div @pass_router="change_router">
        <div v-if="current_router == 'ALL'">

        </div>

      </div> -->

    </div>

  </div>
</template>

<script>
import SideBar from "./components/SideBar.vue";

export default {
  name:'App',
  components:{
    SideBar,
  }, data(){
    return {
      current_router: 'ALL',
    }
  },
  methods: {

    change_router(route_name){
      this.change_router = route_name
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.star {
    visibility:hidden;
    font-size:20px;
    cursor:pointer;
}
.checked {
    visibility:hidden;
    font-size:20px;
    cursor:pointer;
}
.star:before {
  color: orange;
  content: "\2605";
  visibility:visible;
  /* position: absolute; */
}
.checked:before {
  visibility:visible;
  content: "\2606";
  color: orange;
  /* position: absolute; */
}
</style>
