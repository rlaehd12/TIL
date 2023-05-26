<template>
  <div>
    <h1>{{todoitem.title}}</h1>
  </div>
</template>

<script>


export default {
  name: 'TodoListItem',
  props:{
    todoitem: Object,
  }
}
</script>

<style>

</style>