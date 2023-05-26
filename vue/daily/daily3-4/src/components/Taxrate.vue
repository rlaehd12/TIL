<template>
  <div>
    <!-- 없애면 업데이트 안됨 -->
    <h2 style="display:none">{{taxBase}}</h2>
    <!-- 없애면 업데이트 안됨 -->
    <h2>산출 세액: {{after_calc}} </h2>
    <!-- <h2>세액 감면: (-) {{reduction}} </h2> -->
    <hr>
    <Finaltax :reduction="reduction" :after-calc="after_calc" />
  </div>
</template>

<script>
import Finaltax from "@/components/Finaltax.vue";


export default {
  name:'TaxRate',
  components: {
    Finaltax,
  },
  props:{
    taxBase:Number,
    reduction:Number,
  },
  data(){
    return{
      after_calc :0,
    }
  },
  updated(){
    // console.log(this.calc())
    this.after_calc = this.calc()
  },
  methods:{
    calc(){
      console.log(this.$props.reduction)
      if (this.taxBase <= 1200) {
        return Math.round(this.taxBase * 0.06)
      } else if (this.taxBase > 1200 && this.taxBase <= 4600) {
        return Math.round(this.taxBase * 0.15 - 108)
      } else if (this.taxBase > 4600 && this.taxBase <= 8800) {
        return Math.round(this.taxBase * 0.24 - 522)
      } else if (this.taxBase > 8800 && this.taxBase <= 15000) {
        return Math.round(this.taxBase * 0.35 - 1490)
      } else if (this.taxBase > 15000 && this.taxBase <= 30000) {
        return Math.round(this.taxBase * 0.38 - 1940)
      } else if (this.taxBase > 30000 && this.taxBase <= 50000) {
        return Math.round(this.taxBase * 0.4 - 2540)
      } else if (this.taxBase > 50000 && this.taxBase <= 100000) {
        return Math.round(this.taxBase * 0.42 - 3540)
      } else {
        return Math.round(this.taxBase * 0.45 - 6540)
      }
    },
  },
}
</script>

<style>

</style>