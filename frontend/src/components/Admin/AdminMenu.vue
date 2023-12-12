<template>
  <div>
    <el-menu default-active="$route.path" class="el-head-menu" router>
      <el-menu-item class="item" index="/AdminHead">
        <i class="el-icon-s-home"></i>
        <span class="item">首页</span>
      </el-menu-item>
      <el-menu-item index="/TeacherTable">
        <i class="el-icon-medal" ></i>
        <span slot="title">教师管理</span>
      </el-menu-item>
      <el-menu-item index="/StudentTable">
        <i class="el-icon-s-management" ></i>
        <span slot="title">学生管理</span>
      </el-menu-item>
      <el-menu-item index="/CourseTable">
        <i class="el-icon-coffee" ></i>
        <span slot="title">课程管理</span>
      </el-menu-item>
      <el-submenu index="5">
        <template slot="title"><i class="el-icon-share"></i><span class="item">留言管理</span></template>
        <el-menu-item class="subitem" index="/CommentAndDiscussTable/CommentTable">课程评价</el-menu-item>
        <el-menu-item class="subitem" index="/CommentAndDiscussTable/DiscussTable">讨论信息</el-menu-item>
<!--        <el-menu-item class="subitem" index="/AdminHead">修改密码</el-menu-item>-->
    </el-submenu>
      <el-submenu index="6">
        <template slot="title"><i class="el-icon-setting"></i><span>个人中心</span></template>
        <el-menu-item index="/AdminChange">修改密码</el-menu-item>
      </el-submenu>
    </el-menu>
  </div>
</template>

<style>
@import "../../assets/css/menu.css";
</style>

<script>
export default {
  name: 'AdminMenu',
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
