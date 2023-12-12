<template>
  <div>
    <el-container class="background">
      <el-aside width="250px">
        <AdminMenu></AdminMenu>
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
        <el-main style="padding-left: 10%; padding-right: 10%">
          <h2>ICP课程平台</h2>
          <h1>简介</h1>
          <p style="line-height: 2;">ICP(Integrated Course Platform)，是集选课系统、课程评价、推荐课程、作业统计、学习资料管理、公共讨论区于一体的面向老师和学生的课程平台，旨在方便北航学生对学习任务的统一管理和教师对课程的安排，提高师生教学效率。</p>
          <p>ICP 课程平台可以允许同学们方便的选课，并且会有课程评价模块，选过课的同学们可以对课程进行评价，方便其他同学查看以及教师对教学质量的改善。</p>
          <p>学生所选课程的作业会集中到代办事项模块进行显示。</p>
          <p>ICP 设有公共讨论区，方便同学们咨询某些课程的安排以及课程内容问题的探讨。</p>
          <h1>使用说明</h1>
          在左侧菜单栏中，
          <ul>
            <li>点击课程信息——进行选课、退课</li>
            <li>点击讨论区——进行评价课程、问答等讨论交流</li>
            <li>点击待办事项——查看你的任务</li>
            <li>点击个人中心——进行密码修改</li>
          </ul>
          <h4>感谢您的使用！</h4>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import AdminMenu from './AdminMenu'
import Utils from '../../assets/js/util.js'
export default {
  name: 'AdminHead',
  components: {AdminMenu},
  data: function () {
    return {
      circleUrl: '',
      userName: '',
      userNickName: '',
      show: false
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
  },
  methods: {
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('userNickName')
      this.$router.replace('/')
    },
    toggleCollapse: function () {
      this.show = !this.show
      Utils.$emit('toggleCollapseAdmin', 'call function toggleCollapse in Admin')
    },
    handleCommand (command) {
      this.goToHelloWorld()
    }
  }
}
</script>

<style scoped>
  @import '../../assets/css/back.css';
</style>
