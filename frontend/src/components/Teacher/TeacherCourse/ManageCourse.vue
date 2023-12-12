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
      <el-main style="padding-left: 5%; padding-right: 5%; margin-top: 10px">
          <el-row>
            <el-col :span="20">
              <el-input
                placeholder="查找您的相关课程"
                prefix-icon="el-icon-search" v-model="inputSearch"
                style="margin-bottom: 3%"></el-input>
            </el-col>
            <el-col :span="1">
              <el-button
                type="primary"
                icon="el-icon-search"
                style="display: inline-block; white-space: nowrap; cursor: pointer; background: #fff; border: 1px solid #dcdfe6; color: #2277aa; -webkit-appearance: none; box-sizing: border-box; transition: 0.1s; font-weight: 500; font-size: 17px; border-radius: 4px; margin-left: 16px"
                @click="searchCourse(inputSearch)"
                circle></el-button>
            </el-col>
            <el-col :span="3">
               <el-button style="font-size: 18px; float: right; " type="success" plain @click="showAddCourseDialog">开设课程</el-button>
            </el-col>
          </el-row>
          <el-card v-for="(course, index) in showMyCourseList" :key="index"
                   v-loading="loading"
                   shadow="always"
                   style="margin-bottom: 2%;">
            <el-row>
              <el-col :offset="2" :span="2">
                <el-image :src="courseImg" lazy></el-image>
              </el-col>
              <el-col :offset="2" :span="16">
                <el-row style="margin-bottom: 3%">
                  <el-link type="primary" v-on:click="getCourseInfo(index)">
                    <span style="font-size: 16px"><strong>{{ course.name }}</strong></span>
                  </el-link>
                </el-row>
                <el-row>
                  <el-tag type="success"  style="font-size: 13px">课程编号<span>&nbsp;{{course.id}}</span></el-tag>
                </el-row>
              </el-col>
              <el-col :span="2">
    <el-button-group style="margin-bottom: 6%">
      <el-button type="primary" style="display: inline-block; white-space: nowrap; cursor: pointer; background: #fff; border: 1px solid #dcdfe6; color: #2277aa; -webkit-appearance: none; box-sizing: border-box; transition: 0.1s; font-weight: 500; font-size: 17px; border-radius: 4px;margin-left: -24px" icon="el-icon-edit" @click="showEditDialog(index)">修改</el-button>
    </el-button-group>
    <el-button-group>
      <el-button type="danger" style="display: inline-block; white-space: nowrap; cursor: pointer; background: #fff; border: 1px solid #dcdfe6; color: #2277aa; -webkit-appearance: none; box-sizing: border-box; transition: 0.1s; font-weight: 500; font-size: 17px; border-radius: 4px;margin-left: -24px" icon="el-icon-delete" @click="cancelCourse(index)">停课</el-button>
    </el-button-group>
  </el-col>

  <!-- 编辑课程的弹出窗体 -->
  <el-dialog :visible.sync="editDialogVisible" title="编辑课程" width="50%">
    <el-form :model="editFormData" ref="editForm" label-width="80px">
      <el-form-item label="课程名称">
        <el-input v-model="editFormData.name" />
      </el-form-item>
      <el-form-item label="课程介绍">
        <el-input v-model="editFormData.introduction" type="textarea" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="saveEdit">保存</el-button>
        <el-button @click="cancelEdit">取消</el-button>
      </el-form-item>
    </el-form>
  </el-dialog>
            </el-row>
          </el-card>
          <el-dialog title="课程信息" :visible.sync="courseInfoVisible" width="40%">
            <el-descriptions class="info" direction="horizontal">
              <el-descriptions-item label="课程名称(ID)">
                <div style="white-space: nowrap;">
                  {{ courseInfo.name }}({{ courseInfo.id }})
                </div>
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
        <el-dialog :visible.sync="addCourseDialogVisible" title="开设新课程" width="50%">
    <el-form :model="addCourseFormData" ref="addCourseForm" label-width="80px">
      <el-form-item label="课程名称" required>
          <el-input v-model="addCourseFormData.name" placeholder="请输入课程名称" />
        </el-form-item>
        <el-form-item label="课程介绍" required>
          <div class="quill-editor">
            <quill-editor v-model="addCourseFormData.introduction"/>
          </div>
        </el-form-item>
      <el-form-item>
        <el-button style="float: right" @click="cancelAddCourse">取消</el-button>
        <el-button style="margin-right: 10px; float: right" type="primary" @click="saveNewCourse">确定</el-button>
      </el-form-item>
    </el-form>
  </el-dialog>
        </el-main>
    </el-container>
  </el-container>
