<template>
  <div>
    <el-container class="background">
      <el-aside class="aside" width="show?'64px':'400px'">
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
        <el-main style="padding-right: 5%; padding-left: 5%;margin-top: 30px;">
          <div class="todo-app">
            <el-table :border="true" class="custom-table" :row-class-name="tableRowClassName" :data="homeworks" style="width: 100%;margin-bottom: 20px;" :header-row-class-name="headerRowClassName" :header-cell-style="{
      background:'#f0f9eb'}"
 >
      <el-table-column :align="'center'" label="作业ID" prop="id"></el-table-column>
              <el-table-column :align="'center'" label="课程" prop="courseName"></el-table-column>
      <el-table-column :align="'center'" label="作业结束时间" prop="endTime"></el-table-column>
      <el-table-column :align="'center'" label="作业内容" prop="content"></el-table-column>
      <el-table-column :align="'center'" label="是否完成">
        <template slot-scope="scope">
          <el-switch v-model="scope.row.state" active-color="#13ce66" inactive-color="#ff4949" @change="updateHomeworkStatus(scope.row)">
          </el-switch>
        </template>
      </el-table-column>
      <el-table-column label="">
        <template slot-scope="scope">
          <el-button v-if="scope.row.modified === 1" @click="showModifyDialog(scope.row)" type="warning" size="medium" round>修改</el-button>
          <el-button @click="confirmDelete(scope.row)" type="danger" size="medium" round>删除</el-button>
        </template>
      </el-table-column>
    </el-table>
            <el-button round type="success" style="box-shadow: 0 12px 16px rgba(0, 0, 0, 0.1);font-size: 16px"  @click="showAddHomeworkDialog">添加作业</el-button>
            <el-dialog
  title="修改作业"
  :visible.sync="modifyDialogVisible"
  width="30%"
  @close="clearModifyHomeworkData"
>
  <el-form :model="modifyHomeworkData" ref="modifyHomeworkForm">
    <!-- 截止时间 -->
    <el-form-item label="截止时间" prop="endTime">
      <el-date-picker v-model="modifyHomeworkData.endTime" type="datetime" placeholder="选择截止时间"></el-date-picker>
    </el-form-item>

    <!-- 作业内容 -->
    <el-form-item label="作业内容" prop="content">
      <el-input v-model="modifyHomeworkData.content" placeholder="请输入作业内容"></el-input>
    </el-form-item>
  </el-form>

  <div slot="footer" class="dialog-footer">
    <el-button @click="modifyHomework" type="primary">确认修改</el-button>
    <el-button @click="modifyDialogVisible = false">取消</el-button>
  </div>
</el-dialog>
            <el-dialog
      title="添加作业"
      :visible.sync="addHomeworkDialogVisible"
      width="30%"
      @close="clearAddHomeworkForm"
    >
      <el-form :model="addHomeworkForm" ref="addHomeworkForm" :rules="addHomeworkFormRules">
        <el-form-item label="选择课程" prop="course">
          <el-select v-model="addHomeworkForm.course" placeholder="请选择课程">
            <el-option v-for="course in courses" :key="course.id" :label="course.name" :value="course.id" />
          </el-select>
        </el-form-item>
        <el-form-item label="作业内容" prop="content">
          <el-input v-model="addHomeworkForm.content" placeholder="请输入作业内容"></el-input>
        </el-form-item>
        <el-form-item label="截止时间" prop="endTime">
          <el-date-picker v-model="addHomeworkForm.endTime" type="datetime" placeholder="选择截止时间"></el-date-picker>
        </el-form-item>
      </el-form>

      <div slot="footer" class="dialog-footer">
        <el-button @click="addHomework" type="primary">添加</el-button>
        <el-button @click="addHomeworkDialogVisible = false">取消</el-button>
      </div>
    </el-dialog>
          </div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<style>
  .el-table .warning-row {
    background: oldlace;
  }
  /*.el-table tbody tr.table-row-checked,.el-table tbody tr:hover {*/
  /*  position:relative;*/
  /*  background:#fff;*/
  /*}*/
  /*.el-table tbody tr.table-row-checked::after,.el-table tbody tr:hover::after {*/
  /*  position:absolute;*/
  /*  content:" ";*/
  /*  width:100%;*/
  /*  height:100%;*/
  /*  left:0;*/
  /*  background:transparent;*/
  /*  box-shadow:0 3px 10px 1px rgba(0,0,0,0.1);*/
  /*}*/
  .el-table .success-row {
    background: #f0f9eb;
  }
