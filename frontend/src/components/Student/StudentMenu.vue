<template>
  <div>
    <el-menu default-active="$route.path" class="el-head-menu" router>
      <el-menu-item class="item" index="/StudentHead">
        <i class="el-icon-s-home"></i>
        <span class="item">首页</span>
      </el-menu-item>
      <el-submenu index="1">
        <template slot="title"><i class="el-icon-location"></i><span>课程信息</span></template>
          <el-menu-item index="/StudentCourse/SelectCourse">学生选课</el-menu-item>
          <el-menu-item index="/StudentCommentAndDiscuss/StudentAllComment">评价课程</el-menu-item>
          <el-menu-item index="/StudentCourse/SelectedCourse">我的课程</el-menu-item>
      </el-submenu>
      <el-menu-item index="/StudentCommentAndDiscuss/StudentAllDiscuss">
        <i class="el-icon-menu" ></i>
        <span slot="title">讨论区</span>
      </el-menu-item>
      <el-menu-item index="/StudentSchedule">
        <i class="el-icon-document"></i>
        <span slot="title">我的作业</span>
      </el-menu-item>
      <el-submenu index="4">
        <template slot="title"><i class="el-icon-setting"></i><span>个人中心</span></template>
          <el-menu-item index="/StudentInformation/StudentStatistics">数据统计</el-menu-item>
          <el-menu-item index="/StudentInformation/StudentChange">修改密码</el-menu-item>
      </el-submenu>
    </el-menu>
  </div>
</template>

<style>
@import "../../assets/css/menu.css";
</style>

<script>
import Utils from '../../assets/js/util.js'
export default {
  name: 'StudentMenu',
  data () {
    return {
      userName: '',
      userNickName: '',
      isCollapsed: this.$root.isCollapsed
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    var that = this
    Utils.$on('toggleCollapse', function (message) {
      console.log(message)
      that.toggleCollapse()
    })
  },
  methods: {
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('userNickName')
      this.$router.replace('/')
    },
    toggleCollapse: function () {
      this.isCollapsed = !this.isCollapsed
      this.$root.isCollapsed = this.isCollapsed
    }
  }
}
</script>
