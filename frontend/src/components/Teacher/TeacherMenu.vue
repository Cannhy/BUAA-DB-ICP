<template>
  <div>
    <el-menu default-active="$route.path" class="el-head-menu" router>
      <el-menu-item class="item" index="/TeacherHead">
        <i class="el-icon-s-home"></i>
        <span class="item">首页</span>
      </el-menu-item>
      <el-submenu index="1">
        <template slot="title"><i class="el-icon-location"></i><span>课程信息</span></template>
        <el-menu-item index="/TeacherCourse/AllCourse">查看课程</el-menu-item>
        <el-menu-item index="/TeacherCourse/ManageCourse">管理课程</el-menu-item>
      </el-submenu>
      <el-menu-item class="item2" index="/TeacherHomework">
        <i class="el-icon-s-claim"></i>
        <span class="item2">课程作业</span>
      </el-menu-item>
      <el-submenu index="3">
        <template slot="title"><i class="el-icon-share"></i><span class="item">留言板</span></template>
        <el-menu-item class="subitem" index="/TeacherCommentAndDiscuss/TeacherAllComment">课程评价</el-menu-item>
        <el-menu-item class="subitem" index="/TeacherCommentAndDiscuss/TeacherAllDiscuss">自由讨论</el-menu-item>
      </el-submenu>
      <el-submenu index="4">
        <template slot="title"><i class="el-icon-setting"></i><span>个人中心</span></template>
        <el-menu-item index="/TeacherInformation/TeacherStatistics">数据统计</el-menu-item>
        <el-menu-item index="/TeacherInformation/TeacherChange">修改密码</el-menu-item>
      </el-submenu>
    </el-menu>
  </div>
</template>

<style>
@import "../../assets/css/menu.css";
</style>

<script>
export default {
  name: 'StudentMenu',
  data () {
    return {
      userName: '',
      userNickName: '',
      isCollapsed: this.$root.isCollapsed
    }
  },
  methods: {
    handleOpenAndClose: function () {
      this.isCollapsed = !this.isCollapsed
      this.$root.isCollapsed = this.isCollapsed
    }
  }
}
</script>
