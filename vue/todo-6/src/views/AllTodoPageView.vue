<template>
  <div>
    <!-- 제목=============================== -->
    <h1 class="m-2">모든 할일</h1>
    <div class="m-2 d-flex align-self-center">
    <!-- 제목 끝=============================== -->
      <h3 class="m-0">+</h3>
      <input type="text" class="form-control form-control-sm mx-2" v-model="InputData"
      placeholder="할 일을 작성해 주세요!"
      @keyup.enter="SaveInputData">
    </div>
    <hr class="m-2">

    <!-- for문...................... -->
    <!-- <div v-for="(todo, index) in todo_lst" :key="index"
    class="border m-2 d-flex justify-content-between"
    >
      <div class="m-2">
        {{todo.isCompleted}}
        {{todo.content}}
      </div>
      <div class="m-2">
        {{todo.isImportant}}
      </div>
    </div> -->
    <!-- for문끝...................... -->
    <!-- component로 바꿔서 다 가져다 쓰게 -->
    <TodoList
    v-for="(todo, index) in todo_lst" :key="index"
    :todo-item="todo"
    />
    <!-- component로 바꿔서 다 가져다 쓰게 -->

  </div>
</template>

<script>
import TodoList from "@/components/TodoList.vue";

export default {
  name:'AllTodoPageView',
  components:{
    TodoList
  },
  computed:{
    todo_lst(){
      return this.$store.state.todo.list
    }
  },
  data(){
    return{
      InputData:null
    }
  },
  methods:{
    SaveInputData(){
      // console.log(this.InputData);
      this.$store.dispatch('SaveTodoData', this.InputData)
      this.InputData = null
    }
  }
}
</script>

<style scoped>
.star {
    visibility:hidden;
    font-size:30px;
    cursor:pointer;
}
.star:before {
  color: orange;
  content: "\2605";
  position: absolute;
  visibility:visible;
}
.star:checked:before {
  content: "\2606";
  color: orange;
  position: absolute;
}
</style>