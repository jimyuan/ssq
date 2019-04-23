<template lang="html">
  <div class="ssq-block" v-if="ssq.length>0">
    <div class="item-title">基础信息</div>
    <div class="item-label">历史期数：</div>
    <div v-text="ssq.length"></div>
    <div class="item-label">时间范围：</div>
    <div class="item-value">
      <strong>{{ssqNew.slice(-1)[0]}}</strong> ~
      <strong>{{ssqOld.slice(-1)[0]}}</strong>
    </div>
    <div class="item-label">最新期号：</div>
    <div v-text="ssqNew[0]"></div>
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
    // 最新一期数据
    ssqNew () {
      return this.ssq[0]
    },
    // 最早一期数据
    ssqOld () {
      return this.ssq.slice(-1)[0]
    },
    // 最新一期中奖信息
    ssqNewBalls () {
      return this.ssqNew.filter((val, idx) => (idx > 0 && idx < 8))
    }
  }
}
</script>
