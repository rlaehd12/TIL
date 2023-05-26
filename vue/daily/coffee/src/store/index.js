import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    orderList:[],
    menuList:[
      {
        title:'아메리카노',
        price:3000,
        selected:false,
        image:'https://source.unsplash.com/featured/?americano',
      },
      {
        title:'라떼',
        price:4000,
        selected:false,
        image:'https://source.unsplash.com/featured/?latte',
      },
      {
        title:'카푸치노',
        price:4500,
        selected:false,
        image:'https://source.unsplash.com/featured/?cappuccino',
      },
    ],
    sizeList:[
      {
        name:'small',
        price:0,
        selected:false,
      },
      {
        name:'medium',
        price:500,
        selected:false,
      },
      {
        name:'large',
        price:1000,
        selected:false,
      },
    ]

  },
  getters: {
  },
  mutations: {
    UpdateMenuList(state, selectedMenu){
      state.menuList.map((menuItem)=>{
        if (menuItem === selectedMenu) {
          menuItem.selected = !menuItem.selected
          // console.log(menuItem.selected);
        }
      })
    },

    UpdateSizeList(state, selectedSize){
      state.sizeList.map((SizeItem)=>{
        if (SizeItem === selectedSize) {
          SizeItem.selected = !SizeItem.selected
          // console.log(menuItem.selected);
        }
      })
    },
    // addOrder(state, Order){

    // },
  },
  actions: {


    MenuSelect(context, selectedMenu){
      for (const menu of this.state.menuList) {  // 메뉴 선택했는지 안했는지 확인
        if (menu.selected && menu === selectedMenu) {  // 만약 이미 선택한 메뉴랑 같은거 선택하면
          context.commit('UpdateMenuList', selectedMenu)
          return
        }
        else if(menu.selected){
          context.commit('UpdateMenuList', menu)
          context.commit('UpdateMenuList', selectedMenu)
          return
        }
      }
      context.commit('UpdateMenuList', selectedMenu)
    },
    
    
    SizeSelect(context, selectedSize){
      for (const size of this.state.sizeList) {  // 메뉴 선택했는지 안했는지 확인
        if (size.selected && size === selectedSize) {  // 만약 이미 선택한 메뉴랑 같은거 선택하면
          context.commit('UpdateSizeList', selectedSize)
          return
        }
        else if(size.selected){  // 만약 선택된 다른 메뉴가 있다면
          context.commit('UpdateSizeList', size)
          context.commit('UpdateSizeList', selectedSize)
          return
        }
      }
      context.commit('UpdateSizeList', selectedSize)
    },
  },
  modules: {
  }
})
