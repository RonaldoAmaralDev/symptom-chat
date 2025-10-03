import { createRouter, createWebHistory } from 'vue-router'
import Chat from './components/Chat.vue'
import Agent from './components/Agent.vue'
import Dashboard from './components/Dashboard.vue'
import Receita from './components/Receita.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: Chat },
    { path: '/agent', component: Agent },
    { path: '/dashboard', component: Dashboard },
    { path: '/receita', component: Receita }
  ]
})

export default router