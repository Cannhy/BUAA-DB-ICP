import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '../components/HelloWorld'
import StudentLogin from '../components/Student/StudentLogin'
import StudentRegister from '../components/Student/StudentRegister'
import StudentHead from '../components/Student/StudentHead'
import TeacherLogin from '../components/Teacher/TeacherLogin'
import TeacherHead from '../components/Teacher/TeacherHead'
import TeacherRegister from '../components/Teacher/TeacherRegister'
import StudentCourse from '../components/Student/StudentCourse/StudentCourse'
import SelectCourse from '../components/Student/StudentCourse/SelectCourse'
import SelectedCourse from '../components/Student/StudentCourse/SelectedCourse'
import TeacherCourse from '../components/Teacher/TeacherCourse/TeacherCourse'
import TeacherHomework from '../components/Teacher/TeacherHomework'
import ManageCourse from '../components/Teacher/TeacherCourse/ManageCourse'
import ChangeCourse from '../components/Teacher/TeacherCourse/ChangeCourse'
import BuildCourse from '../components/Teacher/TeacherCourse/BuildCourse'
import AllCourse from '../components/Teacher/TeacherCourse/AllCourse'
import StudentChange from '../components/Student/StudentInformation/StudentChange'
import StudentStatistics from '../components/Student/StudentInformation/StudentStatistics'
import StudentInformation from '../components/Student/StudentInformation/StudentInformation'
import TeacherChange from '../components/Teacher/TeacherInformation/TeacherChange'
import TeacherInformation from '../components/Teacher/TeacherInformation/TeacherInformation'
import TeacherStatistics from '../components/Teacher/TeacherInformation/TeacherStatistics'
import StudentCommentAndDiscuss from '../components/Student/StudentCommentAndDiscuss/StudentCommentAndDiscuss'
import StudentAllComment from '../components/Student/StudentCommentAndDiscuss/StudentAllComment'
import StudentComment from '../components/Student/StudentCommentAndDiscuss/StudentComment'
import StudentAllDiscuss from '../components/Student/StudentCommentAndDiscuss/StudentAllDiscuss'
import StudentDiscuss from '../components/Student/StudentCommentAndDiscuss/StudentDiscuss'
import AdminLogin from '../components/Admin/AdminLogin'
import AdminHead from '../components/Admin/AdminHead'
import AdminChange from '../components/Admin/AdminChange/AdminChange'
import StudentTable from '../components/Admin/StudentTable/StudentTable'
import CourseTable from '../components/Admin/CourseTable/CourseTable'
import TeacherTable from '../components/Admin/TeacherTable/TeacherTable'
import TeacherCommentAndDiscuss from '../components/Teacher/TeacherCommentAndDiscuss/TeacherCommentAndDiscuss'
import TeacherAllComment from '../components/Teacher/TeacherCommentAndDiscuss/TeacherAllComment'
import TeacherComment from '../components/Teacher/TeacherCommentAndDiscuss/TeacherComment'
import TeacherAllDiscuss from '../components/Teacher/TeacherCommentAndDiscuss/TeacherAllDiscuss'
import TeacherDiscuss from '../components/Teacher/TeacherCommentAndDiscuss/TeacherDiscuss'
import StudentSchedule from '../components/Student/StudentSchedule'
import Discuss from '../components/Admin/CommentAndDiscussTable/Discuss'
import Comment from '../components/Admin/CommentAndDiscussTable/Comment'
import DiscussTable from '../components/Admin/CommentAndDiscussTable/DiscussTable'
import CommentTable from '../components/Admin/CommentAndDiscussTable/CommentTable'
import CommentAndDiscussTable from '../components/Admin/CommentAndDiscussTable/CommentAndDiscussTable'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/StudentLogin',
      name: 'StudentLogin',
      component: StudentLogin
    },
    {
      path: '/StudentRegister',
      name: 'StudentRegister',
      component: StudentRegister
    },
    {
      path: '/StudentHead',
      name: 'StudentHead',
      component: StudentHead
    },
    {
      path: '/TeacherLogin',
      name: 'TeacherLogin',
      component: TeacherLogin
    },
    {
      path: '/TeacherHead',
      name: 'TeacherHead',
      component: TeacherHead
    },
    {
      path: '/TeacherRegister',
      name: 'TeacherRegister',
      component: TeacherRegister
    },
    {
      path: '/StudentCourse',
      name: 'StudentCourse',
      component: StudentCourse,
      children: [
        {
          path: 'SelectCourse',
          name: 'SelectCourse',
          component: SelectCourse
        },
        {
          path: 'SelectedCourse',
          name: 'SelectedCourse',
          component: SelectedCourse
        }
      ]
    },
    {
      path: '/TeacherCourse',
      name: 'TeacherCourse',
      component: TeacherCourse,
      children: [
        {
          path: 'BuildCourse',
          name: 'BuildCourse',
          component: BuildCourse
        },
        {
          path: 'ManageCourse',
          name: 'ManageCourse',
          component: ManageCourse
        },
        {
          path: 'AllCourse',
          name: 'AllCourse',
          component: AllCourse
        },
        {
          path: 'ChangeCourse',
          name: 'ChangeCourse',
          component: ChangeCourse
        }
      ]
    },
    {
      path: '/StudentInformation',
      name: 'StudentInformation',
      component: StudentInformation,
      children: [
        {
          path: 'StudentChange',
          component: StudentChange
        },
        {
          path: 'StudentStatistics',
          component: StudentStatistics
        }
      ]
    },
    {
      path: '/TeacherInformation',
      name: 'TeacherInformation',
      component: TeacherInformation,
      children: [
        {
          path: 'TeacherChange',
          component: TeacherChange
        },
        {
          path: 'TeacherStatistics',
          component: TeacherStatistics
        }
      ]
    },
    {
      path: '/StudentCommentAndDiscuss',
      name: 'StudentCommentAndDiscuss',
      component: StudentCommentAndDiscuss,
      children: [
        {
          path: 'StudentAllComment',
          name: 'StudentAllComment',
          component: StudentAllComment
        },
        {
          path: 'StudentComment',
          name: 'StudentComment',
          component: StudentComment
        },
        {
          path: 'StudentAllDiscuss',
          name: 'StudentAllDiscuss',
          component: StudentAllDiscuss
        },
        {
          path: 'StudentDiscuss',
          name: 'StudentDiscuss',
          component: StudentDiscuss
        }
      ]
    },
    {
      path: '/TeacherCommentAndDiscuss',
      name: 'TeacherCommentAndDiscuss',
      component: TeacherCommentAndDiscuss,
      children: [
        {
          path: 'TeacherAllComment',
          name: 'TeacherAllComment',
          component: TeacherAllComment
        },
        {
          path: 'TeacherComment',
          name: 'TeacherComment',
          component: TeacherComment
        },
        {
          path: 'TeacherAllDiscuss',
          name: 'TeacherAllDiscuss',
          component: TeacherAllDiscuss
        },
        {
          path: 'TeacherDiscuss',
          name: 'TeacherDiscuss',
          component: TeacherDiscuss
        }
      ]
    },
    {
      path: '/AdminLogin',
      name: 'AdminLogin',
      component: AdminLogin
    },
    {
      path: '/AdminHead',
      name: 'AdminHead',
      component: AdminHead
    },
    {
      path: '/AdminChange',
      name: 'AdminChange',
      component: AdminChange,
      children: [
        {
          path: 'AdminChange',
          component: AdminChange
        }
      ]
    },
    {
      path: '/StudentTable',
      name: 'StudentTable',
      component: StudentTable,
      children: [
        {
          path: 'StudentTable',
          component: StudentChange
        }
      ]
    },
    {
      path: '/CommentAndDiscussTable',
      name: 'CommentAndDiscussTable',
      component: CommentAndDiscussTable,
      children: [
        {
          path: 'CommentTable',
          name: 'CommentTable',
          component: CommentTable
        },
        {
          path: 'Comment',
          name: 'Comment',
          component: Comment
        },
        {
          path: 'DiscussTable',
          name: 'DiscussTable',
          component: DiscussTable
        },
        {
          path: 'Discuss',
          name: 'Discuss',
          component: Discuss
        }
      ]
    },
    {
      path: '/CourseTable',
      name: 'CourseTable',
      component: CourseTable,
      children: [
        {
          path: 'CourseTable',
          component: CourseTable
        }
      ]
    },
    {
      path: '/MaterialTable',
      name: 'MaterialTable',
      children: [
        {
          path: 'MaterialTable'
        }
      ]
    },
    {
      path: '/TeacherTable',
      name: 'TeacherTable',
      component: TeacherTable,
      children: [
        {
          path: 'TeacherTable',
          component: TeacherTable
        }
      ]
    },
    {
      path: '/StudentSchedule',
      name: 'StudentSchedule',
      component: StudentSchedule
    },
    {
      path: '/TeacherHomework',
      name: 'TeacherHomework',
      component: TeacherHomework
    }
  ]
})
