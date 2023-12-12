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
        <el-main style="padding-left: 10%; padding-right: 10%">
          <el-page-header @back="returnStudentAllDiscuss" :content="postTheme.title" style="margin-bottom: 2%">
          </el-page-header>
          <el-row class="buttons">
          </el-row>
          <el-divider>
            <span style="font-weight: bold;">楼主</span>
          </el-divider>
          <el-card shadow="hover" style="margin-bottom: 2%;  background: rgb(255, 255, 255, 0.9);
    box-shadow: 1px 1px 7px #adadad, -1px -1px 7px #ffffff;
    border-radius: 10px;">
            <el-row>
              <el-col :span="1" style="margin-right: 12px">
                <el-image v-if="postTheme.isTeacher === 1" :src="teacherImg" lazy></el-image>
                <el-image v-else-if="postTheme.isTeacher === 2" :src="adminImg" lazy></el-image>
                <el-image v-else :src="studentImg" lazy></el-image>
              </el-col>
              <el-col :offset="0" :span="2">
                <el-row class="time" style="color: rgba(21,4,4,0.52); white-space: nowrap;">
                  {{postTheme.time}}
                </el-row>
                <el-row class="userName" style="font-size: 16px; white-space: nowrap;">
                  <el-col>
                  {{ postTheme.userNickName }} ({{ postTheme.userName }})
                  </el-col>
                </el-row>
                <el-row v-if="postTheme.isTeacher === 1" class="userRole">
                  <el-col>
                    (教师)
                  </el-col>
                </el-row>
                <el-row v-else-if="postTheme.isTeacher === 2" class="userRole">
                  <el-col>
                    (管理员)
                    </el-col>
                </el-row>
              </el-col>
              <el-col :offset="2" :span="16">
                <el-row class="content" v-html="postTheme.content">
                </el-row>
                <el-row class="delete" :span="1" style="float: right">
                  <div v-if="postTheme.userName === userName">
                    <el-link type="danger" v-on:click="deletePostTheme">删除</el-link>
                  </div>
                </el-row>
              </el-col>
              <el-col :offset="1" :span="1">
                <el-button v-on:click="dialogFormVisible = true" type="primary" size="small" style="font-size: 14px; margin-top: 10px; margin-left: -10px">跟贴</el-button>
              </el-col>
            </el-row>
          </el-card>

          <el-dialog :visible.sync="dialogFormVisible">
            <el-input class="input" v-model="input.content" type="textarea" :rows="4" placeholder="与主题相关的讨论">

            </el-input>
            <div slot="footer" class="dialog-footer">
              <el-button @click="dialogFormVisible = false">取 消</el-button>
              <el-button type="primary" @click="buildPost">确 定</el-button>
            </div>
          </el-dialog>
           <el-divider>
            <span style="font-weight: bold;">跟帖</span>
          </el-divider>
          <div class="posts">
          <div style="margin-top: 20px; margin-bottom: 25px" v-for="(post, index) in postList" v-bind:key="index">
            <el-row>
              <el-col :span="1" style="margin-right: 12px">
                <el-image v-if="post.isTeacher === 1" :src="teacherImg" lazy></el-image>
                <el-image v-else-if="post.isTeacher === 2" :src="adminImg" lazy></el-image>
                <el-image v-else :src="studentImg" lazy></el-image>
              </el-col>
              <el-col :span="3">
                <el-row class="time" style="margin-bottom: 4px;white-space: nowrap;">
                  {{post.time}}
                </el-row>
                <el-row class="userName">
                  <div v-if="post.isTeacher === 1">
                    {{post.userNickName}}({{post.userName}}) (教师)
                  </div>
                  <div v-else-if="post.isTeacher === 2">
                    {{post.userNickName}}({{post.userName}}) (管理员)
                  </div>
                  <div v-else>
                    {{post.userNickName}}({{post.userName}})
                  </div>
                </el-row>
              </el-col>
              <el-col class="content" :offset="1" :span="16" style="margin-top: 10px;" v-html="post.content">
              </el-col>
              <el-col class="delete" :span="1" style="float: right">
                <div v-if="post.userName === userName">
                  <el-link type="danger" v-on:click="deletePost(post.id)">删除</el-link>
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
.posts {
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
    font-size: small;
    color: #66b1ff;
  }
  .content {
    font-size: medium;
    word-break: break-all;
  }
  .userRole {
    font-size: small;
    color: #66b1ff;
  }
</style>

