<template>
  <div>
    <h1>AppChild</h1>
    <input type="text" v-model="ChildData">
    <h3>parentdata {{parentData}} </h3>
    <h3>appdata {{appData}} </h3>
    <h3>childdata {{ChildData}} </h3>
    <!-- <ul>
      <li v-for="(data, idx) in ChildDatacomputed" :key="idx">{{data}} </li>
    </ul> -->
  </div>
</template>

<script>
export default {
  name:'AppChild',
  data(){
    return{
      ChildData:null,
      // ChildDatacomputed:null,
    }
  },
  props:{
    appData:String,
    parentData:String,
  },
  methods:{
    ChildToApp(){
      this.$emit('child-to-app', this.ChildData)
    },
  },
  computed:{
    ChildDatacomputed(){
      this.ChildToApp()
      return this.ChildData
    }
  }

}
</script>

<style scoped>

div{
  border: 1px black solid;
}

</style>