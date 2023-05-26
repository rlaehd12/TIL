<template>
  <div>
    <div class="border">
      <h1>App</h1>
      <input type="text" v-model="AppData">
      <h3>parentdata {{parentData}} </h3>
      <h3>childdata {{ChildData}} </h3>
    </div>
    <AppChild :app-data="AppData" :parent-data="parentData"
    @child-to-app = "GetChildData"/>
  </div>
</template>

<script>
import AppChild from "@/components/AppChild.vue";

export default {
  name:'AppMiddle',
  components:{
    AppChild,
  },
  data(){
    return{
      AppData:null,
      ChildData:null,
    }
  },
  props:{
    parentData:String,
  },
  methods:{
    AppToParent(){
      this.$emit('app-to-parent', this.AppData)
    },
    ChildToParent(){
      this.$emit('child-to-parent', this.ChildData)
    },
    GetChildData(data){
      this.ChildData = data
    },

  },
  watch:{
    AppData(){
      this.AppToParent()
      // console.log(data);
    },
    ChildData(){
      this.ChildToParent()
    }
  },


}
</script>

<style scoped>
.border{
  border: 1px black solid;
}

</style>