<template>
  <div>
    <h1>2. 2080!</h1>
    <div class="fade" :class="{show:IsMenuSelected, active:IsMenuSelected}">
      <SizeListItem
      v-for="(item, index) in SizeItem" :key="index"
      :size-list-item="item"
      />
    </div>
  </div>
</template>

<script>
import SizeListItem from "@/components/SizeListItem.vue";

export default {
  name:'SizeList',
  components:{
    SizeListItem
  },
  computed:{
    SizeItem(){
      return this.$store.state.sizeList
    },
    IsMenuSelected(){
      let count = 0  // count가 0보다 크면 1개 이상 메뉴 선택했다는 거니까 true 반환
      this.$store.state.menuList.map((item)=>{
        if (item.selected) {
          count += 1
        }
      })
      return count ? true : false
    }
  },
}
</script>

<style>

</style>