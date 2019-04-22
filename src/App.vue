<template>
  <section id="app">
    <ssq-info :ssq="ssq" v-if="ssq.length>0"></ssq-info>
    <ssq-analy :ssq="ssq" v-if="ssq.length>0"></ssq-analy>
    <picked-balls :balls="pickedBalls" v-if="validResults"></picked-balls>
  </section>
</template>

<script>
import axios from 'axios'
import SsqInfo from '@/components/SsqInfo'
import SsqAnaly from '@/components/SsqAnaly'
import PickedBalls from '@/components/PickedBalls'
export default {
  name: 'app',
  data () {
    return {
      ssq: []
    }
  },
  components: { SsqInfo, SsqAnaly, PickedBalls },
  computed: {
    pickedBalls () {
      return this.$store.state.pickedBalls
    },
    validResults () {
      const { red, blue } = this.pickedBalls
      return red.length + blue.length > 0
    }
  },
  created () {
    axios({
      url: 'data.txt',
      responseType: 'text'
    }).then(req => {
      this.ssq = req.data.replace(/\n$/, '').split('\n').map(item => item.split(','))
    })
  }
}
</script>
