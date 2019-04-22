import 'normalize.css'
import '@/assets/docs.scss'
import Vue from 'vue'
import FastClick from 'fastclick'
import App from './App.vue'
import store from './store'

Vue.config.productionTip = false
FastClick.attach(document.body)

new Vue({
  store,
  render: h => h(App)
}).$mount('#app')
