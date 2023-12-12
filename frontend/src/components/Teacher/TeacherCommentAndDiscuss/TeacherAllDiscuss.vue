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
        <el-main style="padding-left: 5%; padding-right: 5%;margin-top: 10px">
          <el-row>
            <el-col :span="24">
              <el-row>
                <el-col :span="21">
                  <el-input
                    placeholder="查找相关帖子"
                    prefix-icon="el-icon-search" v-model="inputSearch"
                    style="margin-bottom: 3%"></el-input>
                </el-col>
                <el-col :span="3">
                  <el-button
                    type="primary"
                    icon="el-icon-search"
                    style="float: left; margin-right: 10px;margin-left: 20px"
                    @click="searchDiscuss(inputSearch)"
                    circle>
                  </el-button>
                  <el-button
                    type="primary"
                    icon="el-icon-plus"
                    @click="buildThemeVisible = true"
                    circle></el-button>
                  <el-dialog title="新建帖子" :visible.sync = "buildThemeVisible" width="70%">
                    <el-row style="margin-bottom: 10px">
                      <el-col>
                        <el-input v-model="input.title" placeholder="请输入标题"></el-input>
                      </el-col>
                    </el-row>
                    <el-row style="margin-bottom: 10px">
                      <el-col>
                        <quill-editor ref="text" v-model="input.content" style="height: 300px"></quill-editor>
                      </el-col>
                    </el-row>
                    <div slot="footer" class="dialog-footer" style="margin-top: 5%">
                      <el-button @click="buildThemeVisible = false">取消</el-button>
                      <el-button type="primary" @click="buildPostTheme">确定</el-button>
                    </div>
                  </el-dialog>
                </el-col>
              </el-row>
              <el-card v-for="(postTheme, index) in showPostThemeList" :key="index"
                       style="margin-bottom: 2%">
                <div class="clearfix" style="font-size: 18px">
                  <span>{{postTheme.title}}</span>
                  <el-button style="float: right; padding: 3px 0;font-size: 17px" type="text"
                             v-on:click="enterPostTheme(index)">进入帖子</el-button>
                </div>
                <div class="textitem" style="margin-top: 2%; margin-bottom: 2%">
                  <el-tag style="font-size: 15px; height: 30px;display: inline-flex; align-items: center; justify-content: center;">
                  <span v-if="postTheme.isTeacher === 0">学生</span>
                  <span v-else-if="postTheme.isTeacher === 1">教师</span>
                  <span v-else-if="postTheme.isTeacher === 2">管理员</span>
                  </el-tag>
                </div>
                <div>
                  <span style="color: gray; font-size: 14px">发表于-{{postTheme.time}}</span>
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
import {quillEditor} from 'vue-quill-editor'
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'
import TeacherImg from '../../../assets/img/teacher.png'
export default {
  name: 'TeacherAllDiscuss',
  components: {TeacherMenu, quillEditor},
  data: function () {
    return {
      loading: true,
      userName: '',
      userNickName: '',
      inputSearch: '',
      input: {
        title: '',
        content: ''
      },
      teacherImg: TeacherImg,
      postThemeList: [{
        id: '1',
        userName: 'admin',
        userNickName: '学生1',
        title: '前端测试贴标题',
        content: '前端测试贴内容',
        time: 'xxxx',
        isTeacher: 0
      }, {
        id: '2',
        userName: '学号1',
        userNickName: '学生1',
        title: '前端测试贴标题',
        content: '前端测试贴内容',
        time: 'xxxx',
        isTeacher: 0
      }],
      showPostThemeList: [
        {
          id: '1',
          userName: 'admin',
          userNickName: '学生1',
          title: '前端测试贴标题',
          content: '前端测试贴内容',
          time: 'xxxx',
          isTeacher: 1
        },
        {
          id: '2',
          userName: '学号1',
          userNickName: '学生1',
          title: '前端测试贴标题',
          content: '前端测试贴内容',
          time: 'xxxx',
          isTeacher: 0
        }
      ],
      buildThemeVisible: false,
      time: ''
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.getPostThemeList()
  },
  methods: {
    getPostThemeList: function () {
      let that = this
      that.loading = true
      this.$http.request({
        url: that.$url + 'GetMainList/',
        method: 'get'
      }).then(function (response) {
        console.log(response.data)
        that.loading = false
        that.postThemeList = response.data
        that.showPostThemeList = response.data
      }).catch(function (error) {
        console.log(error)
        that.loading = false
      })
    },
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
    buildPostTheme: function () {
      // this.buildThemeVisible = false
      let that = this
      that.getTime()
      this.$http.request({
        url: that.$url + 'BuildMain/',
        method: 'get',
        params: {
          uid: that.userName,
          title: that.input.title,
          content: that.input.content,
          time: that.time,
          type: 1
        }
      }).then(function (response) {
        console.log(response.data)
        if (response.data === 0) {
          that.$message.success('创建成功')
          that.buildThemeVisible = false
          that.getPostThemeList()
          that.input = {
            title: '',
            content: ''
          }
        } else {
          that.$message.error('未知错误')
        }
      }).catch(function (error) {
        console.log(error)
      })
    },
    enterPostTheme: function (index) {
      let that = this
      this.$router.push({
        name: 'TeacherDiscuss',
        query: {
          postThemeId: that.showPostThemeList[index].id,
          newPostTheme: {
            id: that.showPostThemeList[index].id,
            userName: that.showPostThemeList[index].userName,
            userNickName: that.showPostThemeList[index].userNickName,
            title: that.showPostThemeList[index].title,
            content: that.showPostThemeList[index].content,
            time: that.showPostThemeList[index].time,
            isTeacher: that.showPostThemeList[index].isTeacher
          }
        }
      })
    },
    headerRowClassName () {
      // 返回自定义表头的样式类名
      return 'custom-header-row'
    },
    handleCommand (command) {
      this.goToHelloWorld()
    },
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('userNickName')
      this.$router.replace('/')
    },
    searchDiscuss: function (inputSearch) {
      this.showPostThemeList = this.searchByIndexOf(inputSearch, this.postThemeList)
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
        if (list[i].title.indexOf(keyWord) >= 0) {
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
</style>
