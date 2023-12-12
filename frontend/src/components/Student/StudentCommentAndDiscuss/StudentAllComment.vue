<template>
  <div>
    <el-container class="background">
      <el-aside class="aside" width="show?'64px':'400px'">
        <StudentMenu></StudentMenu>
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
        <el-main style="padding-left: 5%; padding-right: 5%;margin-top: 10px">
          <el-row>
            <el-col :span="23">
              <el-row>
                <el-col :span="22">
                  <el-input
                    placeholder="搜索我的课程"
                    prefix-icon="el-icon-search" v-model="inputSearch"
                    style="margin-bottom: 3%"></el-input>
                </el-col>
                <el-col :span="2">
                  <el-button
                    type="primary"
                    icon="el-icon-search"
                    style="display: inline-block; white-space: nowrap; cursor: pointer; background: #fff; border: 1px solid #dcdfe6; color: #2277aa; -webkit-appearance: none; box-sizing: border-box; transition: 0.1s; font-weight: 500; font-size: 17px; border-radius: 4px; float: right;margin-right: 37px"
                    @click="searchCourse(inputSearch)"
                    circle></el-button>
                </el-col>
              </el-row>
              <el-card
                v-for="(course, index) in showCourseList" :key="index"
                style="font-size: small; margin-bottom: 2%;">
                <div slot="header" class="clearfix">
                  <el-col :span="2">
                    <el-image :src="courseImg" lazy></el-image>
                  </el-col>
                  {{ course.name }}
                  <el-button v-on:click="commentCourse(index)" type="text" style="font-size: medium; float: right">
                    进入评价
                  </el-button>
                  <el-rate
                    v-model="course.score"
                    disabled
                    show-score
                    text-color="#ff9900">
                  </el-rate>
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
import StudentMenu from '../StudentMenu'
import StudentImg from '../../../assets/img/student.png'
import CourseImg from '../../../assets/img/buaa_class_img.jpg'

export default {
  name: 'StudentAllComment',
  components: {StudentMenu},
  data: function () {
    return {
      userName: '',
      loading: false,
      userNickName: '',
      commentNum: '',
      courseNum: '',
      courseImg: CourseImg,
      studentImg: StudentImg,
      inputSearch: '',
      courseList: [{
        id: 1,
        name: 'asdawd',
        introduction: 'asdasd',
        score: 3.0
      }],
      showCourseList: [{
        id: '1',
        name: 'course 1',
        introduction: 'asd',
        score: 3.0
      },
      {
        id: '2',
        name: 'course 1',
        introduction: 'asd',
        score: 3.0
      }]
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.getCourseList()
    this.showCourseList = this.courseList
  },
  methods: {
    handleCommand (command) {
      this.goToHelloWorld()
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
    commentCourse: function (index) {
      let that = this
      this.$router.push({
        path: '/StudentCommentAndDiscuss/StudentComment',
        query: {
          courseId: that.showCourseList[index].id
        }
      })
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
