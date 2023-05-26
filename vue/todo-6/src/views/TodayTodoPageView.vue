<template>
  <div>


    <h1 class="m-2">오늘 할일</h1>
    <hr class="m-2">
    {{today}}
    <div v-for="(todo, index) in todo_lst" :key="index">
      <TodoList v-if="todo.dueDateTime.substring(0,10) === today"
      :todo-item="todo"/>
    </div>


  </div>
</template>

<script>
import TodoList from "@/components/TodoList.vue";

export default {
  name:'TodayTodoPageView',
  components:{
    TodoList
  },
  computed:{
    todo_lst(){
      return this.$store.state.todo.list
    },
    today(){
      const today_date = new Date()
      const currentYear = today_date.getFullYear();
      const currentMonth = String(today_date.getMonth() + 1).padStart(2, '0'); // Zero-padding the month value
      const currentDay = String(today_date.getDate()).padStart(2, '0'); // Zero-padding the day value

      console.log(`${currentYear}-${currentMonth}-${currentDay}`);
      return `${currentYear}-${currentMonth}-${currentDay}`
    }
  },
}
</script>

<style>

</style>