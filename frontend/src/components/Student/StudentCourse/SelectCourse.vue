<template>
  <div>
    <el-container class="background">
      <el-aside class="aside" width="show?'64px':'300px'">
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
        <el-main style="padding-right: 5%; padding-left: 5%;margin-top: 10px">
          <el-row style="padding-bottom: 0%">
            <el-col :span="23">
              <el-input
                placeholder="搜索课程"
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
                   shadow="hover"
                   style="margin-bottom: 2%">
            <el-row>
              <el-col :offset="1" :span="2">
                <el-image :src="courseImg"></el-image>
              </el-col>
              <el-col :offset="2" :span="14">
                <el-row style="margin-bottom: 20px">
                  <el-link type="primary" v-on:click="getCourseInfo(index)">
                    <span style="font-size: 20px"><strong>{{ course.name }}</strong></span>
                  </el-link>
                </el-row>
                <el-row>
                  <el-tag type="warning"  style="font-size: 13px">课程编号<span>&nbsp;{{course.id}}</span></el-tag>
                  <el-tag type="success" style="margin-left: 5px;font-size: 13px">
        授课教师<span>&nbsp;{{ course.teacher }}</span>
</el-tag>
                </el-row>
              </el-col>
              <el-col :span="2">
                <el-button-group style="margin-top: 15px; margin-left: 120px">
                  <el-button round v-on:click="selectCourse(index)" type="primary">选课</el-button>
                </el-button-group>
              </el-col>
            </el-row>
          </el-card>
          <el-dialog title="提示" :visible.sync="courseInfoVisible" width="40%">
            <el-descriptions class="info">
              <el-descriptions-item label="课程介绍">&nbsp;&nbsp;
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
  </div>
</template>

<style scoped>
@import "../../../assets/css/back.css";
.info {
  margin-bottom: 20px;
  word-break: break-all;
}
</style>

<script>
import StudentMenu from '../StudentMenu'
import CourseImg from '../../../assets/img/csa.png'
export default {
  /* eslint-disable */
  name: 'SelectCourse',
  components: {StudentMenu},
  data: function () {
    return {
      courseInfoVisible: false,
      courseInfo: {
        id: '',
        name: '',
        introduction: ''
      },
      courseImg: CourseImg,
      loading: false,
      userName: '',
      userNickName: '',
      courseList: [{
        name:'course 1',
        id: '1',
        teacher: '酱紫面林',
        introduction: '',
        avgDegree: 2.0
      },
        {
        name:'course 2',
        id: '2',
          teacher: '草尖或',
        introduction: 'asd',
        avgDegree: 3.0
      }
      ],
      showCourseList: this.courseList,
      inputSearch: ''
    }
  },
  created () {
     this.showCourseList = this.courseList;
  },
  mounted: function () {
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
      that.courseInfo = that.courseList[index]
      that.courseInfoVisible = true
    },
    getCourseList: function () {
      let that = this
      that.loading = true
      console.log("asdawdsa")
      this.$http.request({
        url: that.$url + 'getAllCourses/',
        method: 'get',
        params: {
            userName: that.userName
          }
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
    selectCourse (index) {
      console.log(index)
      let that = this
      this.$http.request({
        url: that.$url + 'SelectCourse/',
        method: 'get',
        params: {
          sid: that.userName,
          cid: that.showCourseList[index].id
        }
      }).then(function (response) {
        console.log(response.data)
        let status = response.data;
        if (status === 0) {
          that.$message.success('选课成功')
          that.getCourseList()
        } else {
          that.$message.error('!')
        }
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
  }
}
</script>
