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
      <span class="count-ball red-ball"
        v-for="(ball, idx) of redBallsUnit"
        :key="idx"
        @click="pickBalls(ball, false)">
          {{ball}}({{redBallsCount[ball]}})
      </span>
    </div>
    <div class="item-row">
      <span class="count-ball blue-ball"
        v-for="(ball, idx) of blueBallsUnit"
        :key="idx"
        @click="pickBalls(ball)">
        {{ball}}({{blueBallsCount[ball]}})
      </span>
    </div>
    <template v-if="pickedRedBalls.length>0 || pickedBlueBalls.length>0">
      <div class="item-title">选取结果</div>
      <div class="item-row">
        <span class="count-ball red-ball" v-for="(ball, idx) of pickedRedBalls">{{ball}}</span>
        <span class="count-ball blue-ball" v-for="(ball, idx) of pickedBlueBalls">{{ball}}</span>
      </div>
    </template>
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
      blueBallsGroup: [],
      pickedRedBalls: [],
      pickedBlueBalls: []
    }
  },
  computed: {
    max () {
      return this.ssq.length
    },
    redBallsUnit () {
      return [...new Set(this.redBallsGroup)].sort()
    },
    blueBallsUnit () {
      return [...new Set(this.blueBallsGroup)].sort()
    },
    redBallsCount () {
      return this.redBallsGroup.reduce((elements, ele) => {
        ele in elements ? elements[ele]++ : (elements[ele] = 1)
        return elements
      }, {})
    },
    blueBallsCount () {
      return this.blueBallsGroup.reduce((elements, ele) => {
        ele in elements ? elements[ele]++ : (elements[ele] = 1)
        return elements
      }, {})
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
    },
    pickBalls (num, blueFlag = true) {
      if (blueFlag) {
        const idx = this.pickedBlueBalls.indexOf(num)
        if (idx === -1) {
          this.pickedBlueBalls.push(num)
          this.pickedBlueBalls.sort()
        } else {
          this.pickedBlueBalls.splice(idx, 1)
        }
      } else {
        const idx = this.pickedRedBalls.indexOf(num)
        if (idx === -1) {
          this.pickedRedBalls.push(num)
          this.pickedRedBalls.sort()
        } else {
          this.pickedRedBalls.splice(idx, 1)
        }
      }
    }
  },
  mounted () {
  }
}
</script>
