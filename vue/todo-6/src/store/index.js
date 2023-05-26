import Vue from 'vue'
import Vuex from 'vuex'
import todo from './modules/todo'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    id:16387715533779
  },
  getters: {
  },
  mutations: {
    SAVE_TODO_DATA(state, input){
      this.state.id += 1
      // get date===================================================================
      const currentDate = new Date();
      const currentYear = currentDate.getFullYear();
      const currentMonth = String(currentDate.getMonth() + 1).padStart(2, '0'); // Zero-padding the month value
      const currentDay = String(currentDate.getDate()).padStart(2, '0'); // Zero-padding the day value


      // year, month, day, hours, minutes, seconds
      const date_formatter = new Date(currentYear, currentMonth, currentDay)
      
      console.log("date_formatter.format('YYYY-mm-dd')", date_formatter)
      console.log(`${currentYear}-${currentMonth}-${currentDay}T00:00`);
      const date = `${currentYear}-${currentMonth}-${currentDay}T00:00`
      // =========================================================================
      
      const curid = this.state.id
      const curdata={
        id:curid,
        content:input,
        dueDateTime:date,
        isCompleted:false,
        isImportant:false,
      }
      state.todo.list.push(curdata)
    },
    CHANGE_IMPORTANT(state, obj){
      for (const todo of state.todo.list) {
        if (todo === obj) {
          // console.log(obj.isImportant);
          obj.isImportant = !obj.isImportant
        }
      }
    },
    CHANGE_COMPLETE(state, obj){
      for (const todo of state.todo.list) {
        if (todo === obj) {
          obj.isCompleted = !obj.isCompleted
        }
      }
    },

  },
  actions: {
    SaveTodoData(context, input){
      // console.log(input);
      context.commit('SAVE_TODO_DATA', input)
    },
    ChangeImportant(context, obj){
      context.commit('CHANGE_IMPORTANT', obj)
    },
    ChangeComplete(context, obj){
      context.commit('CHANGE_COMPLETE', obj)
    }
  },
  modules: {
    todo
  }
})
