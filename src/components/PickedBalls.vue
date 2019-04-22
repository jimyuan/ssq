<template lang="html">
  <!-- 手工选号结果   -->
  <div class="ssq-block">
    <div class="item-title">选取结果 <small v-if="validBets">（共 <strong v-html="betsCount" class="text-red"></strong> 注）</small></div>
    <transition-group name="list-complete" tag="div" class="item-row">
      <!-- 红球 -->
      <span class="count-ball red-ball selected list-complete-item"
      v-for="ball of redBalls" :key="`red-${ball}`"
      v-text="ball"></span>
      <!-- 兰球 -->
      <span class="count-ball blue-ball selected list-complete-item"
      v-for="ball of blueBalls" :key="`blue-${ball}`"
      v-text="ball"></span>
    </transition-group>
    <div class="item-row tongji-btn" v-if="validBets">
      <button class="btn" @click="handleData">下注详情</button>
    </div>
  </div>
</template>

<script>
/**
 * 阶乘算法
 */
const fact = num => {
  if (num < 0) return -1
  if (num <= 1) return 1
  return num * fact(num - 1)
}

/**
 * 组合算法
 */
const comb = (m, n) => {
  return fact(m) / fact(m - n) / fact(n)
}

export default {
  props: {
    balls: {
      type: Object,
      require: true
    }
  },
  computed: {
    // 达到投注要求
    validBets () {
      return this.redBalls.length > 5 && this.blueBalls.length > 0
    },
    // 选中的红球
    redBalls () {
      return this.balls.red
    },
    // 选中的兰球
    blueBalls () {
      return this.balls.blue
    },
    // 计算注数
    betsCount () {
      const r = comb(this.redBalls.length, 6)
      const b = this.blueBalls.length
      return `${r} &times; ${b} = ${r * b}`
    }
  },
  methods: {
    handleData () {}
  }
}
</script>
