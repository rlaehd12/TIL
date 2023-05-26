<template>
  <div>
    <nav>
      <!--  -->
      <div>
        <h1><router-link to="/">모든</router-link></h1>
      </div>
      <div>
        <h1><router-link :to="{name:'TodayTodoPageView'}">오늘</router-link></h1>
      </div>
      <div>
        <h1><router-link :to="{name:'ImportantTodoPageView'}">중요</router-link></h1>
      </div>

      <!-- <ul>
        <li @click="pass_router('ALL')">모든</li>
        <li>오늘</li>
        <li>중요</li>
      </ul> -->

    </nav>
  </div>
</template>

<script>
export default {

methods:{
  pass_router(route_name){
    this.$emit('pass_router', route_name)
  }
}
}
</script>

<style scoped>
nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>