<template>
  <el-container class="background">
    <el-aside class="aside" width="show?'64px':'400px'">
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
      <el-main style="padding-right: 5%; padding-left: 5%">
          <el-row style="margin-top: 10px">
            <el-col :span="21">
              <el-input
                placeholder="查找课程"
                prefix-icon="el-icon-search" v-model="inputSearch"
                style="margin-bottom: 3%"></el-input>
            </el-col>
            <el-col :span="3">
              <el-button
                type="primary"
                icon="el-icon-search"
                style="float: right; margin-right: 75px"
                @click="searchCourse(inputSearch)"
                circle></el-button>
            </el-col>
          </el-row>
          <el-card v-for="(course, index) in showCourseList" :key="index"
                   v-loading="loading"
                   shadow="always"
                   style="margin-bottom: 2%; margin-right: 5%">
            <el-row>
              <el-col :offset="2" :span="2" style="margin-right: -50px;margin-left: 80px;margin-top: 6px">
                <el-image style="margin-left: -10px" :src="courseImg" lazy></el-image>
              </el-col>
              <el-col :offset="2" :span="14">
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
              <el-col :span="2">
                <el-button v-on:click="cancelCourse(index)" type="danger" size="medium" style="margin-top: 18px; margin-left: 100px">删除</el-button>
              </el-col>
            </el-row>
          </el-card>
          <el-dialog title="提示" :visible.sync="courseInfoVisible" width="40%">
            <el-descriptions class="info" direction="vertical">
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
import AdminMenu from '../AdminMenu'
import CourseImg from '../../../assets/img/csa.png'
export default {
  name: 'CourseTable',
  components: {AdminMenu},
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
        id: '1',
        name: '课程1',
        teacher: '撒谎对撒',
        introduction: ''
      }, {
        id: '2',
        name: '课程2',
        introduction: ''
      }],
      showCourseList: this.courseList,
      inputSearch: ''
    }
  },
  created () {
    this.showCourseList = this.courseList
  },
  mounted () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.getCourseList()
  },
  methods: {
    handleCommand (command) {
      this.goToHelloWorld()
    },
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('userNickName')
      this.$router.replace('/')
    },
    getCourseInfo: function (index) {
      let that = this
      that.courseInfo = that.courseList[index]
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
        that.loading = false
        console.log(error)
      })
    },
    cancelCourse: function (index) {
      this.$confirm('此操作将停开并删除该课程，是否继续？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        console.log(index)
        let that = this
        that.loading = true
        this.$http.request({
          url: that.$url + 'CancelCourse/',
          method: 'get',
          params: {
            userName: that.userName,
            cid: that.showCourseList[index].id
          }
        }).then(function (response) {
          console.log(response.data)
          that.loading = false
          if (response.data === 0) {
            that.$message.success('停课成功')
          } else {
            that.$message.error('未知错误')
          }
          that.getCourseList()
        }).catch(function (error) {
          console.log(error)
          that.loading = false
        })
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
