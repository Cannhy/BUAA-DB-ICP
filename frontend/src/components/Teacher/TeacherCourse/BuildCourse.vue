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
      <template>
  <div class="add-course-container">
    <el-card class="add-course-card">
      <h2 class="add-course-title">开设课程</h2>
      <el-form :model="courseForm" label-width="80px">
        <el-form-item label="课程名称" required>
          <el-input v-model="courseForm.name" placeholder="请输入课程名称" />
        </el-form-item>
        <el-form-item label="课程介绍" required>
          <div class="quill-editor">
            <quill-editor v-model="courseForm.introduction" :options="quillOptions" />
          </div>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm">提交</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>
    </el-container>
  </el-container>
</template>

<style scoped>
@import "../../../assets/css/back.css";
.container {
  width: 60%;
  /* 占据浏览器宽度的60% */
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f8f8f8;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  /* 水平居中 */
  border: 1px solid #ccc;
  /* 边框样式 */
  padding: 20px;
  /* 内边距 */
}

h2 {
  color: #333;
}

form {
  margin-bottom: 20px;
  display: flex;
  justify-content: center;
  flex-direction: column;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  width: 80%;
}

input[type="text"],
textarea {
  width: 80%;
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 3px;
  margin: 0 10px;
}

button {
  padding: 8px 16px;
  background-color: #4caf50;
  color: #fff;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}

p {
  margin-top: 5px;
}
</style>

<script>
import TeacherMenu from '../TeacherMenu'
import {quillEditor} from 'vue-quill-editor'
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'
export default {
  name: 'BuildCourse',
  components: {TeacherMenu, quillEditor},
  data () {
    return {
      courseForm: {
        name: '',
        introduction: ''
      },
      loading: false,
      userName: '',
      userNickName: 'asd',
      courseName: '',
      course: {
        name: '',
        introduction: ''
      },
      response: null
    }
  },
  mounted () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
  },
  methods: {
    submitForm () {
      // 处理表单提交逻辑，例如发送请求保存课程信息
      let that = this
      console.log('课程名称:', this.courseForm.name)
      console.log('课程介绍:', this.courseForm.introduction)
      // 提交成功后可以进行页面跳转或其他操作
      const cname = that.courseForm.name
      const cintro = that.courseForm.introduction
      that.loading = true
      this.$http.request({
        url: that.$url + 'BuildCourse/',
        method: 'get',
        params: {
          id: that.userName,
          name: cname,
          introduction: cintro
        }
      }).then(function (response) {
        console.log(response.data)
        that.loading = false
        that.status = response.data
        if (that.status === 0) {
          that.$message.success('创建成功')
          that.materialIdString = ''
          that.course = {
            name: ''
          }
        } else if (that.status === 1) {
          that.$message.error('课程名称不可为空')
        }
      }).catch(function (error) {
        console.log(error)
        that.loading = false
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
<style scoped>
.add-course-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.add-course-card {
  width: 1200px;
  height: 600px;
}

.add-course-title {
  text-align: center;
  margin-bottom: 20px;
  font-size: 20px;
  color: #150404;
  font-weight: 600;
}
.quill-editor {
  width: 100%;
}
</style>
