<template>
  <section id="app">
    <ssq-info :ssq="ssq" v-if="ssq.length>0"></ssq-info>
    <ssq-analy :ssq="ssq" v-if="ssq.length>0"></ssq-analy>
    <picked-bets :bets="pickedBalls" v-if="validResults"></picked-bets>
    <bets-detail :bets="pickedBalls" v-if="validResults"></bets-detail>
    <div class="loading" v-if="loadingFlag">
      <img src="loading.svg" alt="loading">
      <span>数据加载中...</span>
    </div>
  </section>
</template>

<script>
import axios from 'axios'
import SsqInfo from '@/components/SsqInfo'
import SsqAnaly from '@/components/SsqAnaly'
import PickedBets from '@/components/PickedBets'
import BetsDetail from '@/components/BetsDetail'
export default {
  name: 'app',
  data () {
    return {
      ssq: [],
      loadingFlag: true
    }
  },
  components: { SsqInfo, SsqAnaly, PickedBets, BetsDetail },
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
    this.loadingFlag = true
    axios({
      url: 'data.txt',
      responseType: 'text'
    }).then(req => {
      this.ssq = req.data.replace(/\n$/, '').split('\n').map(item => item.split(','))
      this.loadingFlag = false
    })
  }
}
</script>