</template>

/* CSS美化代码 */
<style>
/* 搜索框样式 */
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

.course-search textarea {
  width: 200px;
}
</style>

<script>
import TeacherMenu from '../TeacherMenu'
import CourseImg from '../../../assets/img/csa.png'
import {quillEditor} from 'vue-quill-editor'
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'
export default {
  name: 'ManageCourse',
  components: {TeacherMenu, quillEditor},
  data: function () {
    return {
      editDialogVisible: false,
      editFormData: {
        name: '',
        introduction: '',
        id: ''
        // 其他需要编辑的字段
      },
      courseInfoVisible: false,
      courseInfo: {
        id: '',
        name: '',
        introduction: ''
      },
      courseImg: CourseImg,
      loading: false,
      userNickName: '',
      userName: '',
      myCourseList: [{
        id: 1,
        name: '综合个测评',
        introduction: '毫阿三大苏打伟大啊我顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶阿斯顿顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶克'
      }],
      showMyCourseList: this.myCourseList,
      inputSearch: '',
      addCourseDialogVisible: false,
      // 存储添加课程表单数据
      addCourseFormData: {
        name: '',
        introduction: ''
      }
    }
  },
  created () {
    this.showMyCourseList = this.myCourseList
  },
  mounted () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.getTeacherCourseList()
  },
  methods: {
    showAddCourseDialog () {
      this.addCourseDialogVisible = true
    },
    // 取消添加课程
    cancelAddCourse () {
      this.addCourseDialogVisible = false
      // 可选：重置表单数据
      this.$refs.addCourseForm.resetFields()
    },
    // 保存新课程
    saveNewCourse () {
      let that = this
      // 提交成功后可以进行页面跳转或其他操作
      const cname = that.addCourseFormData.name
      const cintro = that.addCourseFormData.introduction
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
          that.addCourseFormData = {
            name: '',
            introduction: ''
          }
          that.getTeacherCourseList()
          that.cancelAddCourse()
        } else if (that.status === 1) {
          that.$message.error('课程名称不可为空')
        }
      }).catch(function (error) {
        console.log(error)
        that.loading = false
      })
      // 可选：关闭弹出窗体
    },
    showEditDialog (index) {
      // 根据索引获取需要编辑的课程信息，假设课程列表为 this.courseList
      const courseToEdit = this.myCourseList[index]
      // 将课程信息填充到编辑表单中
      this.editFormData = {
        name: courseToEdit.name,
        introduction: courseToEdit.introduction,
        id: courseToEdit.id
        // 其他需要编辑的字段
      }
      // 显示编辑弹出窗体
      this.editDialogVisible = true
    },
    saveEdit () {
      let that = this
      this.$http.request({
        url: that.$url + 'ChangeCourse/',
        method: 'get',
        params: {
          cid: that.editFormData.id,
          name: that.editFormData.name,
          introduction: that.editFormData.introduction,
          userName: that.userName
        }
      }).then(function (response) {
        console.log(response.data)
        if (response.data === 1) {
          that.$message.error('课程名字不可为空')
        }
        that.getTeacherCourseList()
        that.loading = false
      }).catch(function (error) {
        console.log(error)
        that.loading = false
      })
      // 隐藏编辑弹出窗体
      that.editDialogVisible = false
    },
    cancelEdit () {
      // 取消编辑，清空编辑表单数据
      this.editFormData = {
        name: '',
        introduction: ''
        // 其他需要编辑的字段
      }
      // 隐藏编辑弹出窗体
      this.editDialogVisible = false
    },
    handleCommand (command) {
      this.goToHelloWorld()
    },
    getCourseInfo: function (index) {
      let that = this
      that.courseInfo = that.showMyCourseList[index]
      that.courseInfoVisible = true
    },
    getTeacherCourseList: function () {
      let that = this
      that.loading = true
      this.$http.request({
        url: that.$url + 'GetTeacherCourseList/',
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
            cid: that.showMyCourseList[index].id
          }
        }).then(function (response) {
          console.log(response.data)
          that.loading = false
          if (response.data === 0) {
            that.$message.success('停课成功')
          } else {
            that.$message.error('未知错误')
          }
          that.getTeacherCourseList()
        }).catch(function (error) {
          console.log(error)
          that.loading = false
        })
      })
    },
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('userNickName')
      this.$router.replace('/')
    },
    searchCourse: function (inputSearch) {
      let that = this
      that.showMyCourseList = this.searchByIndexOf(inputSearch, that.myCourseList)
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
