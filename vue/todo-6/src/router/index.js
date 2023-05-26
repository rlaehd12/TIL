import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'AllTodoPageView',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "all" */ '../views/AllTodoPageView.vue')
  },
  {
    path: '/today',
    name: 'TodayTodoPageView',
    component: () => import(/* webpackChunkName: "today" */ '../views/TodayTodoPageView.vue')
  },
  {
    path: '/important',
    name: 'ImportantTodoPageView',
    component: () => import(/* webpackChunkName: "important" */ '../views/ImportantTodoPageView.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