<script>
import StudentMenu from '../StudentMenu'
import StudentImg from '../../../assets/img/G.jpg'
import TeacherImg from '../../../assets/img/t.png'
import AdminImg from '../../../assets/img/admin.jpg'
export default {
  name: 'StudentDiscuss',
  components: {StudentMenu},
  data: function () {
    return {
      loading: true,
      userName: '',
      userNickName: '',
      dialogFormVisible: false,
      studentImg: StudentImg,
      teacherImg: TeacherImg,
      adminImg: AdminImg,
      postThemeId: 0,
      postTheme: {
        id: 1,
        userName: 'sadwad',
        userNickName: 'asdwadad',
        title: 'asdwad',
        content: 'asdsad',
        time: 'asdasd',
        isTeacher: 1
      },
      input: {
        content: ''
      },
      postList: [{
        id: 1,
        userName: '20388782',
        userNickName: '阿斯顿',
        content: '水水水水水水水水水水水水水水水sssssssssa阿三顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶阿三顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶水水',
        time: '2001-2021-10.2',
        isTeacher: 1
      }, {
        id: 1,
        userName: '20388782',
        userNickName: '阿斯顿',
        content: '水水水水水水水水水水水水水水水水水',
        time: '2001-2021-10.2',
        isTeacher: 2
      }],
      time: ''
    }
  },
  mounted () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.postTheme = this.$route.query.newPostTheme
    this.postThemeId = this.$route.query.postThemeId
    this.getPostTheme()
    this.getPostList()
    console.log('Checking...')
    console.log(this.postTheme)
  },
  methods: {
    getPostTheme: function () {
      let that = this
      this.$http.request({
        url: that.$url + 'GetMain/',
        method: 'get',
        params: {
          mainId: that.postThemeId
        }
      }).then(function (response) {
        console.log(response.data)
        that.postTheme = response.data
      }).catch(function (error) {
        console.log(error)
      })
    },
    getTime: function () {
      let that = this
      let dt = new Date()
      let yyyy = dt.getFullYear()
      let MM = (dt.getMonth() + 1).toString().padStart(2, '0')
      let dd = dt.getDate().toString().padStart(2, '0')
      let h = dt.getHours().toString().padStart(2, '0')
      let m = dt.getMinutes().toString().padStart(2, '0')
      let s = dt.getSeconds().toString().padStart(2, '0')
      that.time = yyyy + '-' + MM + '-' + dd + ' ' + h + ':' + m + ':' + s
    },
    deletePostTheme: function () {
      this.$confirm('此操作将永久删除该主题贴及其跟贴，是否继续？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        let that = this
        that.getTime()
        this.$http.request({
          url: that.$url + 'DeleteMain/',
          method: 'get',
          params: {
            mainId: that.postTheme.id
          }
        }).then(function (response) {
          console.log(response.data)
          if (response.data === 0) {
            that.$message.success('删除成功')
            that.returnStudentAllDiscuss()
          } else {
            that.$message.error('未知错误')
          }
        }).catch(function (error) {
          console.log(error)
        })
      })
    },
    getPostList: function () {
      let that = this
      that.loading = true
      this.$http.request({
        url: that.$url + 'GetSecondList/',
        method: 'get',
        params: {
          mainId: that.postThemeId
        }
      }).then(function (response) {
        console.log(response.data)
        that.loading = false
        that.postList = response.data
      }).catch(function (error) {
        console.log(error)
        that.loading = false
      })
    },
    buildPost: function () {
      this.dialogFormVisible = false
      let that = this
      that.getTime()
      this.$http.request({
        url: that.$url + 'BuildSecond/',
        method: 'get',
        params: {
          mid: that.postTheme.id,
          uid: that.userName,
          content: that.input.content,
          time: that.time,
          type: 0
        }
      }).then(function (response) {
        console.log(response.data)
        if (response.data === 0) {
          that.$message.success('跟贴成功')
          that.getPostList()
          that.input.content = ''
        } else {
          that.$message.error('未知错误')
        }
      }).catch(function (error) {
        console.log(error)
      })
    },
    deletePost: function (postId) {
      this.$confirm('此操作将永久删除该跟贴，是否继续？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        let that = this
        that.getTime()
        this.$http.request({
          url: that.$url + 'DeleteSecond/',
          method: 'get',
          params: {
            secondId: postId
          }
        }).then(function (response) {
          console.log(response.data)
          if (response.data === 0) {
            that.$message.success('删除成功')
            that.getPostList()
          } else {
            that.$message.error('未知错误')
          }
        }).catch(function (error) {
          console.log(error)
        })
      })
    },
    returnStudentAllDiscuss: function () {
      let that = this
      that.$router.push({
        name: 'StudentAllDiscuss'
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
