import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    messsage: 'message in store'
  },
  getters: {
    messageLength(state){
      return state.messsage.length
    },
    doubleLenght(state, getters){
      console.log(getters.messageLength);
      return getters.messageLength * 2
    },
  },
  mutations: {
    CHANGE_MESSAGE(state, msg){
      // console.log(state);
      // console.log(msg);
      state.messsage = msg
    }
  },
  actions: {
    changeMessage(context, message){
      // console.log(context, message);
      context.commit('CHANGE_MESSAGE', message)
    }
  },
  modules: {
  }
})
