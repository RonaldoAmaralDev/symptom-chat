import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import './assets/app.css'
import './assets/chat.css'

import "vue3-toastify/dist/index.css";
import Vue3Toastify from "vue3-toastify";

const app = createApp(App)

app.use(Vue3Toastify, {
  position: "top-right",
  autoClose: 4000,
});

app.use(router)
app.mount('#app')