</style>

<style scoped>
.el-table {
  box-shadow: 1px 1px 7px #adadad, -1px -1px 7px #ffffff;
}

/* 如果你希望鼠标悬停时出现更强的阴影，你可以添加如下样式： */
.el-table:hover {
  box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
}
</style>

<script>
import StudentMenu from './StudentMenu'
export default {
  name: 'StudentSchedule',
  components: {StudentMenu},
  data () {
    return {
      userName: '',
      userNickName: '',
      courses: [{id: 1, name: '123'},
        {id: 2, name: '1232'}],
      homeworks: [
        {id: 1, courseName: 'test', endTime: '2023-12-31', isTeacher: 1, content: '作业内容1', state: false, modified: 1},
        {id: 2, courseName: 'test', endTime: '2023-12-31', isTeacher: 1, content: '作业内容2', state: true, modified: 0}
      ],
      addHomeworkDialogVisible: false,
      modifyDialogVisible: false,
      addHomeworkForm: {
        courseId: '',
        course: null,
        content: '',
        endTime: null
      },
      modifyHomeworkData: {
        id: null,
        endTime: null,
        content: ''
      },
      addHomeworkFormRules: {
        course: [{ required: true, message: '请选择课程', trigger: 'change' }],
        content: [{ required: true, message: '请输入作业内容', trigger: 'blur' }],
        endTime: [{ required: true, message: '请选择截止时间', trigger: 'change' }]
      }
    }
  },
  mounted () {
    this.userName = this.cookie.getCookie('userName')
    this.userNickName = this.cookie.getCookie('userNickName')
    this.fetchTodoList()
    this.getStudentCourseList()
  },
  methods: {
    tableRowClassName ({row, rowIndex}) {
      if (rowIndex === 1) {
        return 'warning-row'
      } else if (rowIndex === 3) {
        return 'success-row'
      }
      return ''
    },
    headerRowClassName () {
      // 返回自定义表头的样式类名
      return 'custom-header-row'
    },
    rowStyle ({ row, rowIndex }) {
      // 自定义每一行的样式
      return {
        background: rowIndex % 2 === 0 ? '#a4e4fd' : 'rgba(164,228,253,0.93)', // 行的背景颜色交替
        color: '#333'
      }
    },
    goToHelloWorld: function () {
      this.cookie.clearCookie('userName')
      this.cookie.clearCookie('userNickName')
      this.$router.replace('/')
    },
    handleCommand (command) {
      this.goToHelloWorld()
    },
    fetchTodoList: function () {
      let that = this
      that.loading = true
      this.$http.request({
        url: that.$url + 'StudentHomeworkList/',
        method: 'get',
        params: {
          sid: that.userName
        }
      }).then(function (response) {
        console.log(response.data)
        that.loading = false
        that.homeworks = response.data
      }).catch(function (error) {
        console.log(error)
        that.loading = false
      })
    },
    // 更新待办事项的完成状态
    updateHomeworkStatus (homework) {
      let that = this
      const index = that.homeworks.indexOf(homework)
      console.log(index)
      that.homeworks[index].state = !homework.state
      homework.state = !homework.state
      console.log(homework.state)
      this.$http.request({
        url: that.$url + 'StudentChangeHomeworkState/',
        method: 'get',
        params: {
          sid: that.userName,
          hid: homework.id,
          state: homework.state ? 1 : 0
        }
      }).then(function (response) {
        console.log(response.data)
      })
    },
    showModifyDialog (row) {
    // 将当前行的内容传递给修改的数据对象
      this.modifyHomeworkData = {
        id: row.id,
        endTime: row.endTime,
        content: row.content
      }
      this.modifyDialogVisible = true
    },
    clearModifyHomeworkData () {
    // 清空修改的数据对象
      this.modifyHomeworkData = {
        id: null,
        courseName: '',
        endTime: null,
        content: ''
      }
      this.modifyDialogVisible = false
    },
    modifyHomework () {
      this.$refs.modifyHomeworkForm.validate((valid) => {
        if (valid) {
          let that = this
          this.$http.request({
            url: that.$url + 'StudentChangeHomework/',
            method: 'get',
            params: {
              hid: that.modifyHomeworkData.id,
              end_time: that.modifyHomeworkData.endTime,
              content: that.modifyHomeworkData.content
            }
          }).then(function (response) {
            console.log(response.data)
            that.fetchTodoList()
          })
          that.addHomeworkDialogVisible = false
          this.clearModifyHomeworkData()
        } else {
          // 验证失败，不执行任何操作
        }
      })
    },
    confirmDelete (homework) {
      this.$confirm(`确定要删除作业ID为 ${homework.id} 的作业吗？`, '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      })
        .then(() => {
          // 在这里处理确认删除的逻辑
          this.deleteHomework(homework.id)
        })
        .catch(() => {
          // 用户点击取消的处理逻辑
        })
    },
    deleteHomework (homeworkId) {
      // 在这里实现删除作业的逻辑
      // 可以从数据源中删除对应的作业对象，然后刷新表格数据
      const index = this.homeworks.findIndex((homework) => homework.id === homeworkId)
      if (index !== -1) {
        this.homeworks.splice(index, 1)
      }
      let that = this
      this.$http.request({
        url: that.$url + 'StudentDeleteHomework/',
        method: 'get',
        params: {
          hid: homeworkId
        }
      }).then(function (response) {
        console.log(response.data)
      })
    },
    showAddHomeworkDialog () {
      this.addHomeworkDialogVisible = true
    },
    clearAddHomeworkForm () {
      this.$refs.addHomeworkForm.resetFields()
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
        that.courses = response.data
      }).catch(function (error) {
        console.log(error)
        that.loading = false
      })
    },
    addHomework () {
      this.$refs.addHomeworkForm.validate((valid) => {
        if (valid) {
          let that = this
          this.$http.request({
            url: that.$url + 'StudentAddHomework/',
            method: 'get',
            params: {
              sid: that.userName,
              cid: that.addHomeworkForm.course,
              end_time: that.addHomeworkForm.endTime,
              content: that.addHomeworkForm.content
            }
          }).then(function (response) {
            console.log(response.data)
            that.fetchTodoList()
          })
          that.addHomeworkDialogVisible = false
          that.clearAddHomeworkForm()
        } else {
          // 验证失败，不执行任何操作
        }
      })
    }
  }
}
</script>

<style scoped>
@import "../../assets/css/menu.css";
@import "../../assets/css/back.css";

.todo-app {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}
.todo-input {
  width: 200px;
  margin-bottom: 10px;
}

.todo-select {
  width: 200px;
  margin-bottom: 10px;
}

/* 调整日期选择器样式 */
.todo-datepicker {
  width: 200px;
  margin-bottom: 10px;
}
.todo-button {
  margin-bottom: 10px;
}
.todo-table {
  margin-top: 10px;
  width: 400px;
}
.todo-table th {
  background-color: #f5f7fa;
  color: #909399;
  font-weight: bold;
  text-align: left;
}
.todo-table tr:nth-child(odd) {
  background-color: #f9fafc;
}
.custom-table {
  /* 添加自定义样式 */
}

.custom-table::before {
  content: "";
}
</style>
