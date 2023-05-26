<template>
  <div>


    <h1 class="m-2">중요 할일</h1>
    <hr class="m-2">
    <div v-for="(todo, index) in todo_lst" :key="index">
      <TodoList v-if="todo.isImportant"
      :todo-item="todo"/>
    </div>


  </div>
</template>

<script>
import TodoList from "@/components/TodoList.vue";

export default {
  name:'ImportantTodoPageView',
  components:{
    TodoList
  },
  computed:{
    todo_lst(){
      return this.$store.state.todo.list
    }
  },
  
}
</script>

<style>

</style>