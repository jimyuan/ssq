<template>
  <section id="app">
    <ssq-info :ssq="ssq" v-if="ssq.length>0"></ssq-info>
    <ssq-analy :ssq="ssq" v-if="ssq.length>0"></ssq-analy>
  </section>
</template>

<script>
import axios from 'axios'
import SsqInfo from '@/components/SsqInfo'
import SsqAnaly from '@/components/SsqAnaly'
export default {
  name: 'app',
  data () {
    return {
      ssq: []
    }
  },
  components: { SsqInfo, SsqAnaly },
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
