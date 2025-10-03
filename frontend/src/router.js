import { createRouter, createWebHistory } from 'vue-router'
import Chat from './components/Chat.vue'
import Dashboard from './components/Dashboard.vue'
import Receita from './components/Receita.vue'

export default createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: Chat },
    { path: '/dashboard', component: Dashboard },
    { path: '/receita', component: Receita }
  ]
})
