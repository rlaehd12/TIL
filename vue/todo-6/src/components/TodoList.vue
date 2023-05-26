<template>
  <div>


    <div class="border m-2 d-flex justify-content-between">
      <div class="m-2" @click="ChangeComplete">
        {{todoItem.isCompleted}}
        {{todoItem.content}}
      </div>
      <div class="m-2" @click="ChangeImportant">
        <div :class="{star:todoItem.isImportant, checked:!todoItem.isImportant}"
        ></div>
      </div>
    </div>


  </div>
</template>

<script>
export default {
  name:'TodoList',
  props:{
    todoItem:Object
  },
  methods:{
    ChangeImportant(){
      this.$store.dispatch('ChangeImportant',this.todoItem)
    },
    ChangeComplete(){
      this.$store.dispatch('ChangeComplete',this.todoItem)
    }
  }
}
</script>

<style>

</style>