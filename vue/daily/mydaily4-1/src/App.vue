<template>
  <div id="app">
    <!-- <h1 class="fw-bold my-4">버튼 박스 제작</h1>
    <div id="date-box" class="col-6 shadow p-3 mb-5 bg-body rounded m-auto">
      <h2 class="mb-5 fw-bold">예약 페이지</h2>
      <h3 class="my-3 fw-bold">시간 선택</h3>
      <span v-for="(time,idx) in times" v-bind:key="idx">
        <br v-if="idx%8 ===0 && idx!==0">
        <span @click="span_click(idx)" @mouseover="span_mouseover" @mouseleave="span_mouseleave" class="px-2 py-2" :data-id="idx">
          {{time}}
        </span>
      </span>
      <hr>
      <div class="fw-bold">
        선택 시간 : 
        <span v-for="(el,idx) in mylst" v-bind:key="idx"> {{times[el]}} </span>
      </div>
    </div> -->
  <HelloWorld/>
  </div>
</template>

<script>
import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: 'App',
  components: {
      HelloWorld,
    },
  // data : function () {
  // },
  data(){  // 메서드 단축 표현
    return{
      mylst:[],
      times: [
  "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
  "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
  "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
      ],
      visited:new Array(100)
      
    }
  },
  methods:{
    span_click: function (idx) {
      console.log('idx', idx);
      console.log(this.times[idx])
      if (this.mylst.length<5 && this.visited[idx]===undefined) {
        this.visited[idx] = 1
        this.mylst.push(idx)
      } else{
        alert('중복 or 5개이상')
      }
      console.log(this.mylst);

    },
    span_mouseover: function (idx) {
      // console.log(idx.target.dataset.id);
      idx.target.setAttribute('style', 'background-color: #658dc63d;')
    },
    span_mouseleave: function (idx) {
      idx.target.setAttribute('style', '')
    },
  },
  mounted(){},
  created(){},

}


</script>

<style>
@import url(http://fonts.googleapis.com/earlyaccess/notosanskr.css);

.test{ width:300px; font-size:14px;}
.active{ font-family:'Noto Sans KR', sans-serif ; }

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #424242;
  margin-top: 60px;
}
</style>
