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
        <el-main style="padding-left: 5%; padding-right: 5%; margin-top: 10px">
          <el-row>
            <el-col :span="23">
              <el-input
                placeholder="查找您的相关课程"
                prefix-icon="el-icon-search" v-model="inputSearch"
                style="margin-bottom: 1%"></el-input>
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
          <div class="base">
          <div v-for="(course, index) in showMyCourseList" :key="index" class="card">
      <div class="header2">{{course.name}}</div>
      <div class="body">
        <div class="item_board">
          <div class="item">
            <span class="item_entry">课程 ID ：</span><span class="item_content">{{course.id}}</span>
          </div>
          <div class="item">
            <span class="item_entry">授课教师：</span><span class="item_content">{{course.teacher}}</span>
          </div>
          <div class="item">
            <span class="item_entry">课程介绍：</span>
            <el-button type="warning" style="margin-left: -10px" v-on:click="getCourseInfo(index)" plain round size="small">查看介绍</el-button>
          </div>
          <el-button type="danger" round class="bt" v-on:click="dropCourse(index)">退选课程</el-button>
        </div>
      </div>
    </div>
            </div>
          <el-dialog title="提示" :visible.sync="courseInfoVisible" width="40%">
            <el-descriptions class="info" direction="vertical">
              <el-descriptions-item label="课程名称(ID)">
                &nbsp;&nbsp;
                {{courseInfo.name}}({{courseInfo.id}})
              </el-descriptions-item>
              <el-descriptions-item label="课程介绍">&nbsp;&nbsp;
                <span v-html="courseInfo.introduction "></span>
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
body {
  margin: 0;
}

.background {
  height: 100vh;
  background-image: url("../../../assets/img/background.png");
}

.main {
  height: 100vh;
}

.heading_left {
  font-size: 20px;
  display: inline-flex;
  float: left;
  margin-top: 20px;
}

.heading_right {
  font-size: 20px;
  display: inline-flex;
  float: right;
}

.header {
  line-height: 60px;
}

</style>

<script>
import StudentMenu from '../StudentMenu'
import CourseImg from '../../../assets/img/csa.png'
export default {
  /* eslint-disable */
  name: 'StudentCourse',
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
      loading: true,
      userName: '',
      userNickName: '',
      inputSearch: '',
      myCourseList: [{
        id: '1',
        name: '课程1',
        teacher: 'asdasd',
        time: 'as',
        location: 'lc',
        introduction: '',
        avgDegree: 3.0
      }],
      showMyCourseList: [{
        id: '1',
        name: '课程1',
        teacher: 'asdasd',
        time: 'as',
        location: 'lc',
        introduction: '和',
        avgDegree: 3.0
      }]
    }
  },
  mounted: function () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.loading = false
    this.getStudentCourseList()
  },
  methods: {
    getCourseInfo: function (index) {
      let that = this
      that.courseInfo = that.showMyCourseList[index]
      that.courseInfoVisible = true
    },
    getStudentCourseList: function () {
      let that = this
      that.loading = true
      this.$http.request({
        url: that.$url + 'GetStudentCourseList/',
        method: 'get',
        params: {
          id: that.userName
        }
      }).then(function (response) {
        console.log(response.data)
        that.loading = false
        that.myCourseList = response.data
        that.showMyCourseList = response.data
      }).catch(function (error) {
        console.log(error)
        that.loading = false
      })
    },
    dropCourse: function (index) {
      this.$confirm('此操作将退选该课程，是否继续？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        console.log(index)
        let that = this
        this.$http.request({
          url: that.$url + 'DropCourse/',
          method: 'get',
          params: {
            sid: that.userName,
            cid: that.showMyCourseList[index].id
          }
        }).then(function (response) {
          console.log(response.data)
          if (response.data === 0) {
            that.$message.success('退课成功')
          } else {
            that.$message.error('未知错误')
          }
          that.getStudentCourseList()
        }).catch(function (error) {
          console.log(error)
        })
      })
    },
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('userNickName')
      this.$router.replace('/')
    },
    handleCommand (command) {
      this.goToHelloWorld()
    },
    searchCourse: function (inputSearch) {
      this.showMyCourseList = this.searchByIndexOf(inputSearch, this.myCourseList)
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
@font-face {
    font-family: 'myFont1';
    src: url("../../../assets/font/font1.ttf");
  }
  .base {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
  }
.item {
    margin: 15px;
  }
  .item_board {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    width: 395px;
    margin-left: 2px;
    margin-top: 2px;
  }
  .item_entry {
    color: #1a1a1a;
    font-size: 15px;
    font-family: serif;
    font-weight: bold;
    margin-right: 10px;
  }
  .item_content {
    color: #303133;
    font-family: serif;
  }
  .card {
    background-color: white;
    margin: 20px;
    width: 400px;
    height: 280px;
    border-radius: 10px; /*设置边角圆形*/
    box-shadow: 0 0 0 rgb(0 0 0 / 10%), 0 4px 5px rgb(38 38 38 / 12%);
  }
  .header2 {
    text-align: center;
    margin-top: 0.5px;
    margin-right: 1px;
    margin-left: 1px;
    height: 60px;
    line-height: 60px;
    border-radius: 10px; /*设置边角圆形*/
    font-weight: bolder;
    font-size: 20px;
    font-family: serif;
    color: white;
    background-color: rgb(255, 152, 0);
  }
  .card:hover {
    box-shadow: 0 0 0 rgb(0 0 0 / 10%), 0 8px 10px rgb(38 38 38 / 12%);
  }
  .bt {
    margin-left: 260px;
  }
  .el-button--warning.is-plain:hover {
    color: white;
    font-weight: bolder;
    background: #ff9800;
    border-color: #f5dab1;
  }
</style>
