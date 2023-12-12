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
          <el-row style="margin-top: 1px">
            <el-col :span="23">
              <el-input
                placeholder="查找学生"
                prefix-icon="el-icon-search" v-model="inputSearch"
                style="margin-bottom: 2%"></el-input>
            </el-col>
            <el-col :span="1">
              <el-button
                type="primary"
                icon="el-icon-search"
                style="float: right"
                @click="searchCourse(inputSearch)"
                circle></el-button>
            </el-col>
          </el-row>
          <el-card v-for="(student, index) in showStudentList" :key="index" style="margin-bottom: 2%">
            <el-row>
              <el-col :offset="2" :span="2">
                <el-empty :image-size="40" style="margin: 0 !important; padding: 0 !important;"></el-empty>
              </el-col>
              <el-col :offset="2" :span="16">
                <el-row style="margin-bottom: 3%">
                  <span style="font-size: 20px"><strong>{{ student.name }}</strong></span>
                </el-row>
                <el-row>
                  <el-tag type="success" style="font-size: 14px">学号</el-tag><span style="color: gray; font-size: 17px">&nbsp;&nbsp;{{student.id}}</span>
                </el-row>
              </el-col>
            </el-row>
          </el-card>
        </el-main>

    </el-container>
  </el-container>
</template>

<script>
import AdminMenu from '../AdminMenu'
export default {
  name: 'StudentTable',
  components: {AdminMenu},
  data () {
    return {
      loading: true,
      userName: '',
      userNickName: '',
      showStudentList: this.studentList,
      studentList: [
        {
          id: 1235113,
          name: 'asfasd'
        },
        {
          id: 54375375,
          name: 'dfghdfgdf'
        },
        {
          id: 543753575,
          name: 'sdfgsdf'
        }
      ],
      inputSearch: ''
    }
  },
  created () {
    this.showStudentList = this.studentList
  },
  mounted () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.getStudentList()
  },
  methods: {
    getStudentList: function () {
      let that = this
      that.loading = true
      this.$http.request({
        url: that.$url + 'GetStudentList/',
        method: 'get'
      }).then(function (response) {
        console.log(response.data)
        that.loading = false
        that.studentList = response.data
        that.showStudentList = response.data
      }).catch(function (error) {
        console.log(error)
        that.loading = false
      })
    },
    searchCourse: function (inputSearch) {
      this.showStudentList = this.searchByIndexOf(inputSearch, this.studentList)
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
    },
    handleCommand (command) {
      this.goToHelloWorld()
    },
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('userNickName')
      this.$router.replace('/')
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
