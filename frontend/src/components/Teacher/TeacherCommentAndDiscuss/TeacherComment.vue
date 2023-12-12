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
       <el-main style="padding-left: 5%; padding-right: 5%; ">
          <el-page-header @back="returnStudentAllComment" style="margin-bottom: 2%"></el-page-header>
          <el-card class="course" shadow="always" style="margin-bottom: 0">
            <el-row>
              <el-col :offset="1" :span="3">
                <el-image :src="courseImg" lazy></el-image>
                <el-row>
                  &nbsp;
                </el-row>
                <el-row style="text-align: center; font-size: medium">
                  课程评分
                </el-row>
                <el-rate
                  align="center"
                  v-model="courseAvgDegree"
                  disabled
                  show-score
                  text-color="#ff9900"></el-rate>
              </el-col>
              <el-col :offset="2" :span="17">
                <el-row>
                  <el-col :span="18">
                    <strong>{{courseName}}</strong>
                  </el-col>
                </el-row>
                <el-row>
                  <el-divider>
                  </el-divider>
                </el-row>
                <el-row>
                  <div style="font-size: small">
                    <h3>课程介绍</h3>
                    <span v-html="courseIntroduction"></span>
                  </div>
                </el-row>
              </el-col>
            </el-row>
          </el-card>
          <el-row>
          </el-row>
          <div class="comment">
          <div style="margin-top: 20px" v-for="(comment) in commentList" v-bind:key="comment">
            <el-row>
              <el-col :span="1">
            <el-avatar :src="studentImg" size="medium"></el-avatar></el-col>
      <!-- 用户名和评分 -->
              <el-col :span="14">
      <div class="user-info">
        <div class="user-name-rating">
          <div class="user-name">{{ comment.userNickName }}</div>
          <el-rate style=" margin-left: 8px;" :value="comment.degree" disabled></el-rate>
          <div class="time">{{ comment.time }}</div>
        </div>
      </div>
      <!-- 评论内容 -->
      <div class="content">
        <div class="content-of-comment" v-html="comment.content"></div>
        <!-- 删除按钮，仅显示在评论者为当前用户时 -->
      </div>
                </el-col>
              </el-row>
          </div>
          </div>
      </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<style scoped>
@import "../../../assets/css/back.css";
.course {
    margin: 20px auto;
    background: rgb(255, 255, 255, 0.9);
    box-shadow: 1px 1px 7px #adadad, -1px -1px 7px #ffffff;
    border-radius: 10px;
    padding: 20px;
    width: 95%;
    overflow: auto;
  }
  .comment {
    margin: 20px auto;
    background: rgb(255, 255, 255, 0.9);
    box-shadow: 1px 1px 7px #adadad, -1px -1px 7px #ffffff;
    border-radius: 10px;
    padding: 20px;
    width: 95%;
    overflow: auto;
  }
  .score {
    margin: 20px auto;
    background: rgb(255, 255, 255, 0.9);
    box-shadow: 1px 1px 7px #adadad, -1px -1px 7px #ffffff;
    border-radius: 10px;
    padding: 20px;
    width: 95%;
    overflow: auto;
  }
  .buttons {
    margin-bottom: 10px;
  }
  .input {
    font-size: large;
  }
  .time {
    font-size: small;
    color: rgba(21, 4, 4, 0.52);
  }
  .userName {
    font-size: medium;
    color: #66b1ff;
  }
  .content {
    font-size: medium;
    word-break: break-all;
  }
  .user-info {
  margin-left: 10px;
  display: flex;
  flex-direction: column;
}

.user-name-rating {
  display: flex;
  align-items: center; /* 水平居中对齐 */
}

.user-name {
  font-weight: bold;
  margin-right: 5px;
}

.time {
font-size: small;
    color: rgba(21, 4, 4, 0.52);
  margin-left: 10px;
}

.content {
  margin-top: 15px;
  margin-bottom: 30px;
  margin-left: 10px;
  font-size: medium;
    word-break: break-all;
}
</style>

<script>
import TeacherMenu from '../TeacherMenu'
import CourseImg from '../../../assets/img/buaa_class_img.jpg'
import StudentImg from '../../../assets/img/G.jpg'
export default {
  name: 'TeacherComment',
  components: {TeacherMenu},
  data: function () {
    return {
      loading: true,
      userName: '',
      userNickName: '',
      courseId: '',
      courseName: 'asdwa',
      courseIntroduction: 'asdwad',
      courseAvgDegree: 1.0,
      contentInput: '',
      courseImg: CourseImg,
      studentImg: StudentImg,
      time: '',
      commentList: [{
        id: 1,
        userName: '20323232',
        userNickName: '杨某困',
        degree: 2,
        content: '阿斯顿顶顶顶顶顶',
        time: '200-1022-15：00'
      }, {
        id: 2,
        userName: '20323232',
        userNickName: '杨某困',
        degree: 3,
        content: '阿斯顿顶顶顶顶顶',
        time: '200-1022-15：00'
      }
      ]
    }
  },
  mounted () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.courseId = this.$route.query.courseId
    this.getCourseInfo()
    this.getDegree()
    this.getCommentList()
  },
  methods: {
    getTime: function () {
      let dt = new Date()
      let yyyy = dt.getFullYear()
      let MM = (dt.getMonth() + 1).toString().padStart(2, '0')
      let dd = dt.getDate().toString().padStart(2, '0')
      let h = dt.getHours().toString().padStart(2, '0')
      let m = dt.getMinutes().toString().padStart(2, '0')
      let s = dt.getSeconds().toString().padStart(2, '0')
      this.time = yyyy + '-' + MM + '-' + dd + ' ' + h + ':' + m + ':' + s
    },
    getCourseInfo: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'GetCourseInfo/',
        method: 'get',
        params: {
          courseId: that.courseId
        }
      }).then(function (response) {
        console.log(response.data)
        that.courseName = response.data.name
        that.courseIntroduction = response.data.introduction
      }).catch(function (error) {
        console.log(error)
      })
    },
    getCommentList: function () {
      let that = this
      that.loading = true
      this.$http.request({
        url: that.$url + 'GetCommentList/',
        method: 'get',
        params: {
          cid: that.courseId
        }
      }).then(function (response) {
        console.log(response.data)
        that.loading = false
        that.commentList = response.data
      }).catch(function (error) {
        console.log(error)
        that.loading = false
      })
    },
    getDegree: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'GetDegree/',
        method: 'get',
        params: {
          id: that.courseId
        }
      }).then(function (response) {
        console.log(response.data)
        that.courseAvgDegree = response.data
        if (that.courseAvgDegree !== 5) {
          that.courseAvgDegree = Number(that.courseAvgDegree).toFixed(1)
        }
      })
    },
    returnStudentAllComment: function () {
      let that = this
      that.$router.push({
        name: 'TeacherAllComment'
      })
    },
    handleCommand (command) {
      this.goToHelloWorld()
    },
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('userNickName')
      this.$router.replace('/')
    }
  }
}
</script>
