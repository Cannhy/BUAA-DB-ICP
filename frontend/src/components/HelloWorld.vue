<template>
  <transition name="head-login-register">
    <div class="welcome">
      <div class="navigator">
        <div class="navigator-left">
          <i class="el-icon-edit">ICP课程平台</i>
        </div>
        <div class="navigator-right">
          <div class="time-container">
            <div id="time">{{ currentTime }}</div>
          </div>
        </div>
      </div>
      <div class="introduction">
        <el-carousel height="600px">
          <el-carousel-item v-for="(item, index) in headImg" :key="index">
            <img :src="item.src" style="width: 120%; height: 100%;" alt="">
            <div class="cover">
              <span style="font-size: 50px; opacity:1;color: #2C5E19;">{{ item.title }}</span><br>
              <span style="font-size: 25px; opacity:1;color: #2C5E19;">{{ item.subTitle }}</span><br>
              <span><el-button round type="success" class="buttons"
                               @click="goToStudentLogin">我是学生</el-button></span>
              <span>&nbsp;&nbsp;&nbsp;&nbsp;</span>
              <span><el-button round type="success" class="buttons"
                               @click="goToTeacherLogin">我是老师</el-button></span>
              <span>&nbsp;&nbsp;&nbsp;&nbsp;</span>
              <span><el-button round type="success" class="buttons"
                               @click="goToAdminLogin">管理员登录</el-button></span>
            </div>
          </el-carousel-item>
        </el-carousel>
      </div>
    </div>
  </transition>
</template>

<script>
import background from '../assets/img/background.jpg'
import background2 from '../assets/img/background2.jpg'

export default {
  data: function () {
    return {
      headImg: [
        {
          'title': 'ICP课程平台',
          'subTitle': 'Integrated Course Platform',
          'src': background2
        },
        {
          'title': 'ICP课程平台',
          'subTitle': 'Integrated Course Platform',
          'src': background
        }
      ],
      fullscreenLoading: false,
      currentTime: ''
    }
  },
  mounted () {
    setInterval(this.updateTime, 1000)
  },
  methods: {
    updateTime () {
      var now = new Date()
      var timeString = now.toLocaleTimeString()
      this.currentTime = timeString
    },
    goToStudentLogin () {
      this.$router.push({
        name: 'StudentLogin'
      })
    },
    goToTeacherLogin () {
      this.$router.push({
        name: 'TeacherLogin'
      })
    },
    goToAdminLogin () {
      this.$router.push({
        name: 'AdminLogin'
      })
    }
  }
}
</script>

<style scoped>
@import "../assets/css/HelloWorld/block1.css";
@import "../assets/css/HelloWorld/block2.css";
@import "../assets/css/HelloWorld/copyright.css";
@import "../assets/css/HelloWorld/introduction.css";
@import "../assets/css/HelloWorld/navigator.css";
@import "../assets/css/Transition/head-login-register.css";

.welcome {
  margin-left: 0px;
  margin-right: 0px;
  background-image: url('../assets/img/background.png');
  background-size: cover;
}

</style>
