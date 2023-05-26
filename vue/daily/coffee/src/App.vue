<template>
  <div id="app">
    <h1>Coffee Order App</h1>
    <div class="menu-size">
      <MenuList class="col-6"/>
      <SizeList class="col-6"/>
    </div>
    <OrderList/>
  </div>
</template>

<script>
import MenuList from "@/components/MenuList.vue";
import SizeList from "@/components/SizeList.vue";
import OrderList from "@/components/OrderList.vue";

export default {
  name: 'App',
  components: {
    MenuList,
    SizeList,
    OrderList,
  }
}
</script>

<style>
.menu-size {
  display: flex;
  justify-content: space-between;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  color: #2c3e50;
  margin-top: 30px;
}

#app{
  text-align: center;
}
</style>
