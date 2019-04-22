import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    pickedBalls: {
      red: [],
      blue: []
    }
  },
  mutations: {
    updatePickedBalls (state, data) {
      state.pickedBalls = {
        red: data.red,
        blue: data.blue
      }
    }
  },
  actions: {

  }
})
