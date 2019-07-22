<template>
  <section id="app">
    <ssq-info :ssq="ssq" v-if="ssq.length>0"></ssq-info>
    <ssq-analy :ssq="ssq" v-if="ssq.length>0"></ssq-analy>
    <picked-bets :bets="pickedBalls" v-if="validResults"></picked-bets>
    <bets-detail :bets="pickedBalls" v-if="validResults"></bets-detail>
    <!-- loading icon -->
    <div class="loading" v-if="loadingFlag">
      <svg viewBox="0 0 1024 1024" version="1.1" width="81" height="81">
        <path d="M512 1024c-113.777778 0-221.866667-34.133333-307.2-102.4-39.822222-28.444444-45.511111-79.644444-17.066667-119.466667 28.444444-39.822222 79.644444-45.511111 119.466667-17.066666 56.888889 45.511111 130.844444 68.266667 204.8 68.266666 187.733333 0 341.333333-153.6 341.333333-341.333333s-153.6-341.333333-341.333333-341.333333-341.333333 153.6-341.333333 341.333333c0 45.511111-39.822222 85.333333-85.333334 85.333333S0 557.511111 0 512c0-284.444444 227.555556-512 512-512s512 227.555556 512 512-233.244444 512-512 512z"></path>
      </svg>
      <span>数据加载中...</span>
    </div>
  </section>
</template>

<script>
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
    const xhr = window.XMLHttpRequest
      ? new XMLHttpRequest()
      : window.ActiveXObject('microsoft.XMLHttp')
    xhr.open('get', 'data.txt', true)
    xhr.send()
    xhr.onreadystatechange = () => {
      const { readyState, status, responseText } = xhr
      if (readyState === 4 && (status === 200 || status === 304)) {
        this.ssq = responseText.replace(/\n$/, '').split('\n').map(item => item.split(','))
        this.loadingFlag = false
      }
    }
  }
}
</script>
