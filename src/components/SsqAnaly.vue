<template lang="html">
  <section class="ssq-block">
    <div class="item-title">统计数据</div>
    <div class="item-label">样本数量：</div>
    <div class="item-value item-tongji">
      <input type="range" class="jr" :min="min" :max="max" v-model="sampleCount" step="10">
      近 {{sampleCount}} 期
    </div>
    <!-- button 查询指定期数内的双色球出现频率 -->
    <div class="item-row tongji-btn">
      <button class="btn" @click="handleData">闪亮赋能</button>
    </div>
    <!-- 红球统计数据 -->
    <div class="item-row" v-if="redBallsCount.length>0">
      <p class="text-red">红球统计数据：</p>
      <span class="count-ball red-ball"
        :class="{selected: pickedRedBalls.indexOf(ball[0])>-1}"
        v-for="ball of redBallsCount"
        :key="`red-${ball[0]}`"
        @click="pickBalls(ball[0], false)">
          {{ ball[0] }}({{ ball[1] }})
      </span>
    </div>
    <!-- 篮球统计数据 -->
    <div class="item-row" v-if="blueBallsCount.length>0">
      <p class="text-blue">篮球统计数据：</p>
      <span class="count-ball blue-ball"
        :class="{selected: pickedBlueBalls.indexOf(ball[0])>-1}"
        v-for="ball of blueBallsCount"
        :key="`blue-${ball[0]}`"
        @click="pickBalls(ball[0])">
          {{ ball[0] }}({{ ball[1] }})
      </span>
    </div>
  </section>
</template>

<script>
/**
 * 统计各色球的出现次数，然后按照降序排列
 * @param  {Array} arr 各期开球数据
 * @return {Array}     排完序的结果，例如 [[a,5],[b,3],[c,2]]
 */
const sortable = arr => {
  const ballsCount = arr.reduce((elements, ele) => {
    ele in elements ? elements[ele]++ : (elements[ele] = 1)
    return elements
  }, {})
  return Array.from([...new Set(arr)])
    .sort((a, b) => ballsCount[b] - ballsCount[a])
    .map(item => [item, ballsCount[item]])
}

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
      // 指定期数的所有红球号
      redBallsGroup: [],
      // 指定期数的所有兰球号
      blueBallsGroup: [],
      pickedRedBalls: [],
      pickedBlueBalls: []
    }
  },
  computed: {
    max () {
      return this.ssq.length
    },
    redBallsCount () {
      return sortable(this.redBallsGroup)
    },
    blueBallsCount () {
      return sortable(this.blueBallsGroup)
    }
  },
  methods: {
    /**
     * 按钮事件，获取最新期数中的红篮球出现次数
     */
    handleData () {
      // 每次按键都需要初始化以下变量
      this.redBallsGroup = []
      this.blueBallsGroup = []
      this.pickedRedBalls = []
      this.pickedBlueBalls = []
      this.$store.commit('updatePickedBalls', {
        red: [], blue: []
      })

      // 获取父组件传来的完整历史数据
      const ssq = [...this.ssq]
      // 设定要选取的数据长度，默认 100 期
      const sampleCount = this.sampleCount
      if (this.max > sampleCount) ssq.length = sampleCount

      for (let ball of ssq) {
        for (let num = 1; num <= 7; num++) {
          num === 7
            ? this.blueBallsGroup.push(ball[num])
            : this.redBallsGroup.push(ball[num])
        }
      }
    },
    /**
     * 下注选球
     * @param  {Number}  num             [description]
     * @param  {Boolean} [blueFlag=true] [description]
     */
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
      // 将选中的数据存入 store
      this.$store.commit('updatePickedBalls', {
        red: this.pickedRedBalls,
        blue: this.pickedBlueBalls
      })
    }
  }
}
</script>
