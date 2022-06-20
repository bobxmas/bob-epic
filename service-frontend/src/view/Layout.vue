<template>
  <el-container style="height: 1000px; border: 1px solid #eee;position: relative;display: flex;">
    <el-aside width="300px" style="background-color: rgb(238, 241, 246);">
      <el-menu :default-openeds="['1']">
        <el-submenu index="1">
          <template slot="title">화면 메뉴</template>
          <el-menu-item-group>
            <template slot="title">데모</template>
            <el-menu-item index="1-0"><router-link to="/demo/home">Home</router-link></el-menu-item>
          </el-menu-item-group>
        </el-submenu>
      </el-menu>
    </el-aside>
    <el-container>
      <el-header style="width: 850px;text-align: right; font-size: 12px;">
        <div  :style="`height: 40px;`">
          <span style="float: left;font-weight: bold;font-size: 20px;">Chatbot Builder: Service Mesh Demo</span>
          <template v-if="isLogin" style="text-align: right">
            ID: {{username}} <el-button v-on:click="logout" type="danger">로그아웃</el-button>
          </template>
          <template v-else>
            ID: <el-input placeholder="id" v-model="username" size="mini" /> 비밀번호: <el-input placeholder="password" v-model="password" show-password size="mini" /> <el-button v-on:click="login" type="primary">로그인</el-button>
          </template>
        </div>
      </el-header>
      <el-main style="padding-left: 40px; width: 850px;">
        <template>
          <el-table :data="accessLog" stripe style="width: 100%" height="180" empty-text="No Access Log">
            <el-table-column label="로그인 날짜" width="250px">
              <template slot-scope="scope">
                <i class="el-icon-time" /><span style="margin-left: 10px;">{{scope.row.date}}</span>
              </template>
            </el-table-column>
            <el-table-column prop="username" label="사용자 이름" width="180px">
            </el-table-column>
            <el-table-column prop="token" label="JWT 토큰" width="250px">
              <template slot-scope="scope">
                <el-tooltip effect="dark" placement="top"><div slot="content" style="text-align: left;">{{scope.row.token}}</div>
                  <span>{{scope.row.token.substr(0,20)+"..."}}</span>
                </el-tooltip>
              </template>
            </el-table-column>
            <el-table-column label="Operation" width="100px"><el-button size="mini" type="danger" @click="handleDelete(scope.$index)">삭제</el-button></el-table-column>
          </el-table>
        </template>
        <template v-if="isLogin">
          <router-view :systemKey="systemKey"/>
        </template>
        <template v-else>
          <router-view :systemKey="systemKey"/>
        </template>
      </el-main>
    </el-container>
  </el-container>
</template>
<script>
import { login } from "../api/login"
import headerImg from '@/assets/header.png'

export default {
  name: 'Layout',
  components: { },
  props: {
    msg: String
  },
  computed: {
    isLogin: function () {
      return (this.access_token!=="")
    }
  },
  data () {
    return {
      username: '',
      password: '',
      userId: '',
      systemKey: '',
      access_token: '',
      accessLog: []
    }
  },
  methods : {
    convertDatetime (date) {
      const year = date.getFullYear()
      const month = ('0' + (date.getMonth() + 1)).slice(-2)
      const day = ('0' + date.getDate()).slice(-2)
      const hours = ('0' + date.getHours()).slice(-2)
      const minutes = ('0' + date.getMinutes()).slice(-2)
      const seconds = ('0' + date.getSeconds()).slice(-2)
      return year+"-"+month+"-"+day+" "+hours+":"+minutes+":"+seconds
    },
    handleDelete (index) {
      this.accessLog.splice(index, 1)
    },
    login () {
      const datetime = this.convertDatetime(new Date())
      login(this.username, this.password).then(data => {
        this.access_token = data['access_token']
        if(this.access_token) {
          this.accessLog.push({date: datetime,username: this.username,token: this.access_token})
          localStorage.setItem("access_token", this.access_token)
        } else {
          this.access_token = ""
          this.$message({type: 'error', message: "로그인을 실패했습니다.", duration: 500})
        }
      })
    },
    logout () {
      this.userId = ''
      this.systemKey = ''
      this.access_token = ''
      localStorage.setItem("access_token", "")
    },
    userBackground () {
      return headerImg
    }
  }
}
</script>
<style scoped>
.el-header {
  background-color: #83C0D1;
  color: #333;
  line-height: 60px;
}
.el-aside {
  color: #333;
}
.el-input {
  width: 110px;
}
</style>