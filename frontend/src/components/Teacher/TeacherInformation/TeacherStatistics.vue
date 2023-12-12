<template>
  <div>
    <el-container class="background">
      <el-aside class="aside" width="show?'64px':'400px'">
        <TeacherMenu></TeacherMenu>
      </el-aside>
      <el-container class="main">
        <el-header class="header" style="background: white">
          <div class="heading_left">
            <i class="el-icon-edit">ICP课程平台</i>
          </div>
          <div class="heading_right">
            <el-avatar style="margin-top: 10px;margin-right: 10px"> {{ userNickName }}</el-avatar>
            <el-dropdown @command="handleCommand"><span class="el-dropdown-link">{{ userNickName }}<i
              class="el-icon-arrow-down el-icon--right"></i></span>
              <el-dropdown-menu slot="dropdown">
                <el-dropdown-item command="goToHelloWorld">退出登录</el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
          </div>
        </el-header>
        <el-main style="padding-left: 5%; padding-right: 5%;margin-top: 50px">
          <template>
  <div class="student-profile">
    <div class="profile-header">
      <h2>{{ userNickName }}</h2>
      <p>{{ userName }}</p>
    </div>
    <div class="profile-stats">
      <div class="statistic">
        <div class="count">{{ courseCount }}</div>
        <div class="label">开课门数</div>
      </div>
      <div class="statistic">
        <div class="count">{{ discussCount }}</div>
        <div class="label">发帖数</div>
      </div>
    </div>
  </div>
</template>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<style scoped>
@import "../../../assets/css/back.css";
</style>

<script>
import TeacherMenu from '../TeacherMenu'

export default {
  name: 'TeacherStatistics',
  components: {TeacherMenu},
  data: function () {
    return {
      userName: '20315354',
      userNickName: '胡傲神的',
      courseCount: 10,
      evalCount: 5,
      discussCount: 7
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.GetTeacherCourseNum()
    this.GetTeacherDisCussNum()
  },
  methods: {
    GetTeacherCourseNum: function () {
      let that = this
      that.loading = true
      this.$http.request({
        url: that.$url + 'GetTeacherCourseNum/',
        method: 'get',
        params: {
          tid: that.userName
        }
      }).then(function (response) {
        console.log(response.data)
        that.courseCount = response.data
        that.loading = false
      }).catch(function (error) {
        console.log(error)
        that.loading = false
      })
    },
    GetTeacherDisCussNum: function () {
      let that = this
      that.loading = true
      this.$http.request({
        url: that.$url + 'GetTeacherDiscussNum/',
        method: 'get',
        params: {
          tid: that.userName
        }
      }).then(function (response) {
        console.log(response.data)
        that.discussCount = response.data
        that.loading = false
      }).catch(function (error) {
        console.log(error)
        that.loading = false
      })
    },
    handleCommand (command) {
      this.goToHelloWorld()
    },
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('userNickName')
      this.$router.replace('/')
    }
  }
}
</script>

<style scoped>
  @import "../../../assets/css/back.css";

</style>

<style scoped>
.student-profile {
  max-width: 600px;
  margin: auto;
  padding: 20px;
  background-color: rgb(255, 255, 255, 0.9);
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.profile-header {
  text-align: center;
  margin-bottom: 20px;
}

.profile-stats {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
}

.statistic {
  text-align: center;
  margin: 10px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 8px;
}

.count {
  font-size: 24px;
  font-weight: bold;
  color: #007bff;
}

.label {
  margin-top: 5px;
  color: #555;
}
</style>
