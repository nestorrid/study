import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import HeaderVue from './components/Header.vue'


const app = createApp(App)

app.component('Header', HeaderVue)

app.mount('#app')
