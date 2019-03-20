<template lang="html">
  <div class="ssq-block">
    <div class="item-title">统计数据</div>
    <div class="item-label">样本数量：</div>
    <div class="item-value item-tongji">
      <input type="range" class="jr" :min="min" :max="max" v-model="sampleCount" step="10">
      近 {{sampleCount}} 期
    </div>

    <div class="item-row tongji-btn">
      <button class="btn" @click="handleData">闪亮赋能</button>
    </div>
    <div class="item-row">

    </div>
  </div>
</template>

<script>
export default {
  name: 'ssq-analy',
  props: {
    ssq: {
      type: Array,
      require: true
    }
  },
  data () {
    return {
      sampleCount: 100,
      min: 10,
      redBallsGroup: [],
      blueBallsGroup: []
    }
  },
  computed: {
    max () {
      return this.ssq.length
    }
  },
  methods: {
    handleData () {
      const ssq = [...this.ssq]
      const sampleCount = this.sampleCount
      let tmpBall = null
      if (this.max > sampleCount) ssq.length = sampleCount
      this.redBallsGroup = []
      this.blueBallsGroup = []
      for (let ball of ssq) {
        for (let num = 1; num <= 7; num++) {
          tmpBall = ball[num]
          if (num === 7) {
            this.blueBallsGroup.push(tmpBall)
          } else {
            this.redBallsGroup.push(tmpBall)
          }
        }
      }
    }
  },
  mounted () {
  }
}
</script>
