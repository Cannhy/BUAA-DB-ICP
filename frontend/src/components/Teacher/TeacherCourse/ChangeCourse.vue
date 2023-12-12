<template>
  <div>
    <el-container class="background">
      <el-aside class="aside" width="show?'64px':'250px'">
        <TeacherNav></TeacherNav>
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
        <el-main style="padding-left: 30%; padding-right: 10%">
        <el-page-header @back="returnManageCourse" :content="name" style="margin-bottom: 2%">
        </el-page-header>
        <el-form label-position="top" v-loading="loading">
          <el-form-item label="课程名称">
            <el-col :span="12">
              <el-input v-model="name"></el-input>
            </el-col>
          </el-form-item>
          <el-form-item label="课程介绍">
            <el-col :span="12">
              <quill-editor ref="text" v-model="introduction" style="height: 200px"></quill-editor>
            </el-col>
          </el-form-item>
          <el-form-item style="margin-top: 20%">
            <el-col :span="6">
              <el-button v-on:click="changeCourse" type="primary">确认</el-button>
            </el-col>
          </el-form-item>
        </el-form>
      </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>

import {quillEditor} from 'vue-quill-editor'
import TeacherMenu from '../TeacherMenu'
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'
export default {
  /* eslint-disable */
  name: 'ChangeCourse',
  components: {TeacherMenu, quillEditor},
  data: function () {
    return {
      loading: false,
      userName: '',
      userNickName: '',
      id: '',
      name: '',
      introduction: '',
    }
  },
  mounted () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.id = this.$route.query.id
    this.getCourseInfo()
  },
  methods: {
    handleCommand (command) {
      this.goToHelloWorld()
    },
    getCourseInfo: function () {
      let that = this
      that.loading = true
      this.$http.request({
        url: that.$url + 'GetCourseInfo/',
        method: 'get',
        params: {
          courseId: that.id
        }
      }).then(function (response) {
        console.log(response.data)
        that.loading = false
        that.name = response.data.name
        that.introduction = response.data.introduction
      }).catch(function (error) {
        that.loading = false
        console.log(error)
      })
    },
    returnManageCourse: function () {
      let that = this
      that.$router.push({
        name: 'ManageCourse'
      })
    },
    changeCourse: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'ChangeCourse/',
        method: 'get',
        params: {
          cid: that.id,
          name: that.name,
          introduction: that.introduction,
          userName: that.userName
        }
      }).then(function (response) {
        console.log(response.data)
        that.loading = false
        if (response.data === 0) {
          that.$message.success('修改成功')
          that.$router.push({
            name: 'ManageCourse'
          })
        }
      }).catch(function (error) {
        console.log(error)
        that.loading = false
      })
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
 @import "../../../assets/css/nav.css";
 @import "../../../assets/css/back.css";
</style>
