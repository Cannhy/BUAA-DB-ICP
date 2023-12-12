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
      <el-main style="padding-left: 5%; padding-right: 5%">
          <el-row>
            <el-col :span="23">
              <el-input
                placeholder="查找教师"
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
          <el-card v-for="(teacher, index) in showTeacherList" :key="index" style="margin-bottom: 2%">
            <el-row>
              <el-col :offset="2" :span="2">
                <el-empty :image-size="40" style="margin: 0 !important; padding: 0 !important;"></el-empty>
              </el-col>
              <el-col :offset="2" :span="16">
                <el-row style="margin-bottom: 3%;">
                  <span style="font-size: 20px"><strong>{{ teacher.name }}</strong></span>
                </el-row>
                <el-row>
                  <el-tag type="warning" style="font-size: 14px">工号</el-tag><span style="color: gray;font-size: 17px">&nbsp;&nbsp;{{teacher.id}}</span>
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
  name: 'TeacherTable',
  components: {AdminMenu},
  data () {
    return {
      loading: true,
      userName: '',
      userNickName: '',
      teacherList: [
        {
          id: '123123',
          name: 'sadsad'
        },
        {
          id: '12312312',
          name: 'asdasd'
        },
        {
          id: '567567',
          name: 'asdaw'
        }
      ],
      showTeacherList: this.teacherList,
      inputSearch: ''
    }
  },
  created () {
    this.showTeacherList = this.teacherList
  },
  mounted () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.getTeacherList()
  },
  methods: {
    getTeacherList: function () {
      let that = this
      that.loading = true
      this.$http.request({
        url: that.$url + 'GetTeacherList/',
        method: 'get'
      }).then(function (response) {
        console.log(response.data)
        that.loading = false
        that.teacherList = response.data
        that.showTeacherList = response.data
      }).catch(function (error) {
        console.log(error)
        that.loading = false
      })
    },
    searchCourse: function (inputSearch) {
      this.showTeacherList = this.searchByIndexOf(inputSearch, this.teacherList)
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
