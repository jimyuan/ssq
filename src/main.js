import 'normalize.css'
import '@/assets/docs.scss'
import Vue from 'vue'
import FastClick from 'fastclick'
import App from './App.vue'

Vue.config.productionTip = false
FastClick.attach(document.body)

new Vue({
  render: h => h(App)
}).$mount('#app')
