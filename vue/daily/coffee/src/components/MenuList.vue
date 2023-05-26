<template>
  <div>
    <h1>1. 음료를 고르세요</h1>
    <div>
      <MenuListItem :menu-list-item = "item"
      v-for="(item, index) in MenuItem" :key="index"
      class="menu-box"
      />
    </div>
  </div>
</template>

<script>
import MenuListItem from "@/components/MenuListItem.vue";

export default {
  name:'MenuList',
  components:{
    MenuListItem,
  },
  computed:{
    MenuItem(){
      return this.$store.state.menuList
    }
  }
}
</script>

<style scoped>

</style>