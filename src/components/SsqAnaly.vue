<template lang="html">
  <div class="ssq-block">
    <div class="item-title">统计数据</div>
    <div class="item-label">样本数量：</div>
    <div class="item-value item-tongji">
      <input type="range" class="jr" :min="min" :max="max" v-model="sampleCount" step="10">
      近 {{sampleCount}} 期
    </div>

    <div class="item-row tongji-btn">
      <button class="btn">神啊，请赐予我靓号吧！</button>
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
      min: 10
    }
  },
  computed: {
    max () {
      return this.ssq.length
    }
  },
  methods: {
    adjustSample () {

    }
  },
  mounted () {
  }
}
</script>
