<template>
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
      <el-main style="padding-right: 5%; padding-left: 5%; margin-top: 10px;">
          <el-row>
            <el-col :span="23">
              <el-input
                placeholder="查找您的相关课程"
                prefix-icon="el-icon-search" v-model="inputSearch"
                style="margin-bottom: 3%"></el-input>
            </el-col>
            <el-col :span="1">
              <el-button
                type="primary"
                icon="el-icon-search"
                style="display: inline-block; white-space: nowrap; cursor: pointer; background: #fff; border: 1px solid #dcdfe6; color: #2277aa; -webkit-appearance: none; box-sizing: border-box; transition: 0.1s; font-weight: 500; font-size: 17px; border-radius: 4px; float: right"
                @click="searchCourse(inputSearch)"
                circle></el-button>
            </el-col>
          </el-row>
          <el-card v-for="(course, index) in showCourseList" :key="index"
                   v-loading="loading"
                   shadow="always"
                   style="margin-bottom: 2%">
            <el-row>
              <el-col :offset="1" :span="2">
                <el-image :src="courseImg" lazy></el-image>
              </el-col>
              <el-col :offset="2" :span="16">
                <el-row style="margin-bottom: 3%">
                  <el-link type="primary" v-on:click="getCourseInfo(index)">
                    <span style="font-size: 16px"><strong>{{ course.name }}</strong></span>
                  </el-link>
                </el-row>
                <el-row>
                  <el-tag type="warning"  style="font-size: 13px">课程编号<span>&nbsp;{{course.id}}</span></el-tag>
                  <el-tag type="success" style="margin-left: 5px;font-size: 13px">
        授课教师<span>&nbsp;{{ course.teacher }}</span>
</el-tag>
                </el-row>
              </el-col>
            </el-row>
          </el-card>
          <el-dialog title="提示" :visible.sync="courseInfoVisible" width="40%">
            <el-descriptions class="info">
              <el-descriptions-item label="课程名称(ID)">
                &nbsp;&nbsp;
                {{courseInfo.name}}({{courseInfo.id}})
              </el-descriptions-item>
              <el-descriptions-item label="课程介绍">
                &nbsp;&nbsp;
                <span v-html="courseInfo.introduction"></span>
              </el-descriptions-item>
            </el-descriptions>
            <div slot="footer" class="dialog-footer">
              <el-button type="primary" @click="courseInfoVisible = false">确 定</el-button>
            </div>
          </el-dialog>
        </el-main>

    </el-container>
  </el-container>
</template>

/* CSS美化代码 */
<style>
@import "../../../assets/css/back.css";

/* 外部容器样式 */
.course-search {
  margin: 20px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f8f8f8;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

/* 搜索框样式 */
.course-search input[type="text"] {
  width: 200px;
  padding: 5px;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 3px;
  margin: 0 auto;
}

/* 搜索按钮样式 */
.course-search button {
  padding: 5px 10px;
  font-size: 14px;
  background-color: #4caf50;
  color: #fff;
  border: none;
  border-radius: 3px;
  cursor: pointer;
  margin: 10px;
}

/* 课程列表样式 */
.course-search ul {
  list-style-type: none;
  margin: 10px 0;
  padding: 0;
}

/* 课程项样式 */
.course-search li {
  margin-bottom: 10px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* 标题样式 */
.course-search h3 {
  margin: 0 0 5px;
  font-size: 18px;
}

/* 介绍样式 */
.course-search p {
  margin: 0;
  font-size: 14px;
}

/* 课程项之间的分隔线样式 */
.course-search li:not(:last-child) {
  border-bottom: 1px solid #ccc;
}
</style>

<script>
import TeacherMenu from '../TeacherMenu'
import CourseImg from '../../../assets/img/csa.png'
export default {
  name: 'AllCourse',
  components: {TeacherMenu},
  data: function () {
    return {
      courseInfoVisible: false,
      courseImg: CourseImg,
      courseInfo: {
        id: '',
        name: '',
        introduction: ''
      },
      loading: false,
      userNickName: '',
      userName: '',
      courseList: [{
        id: '2',
        name: '课程2',
        teacher: '哇哦i绝对是',
        introduction: 'qwewqe'
      }],
      showCourseList: this.courseList,
      inputSearch: ''
    }
  },
  created () {
    this.showCourseList = this.courseList
  },
  mounted () {
    // 当组件挂载时调用后端接口获取教师开课列表
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.getCourseList()
  },
  methods: {
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('userNickName')
      this.$router.replace('/')
    },
    handleCommand (command) {
      this.goToHelloWorld()
    },
    getCourseInfo: function (index) {
      let that = this
      that.courseInfo = that.showCourseList[index]
      that.courseInfoVisible = true
    },
    getCourseList: function () {
      let that = this
      that.loading = true
      this.$http.request({
        url: that.$url + 'getCourseList/',
        method: 'get'
      }).then(function (response) {
        console.log(response.data)
        that.loading = false
        that.courseList = response.data
        that.showCourseList = response.data
      }).catch(function (error) {
        console.log(error)
        that.loading = false
      })
    },
    searchCourse: function (inputSearch) {
      this.showCourseList = this.searchByIndexOf(inputSearch, this.courseList)
    },
    searchByIndexOf: function (keyWord, list) {
      if (!(list instanceof Array)) {
        return
      } else if (keyWord === '') {
        return list
      }
      const len = list.length
      const arr = []
      for (let i = 0; i < len; i++) {
        // 如果字符串中不包含目标字符会返回-1
        if (list[i].name.indexOf(keyWord) >= 0) {
          arr.push(list[i])
        }
      }
      return arr
    }
  },
  computed: {
    filteredCourses () {
      // 计算属性，用于返回根据搜索框内容过滤后的课程列表
      // 初始状态下返回全部课程
      return this.courses
    }
  }
}
</script>
