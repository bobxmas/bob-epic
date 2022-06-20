<template>
  <div>
    <p>없어짐</p>
    <el-button @click="service_a">"/api/a" 호출</el-button>
    <el-tooltip effect="dark" placement="top"><div slot="content" style="text-align: left;">Canary Depolyment Test<br /><br />v1: a ▶ b ▶ c<br /> v2: a ▶ b ▶ papago</div><el-button @click="service_ab" type="warning">"/api/a/b" 호출</el-button></el-tooltip>
    <el-button @click="service_abtest">"/api/a/b/test" 호출</el-button>
    <el-button @click="service_ac">"/api/c" 호출</el-button>
    <el-input type="textarea" :rows="5" placeholder="Response of API" v-html="res_obj.data" style="border: 1px solid #eee; height: 250px;" readonly />
  </div>
</template>
<script>
import { callA, callAB, callABTest, callAC } from '../api/service'

export default {
  name: 'Home',
  components: { },
  props: {
    msg: String
  },
  data () {
    return {
      res_obj: {data: "Response of API"}
    }
  },
  methods : {
    service_a() {
      let token = localStorage.getItem("access_token")
      callA(token).then(res => {this.res_obj = res})
    },
    service_ab() {
      let token = localStorage.getItem("access_token")
      callAB(token).then(res => {this.res_obj = res})
    },
    service_abtest() {
      let token = localStorage.getItem("access_token")
      callABTest(token).then(res => {this.res_obj = res})
    },
    service_ac() {
      let token = localStorage.getItem("access_token")
      callAC(token).then(res => {this.res_obj = res})
    }
  }
}
</script>