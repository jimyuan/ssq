<template lang="html">
  <!-- 手工选号结果   -->
  <section class="ssq-block">
    <div class="item-title">选取结果</div>
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
  </section>
</template>

<script>

export default {
  props: {
    bets: {
      type: Object,
      require: true
    }
  },
  computed: {
    // 选中的红球
    redBalls () {
      return this.bets.red
    },
    // 选中的兰球
    blueBalls () {
      return this.bets.blue
    }
  }
}
</script>
