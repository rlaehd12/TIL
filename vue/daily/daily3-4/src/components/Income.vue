<template>
  <div class="wrapper">
    연봉 입력 (만원): <input type="text" v-model.number="total_salary">
    <br>
    세액감면액 (만원): <input type="text" v-model.number="reduction">
    <hr>
      <div>
        <h2>종합소득금액 : {{total_salary}}</h2>
        <h2>종합소득공제 : (-) {{income_deduction}}</h2>
        <h2> 과세표준 : {{computed_value}}</h2>
        <h2> 과세표준 : {{computed_value}}</h2>

      </div>
    <hr>
    <Taxrate :tax-base="total_salary-income_deduction" :reduction="reduction"/>

  </div>
</template>

<script>
import Taxrate from "@/components/Taxrate.vue";


export default {
  name:'InCome',
  components: {
  Taxrate,
  },
  data(){
    return{
      total_salary:0,
      reduction:0,
      income_deduction: 150
    }
  },computed:{
    computed_value(){
      // console.log('computed');
      return this.total_salary-this.income_deduction >0? this.total_salary-this.income_deduction : 0
    }
  },



}
</script>

<style>
.wrapper{
  text-align: center;
}
</style>