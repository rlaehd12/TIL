<template>
  <div class="border">
    <h1>This is 마이 Component</h1>
    <MyChild/>
    <MyChild/>
    <MyChild/>
    <MyChild/>
    <MyChild/>
  </div>
</template>

<script>
import MyChild from './MyChild.vue'
export default { // 컴포넌트 이름 설정
  name: "MyComponent",
  components: {
    MyChild,
  }
}
</script>

<style>
.border{
  border: solid;
}
</style>