<template lang="html">
  <div class="ssq-block" v-if="ssq.length>0">
    <div class="item-title">基础信息</div>
    <div class="item-label">历史期数：</div>
    <div class="item-value" v-text="ssq.length"></div>
    <div class="item-label">时间范围：</div>
    <div class="item-value">
      <strong>{{ssqNew[ssqCol-1]}}</strong> ~
      <strong>{{ssqOld[ssqCol-1]}}</strong>
    </div>
    <div class="item-label">最新期号：</div>
    <div class="item-value" v-text="ssqNew[0]"></div>
    <div class="item-label">最新结果：</div>
    <div class="item-value">
      <span class="item-ball"
        v-for="(ball, idx) of ssqNewBalls"
        :key="idx"
        v-text="ball"></span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ssq-info',
  props: {
    ssq: {
      type: Array,
      require: true
    }
  },
  computed: {
    ssqNew () {
      return this.ssq[0]
    },
    ssqOld () {
      const ssq = [...this.ssq]
      return ssq.pop()
    },
    ssqCol () {
      return this.ssq[0].length
    },
    ssqNewBalls () {
      return this.ssq[0].filter((val, idx) => (idx > 0 && idx < 8))
    }
  }
}
</script>
