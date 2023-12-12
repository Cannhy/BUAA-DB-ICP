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
        <el-main style="padding-right: 5%; padding-left: 5%;margin-top: 10px">
          <el-row>
            <el-col :span="23">
              <el-row>
                <el-col :span="22">
                  <el-input
                    placeholder="查找您的相关课程"
                    prefix-icon="el-icon-search" v-model="inputSearch"
                    style="margin-bottom: 3%"></el-input>
                </el-col>
                <el-col :span="2">
                  <el-button
                    type="primary"
                    icon="el-icon-search"
                    style="float: right; margin-right: 31px;"
                    @click="searchCourse(inputSearch)"
                    circle></el-button>
                </el-col>
              </el-row>
              <el-card
                v-for="(course, index) in showCourseList" :key="index"
                style="font-size: small; margin-bottom: 2%;">
                <div slot="header" class="clearfix" style="font-size: 16px;">
                  <el-col :span="2">
                    <el-image :src="courseImg" lazy></el-image>
                  </el-col>
                  {{ course.name }}
                  <el-button v-on:click="commentCourse(index)" type="text" style="font-size: 15px; float: right">
                    查看评价
                  </el-button>
                  <el-rate
                    v-model="course.score"
                    disabled
                    show-score
                    text-color="#ff9900"
                    style="margin-top: 10px;">
                  </el-rate>
                </div>
                <div
                  style="font-size: 14px; margin-left: 18px;text-overflow: ellipsis ;max-height: 50px; overflow: hidden; white-space: nowrap;">
                  <span v-html="course.introduction"></span>
                </div>
              </el-card>
            </el-col>
          </el-row>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import TeacherMenu from '../TeacherMenu'
import CourseImg from '../../../assets/img/buaa_class_img.jpg'
import TeacherImg from '../../../assets/img/teacher.png'
export default {
  name: 'TeacherAllComment',
  components: {TeacherMenu},
  data: function () {
    return {
      loading: true,
      userName: '',
      userNickName: '',
      courseNum: '1',
      inputSearch: '',
      showIt: false,
      teacherImg: TeacherImg,
      courseImg: CourseImg,
      courseList: [{
        id: '1',
        name: '前端测试课程1',
        introduction: '12312312',
        score: '2'
      }, {
        id: '2',
        name: '前端测试课程2',
        introduction: '12312312',
        score: '5'
      }],
      showCourseList: this.courseList
    }
  },
  created () {
    this.showCourseList = this.courseList
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.getCourseList()
  },
  methods: {
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
    commentCourse: function (index) {
      let that = this
      this.$router.push({
        path: '/TeacherCommentAndDiscuss/TeacherComment',
        query: {
          courseId: that.showCourseList[index].id
        }
      })
    },
    handleCommand (command) {
      this.goToHelloWorld()
    },
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('userNickName')
      this.$router.replace('/')
    },
    changeShowIt: function () {
      this.showIt = !this.showIt
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
  }
}
</script>

<style scoped>
  @import "../../../assets/css/back.css";
  .el-row-button {
    width: 100% !important;
  }
  .el-row-button :hover {
    background-color: initial;
  }
  .el-row-button-head :hover {
    background-color: hsla(0, 0%, 74%, 0.2);
  }
</style>
