<template>
  <div class="menu-box"
  :class="{selected: sizeListItem.selected}"
  >
    <div class="flex" @click="GetSize">
      <div>{{sizeListItem.name}}</div>
      <div>{{sizeListItem.price}}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SizeListItem',
  props:{
    sizeListItem:Object,
  },
  methods:{
    GetSize(){
      const selectedSize = this.sizeListItem
      this.$store.dispatch('SizeSelect', selectedSize)
    },
  },
}
</script>

<style scoped>
.flex{
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 60px;
}

.menu-box{
  border: 1px black solid;
  padding: 5px;
  margin: 5px;
  border-radius: 10px / 10px;
}

.selected{
  background-color: green;
  color: white;
}
</style>