<template>
  <div>
    <div class="border">
      <h1>AppParent</h1>
      <input type="text" v-model="ParentData">
      <h3>appdata {{AppData}} </h3>
      <h3>childdata {{ChildData}} </h3>
    </div>
    <AppMiddle :parent-data="ParentData"
    @app-to-parent = "GetAppData"
    @child-to-parent = "GetChildData"
    />
  </div>
</template>

<script>
import AppMiddle from "@/components/AppMiddle.vue";

export default {
  name:'AppParent',
  components:{
    AppMiddle,
  },
  data(){
    return{
      ParentData:null,
      AppData:null,
      ChildData:null,
    }
  },
  methods:{
    GetAppData(data){
      // console.log(data);
      this.AppData = data
    },
    GetChildData(data){
      this.ChildData = data
    },
  }
}
</script>

<style scoped>
.border{
  border: 1px black solid;
}

</style>