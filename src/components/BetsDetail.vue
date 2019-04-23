<template>
  <section class="ssq-block">
    <div class="item-title">投注详情  <small v-if="validBets">（共 <strong v-html="betsCount" class="text-red"></strong> 注）</small></div>
    <div class="item-row text-red" v-if="!validBets">请至少选择 6 个红球和 1 个兰球</div>
    <template v-else>
      <template v-for="(bet, idx) of betsDetails">
        <span class="bets-num" :key="idx">{{idx+1}} . </span>
        <div :key="`bet-${idx}`">
          <span v-for="(ball, index) of bet" :key="`ball-${index}`" class="item-ball" v-text="ball"></span>
        </div>
      </template>
    </template>
  </section>
</template>

<script>
import { comb, arrayCombine } from '@/utils'
export default {
  props: {
    bets: {
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
      return this.bets.red
    },
    // 选中的兰球
    blueBalls () {
      return this.bets.blue
    },
    // 计算注数
    betsCount () {
      const r = comb(this.redBalls.length, 6)
      const b = this.blueBalls.length
      return `${r} &times; ${b} = ${r * b}`
    },
    // 投注详情
    betsDetails () {
      const [redBets, blueBets] = [arrayCombine(this.redBalls, 6), this.blueBalls]
      const [rLen, bLen] = [redBets.length, blueBets.length]
      return Array.from({ length: rLen * bLen }, (v, i) => [...redBets[i % rLen], blueBets[i % bLen]])
    }
  }
}
</script>
