<template>
  <div>
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
        <el-main>
          <el-row class="buttons">{{courseName}} 评价</el-row>
          <el-row class="buttons">
            <el-button v-on:click="returnStudentAllComment" size="small">返回</el-button>
          </el-row>
          <el-divider></el-divider>
          <div v-for="(comment) in commentList" v-bind:key="comment">
            <el-row class="time">
              {{comment.time}}
            </el-row>
            <el-row class="userName">
              {{comment.userNickName}}({{comment.userName}}) :
            </el-row>
            <el-row class="content" style="color: black">
              {{comment.content}}
            </el-row>
            <el-row class="delete" :span="1" style="float: left">
              <el-link type="danger" v-on:click="deleteComment(comment.id)">删除</el-link>
            </el-row>
            <el-divider></el-divider>
          </div>
      </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<style scoped>
@import "../../../assets/css/back.css";
  .buttons {
    margin-bottom: 10px;
  }
  .input {
    font-size: large;
  }
  .time {
    font-size: small;
    color: rgba(26, 22, 22, 0.37);
  }
  .userName {
    font-size: medium;
    color: #66b1ff;
  }
  .content {
    font-size: medium;
    word-break: break-all;
  }
</style>

<script>
import AdminMenu from '../AdminMenu'
export default {
  name: 'Comment',
  components: {AdminMenu},
  data: function () {
    return {
      userName: '',
      userNickName: '',
      courseId: '',
      courseName: '',
      contentInput: '',
      time: '',
      commentList: [{
        id: 1,
        userName: '12312312',
        userNickName: 'asdwad',
        content: 'asddddddd',
        time: '2020203-100'
      }
      ]
    }
  },
  mounted () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.courseId = this.$route.query.courseId
    this.courseName = this.$route.query.courseName
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
    getCommentList: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'GetCommentList/',
        method: 'get',
        params: {
          cid: that.courseId
        }
      }).then(function (response) {
        console.log(response.data)
        that.commentList = response.data
      }).catch(function (error) {
        console.log(error)
      })
    },
    deleteComment: function (commentId) {
      this.$confirm('此操作将永久删除该评价，是否继续？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消'
      }).then(() => {
        let that = this
        that.getTime()
        this.$http.request({
          url: that.$url + 'DeleteComment/',
          method: 'get',
          params: {
            id: commentId
          }
        }).then(function (response) {
          console.log(response.data)
          if (response.data === 0) {
            that.$message.success('删除成功')
            that.getCommentList()
          } else {
            that.$message.error('未知错误')
          }
        }).catch(function (error) {
          console.log(error)
        })
      })
    },
    returnStudentAllComment: function () {
      let that = this
      that.$router.push({
        name: 'CommentTable'
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
