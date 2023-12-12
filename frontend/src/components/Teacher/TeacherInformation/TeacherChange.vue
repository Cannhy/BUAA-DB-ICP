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
        <el-main>
        <el-form style="padding-left: 5%; padding-right: 5%;margin-top: 50px">
          <el-row>{{userNickName}} 密码修改 </el-row>
          <el-form style="label-width:100px;margin-top: 30px">
          <el-form-item label="原密码">
            <el-col span="6">
              <el-input placeholder="请输入原密码" v-model="userPassWord0" show-password></el-input>
            </el-col>
          </el-form-item>
          <el-form-item label="新密码">
            <el-col span="6">
              <el-input placeholder="请输入新密码" v-model="userPassWord1" show-password></el-input>
            </el-col>
          </el-form-item>
          <el-form-item label="确认新密码">
            <el-col span="6">
              <el-input placeholder="请确认新密码" v-model="userPassWord2" show-password></el-input>
            </el-col>
          </el-form-item>
          <el-form-item>
            <el-col span="6">
              <el-button v-on:click="changePassWord" type="primary" >确认</el-button>
            </el-col>
          </el-form-item>
          </el-form>
        </el-form>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import TeacherMenu from '../TeacherMenu'
export default {
  name: 'TeacherChange',
  components: {TeacherMenu},
  data: function () {
    return {
      userNickName: '',
      userName: '',
      userPassWord0: '',
      userPassWord1: '',
      userPassWord2: ''
    }
  },
  mounted: function () {
    this.userNickName = this.cookie.getCookie('userNickName')
    this.userName = this.cookie.getCookie('userName')
  },
  methods: {
    changePassWord: function () {
      let that = this
      if (that.userPassWord1 === '') {
        that.$message.error('密码不能为空')
      } else {
        that.loading = true
        this.$http.request({
          url: that.$url + 'TeacherPassWordChange/',
          method: 'get',
          params: {
            id: that.userName,
            PassWord0: that.userPassWord0,
            PassWord1: that.userPassWord1,
            PassWord2: that.userPassWord2
          }
        }).then(function (response) {
          console.log(response.data)
          that.loading = false
          that.status = response.data
          if (that.status === 0) {
            that.$message.success('修改成功')
            that.$router.push({
              name: 'TeacherLogin',
              params: {
                userName: that.userName
              }
            })
          } else if (that.status === 1) {
            that.$message.error('原密码错误')
          } else if (that.status === 2) {
            that.$message.error('新密码不一致')
          } else {
            that.$message.error('!')
          }
        }).catch(function (error) {
          console.log(error)
          that.loading = false
        })
      }
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
