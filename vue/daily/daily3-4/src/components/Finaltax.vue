<template>
  <div>
    <h2>결정 세액: {{afterCalc-reduction}}</h2>
  </div>
</template>

<script>
export default {
    name:'FinalTax',
    props:{
        afterCalc:Number,
        reduction:Number
    }
}
</script>

<style>

</style>