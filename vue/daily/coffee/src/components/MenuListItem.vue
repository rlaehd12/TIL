<template>
  <div class="menu-box"
  :class="{selected: menuListItem.selected}"
  >
    <div @click="GetItem" class="flex">
      <img :src="menuListItem.image" alt="" class="small">
      <div>{{menuListItem.title}}</div>
      <div>{{menuListItem.price}}</div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'MenuListItem',
  props:{
    menuListItem:Object,
  },
  methods:{
    GetItem(){
      // console.log(this.menuListItem);
      const selectedMenu = this.menuListItem
      this.$store.dispatch('MenuSelect', selectedMenu)
    }
  }
}
</script>

<style scoped>
.small{
  width: 60px;
  height: 60px;
}

.flex{
  display: flex;
  align-items: center;
  justify-content: space-between;
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