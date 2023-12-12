from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *


# student operations
class StudentLogin(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        userPassWord = str(request.GET.get('userPassWord', None))
        print("StudentLogin得到的学号和密码是 " + userName + " " + userPassWord)
        res = Student.objects.filter(id=userName)
        flag = not not res
        print(res)

        if flag:
            print("请求登录的学生账号是%s,其正确密码是%s" % (res[0].id, res[0].password))
            print("请求登录的学生姓名为%s" % res[0].name)
        else:
            print("找不到该学生")

        if flag:
            if userPassWord == res[0].password:
                return Response(dict([('ret', 0), ('userNickName', res[0].name)]))
            else:
                return Response(dict([('ret', 1)]))
        return Response(dict([('ret', 2)]))


class StudentRegister(APIView):
    def get(self, request):
        userNickName = str(request.GET.get('userNickName', None))
        userName = str(request.GET.get('userName', None))
        userPassWord = str(request.GET.get('userPassWord', None))
        userPassWord2 = str(request.GET.get('userPassWord2', None))

        res = Student.objects.filter(id=userName)
        flag = not not res

        if flag:
            print("已经存在学生:" + userName)
        else:
            print("不存在该学生，可以注册:" + userName)
        if flag:
            return Response(1)
        elif userPassWord != userPassWord2:
            return Response(2)
        else:
            student = Student(id=userName, password=userPassWord, name=userNickName)
            student.save()
            return Response(0)


# teacher operations
class TeacherLogin(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        userPassWord = str(request.GET.get('userPassWord', None))
        print("TeacherLogin得到的学号和密码是 " + userName + " " + userPassWord)
        res = Teacher.objects.filter(id=userName)
        flag = not not res
        print(res)

        if flag:
            print("请求登录的教师账号是%s,其正确密码是%s" % (res[0].id, res[0].password))
            print("请求登录的教师姓名为%s" % res[0].name)
        else:
            print("找不到该教师")

        if flag:
            if userPassWord == res[0].password:
                return Response(dict([('ret', 0), ('userNickName', res[0].name)]))
            else:
                return Response(dict([('ret', 1)]))
        return Response(dict([('ret', 2)]))


class TeacherRegister(APIView):
    def get(self, request):
        userNickName = str(request.GET.get('userNickName', None))
        userName = str(request.GET.get('userName', None))
        userPassWord = str(request.GET.get('userPassWord', None))
        userPassWord2 = str(request.GET.get('userPassWord2', None))

        res = Teacher.objects.filter(id=userName)
        flag = not not res

        if flag:
            print("已经存在教师:" + userName)
        else:
            print("不存在该教师，可以注册:" + userName)
        if flag:
            return Response(1)
        elif userPassWord != userPassWord2:
            return Response(2)
        else:
            teacher = Teacher(id=userName, password=userPassWord, name=userNickName)
            teacher.save()
            return Response(0)


# admin operations
class AdminLogin(APIView):
    def get(self, request):
        userName = str(request.GET.get('userName', None))
        userPassWord = str(request.GET.get('userPassWord', None))
        res = Admin.objects.filter(id=userName).all()
        flag = not not res
        print(res)

        if flag:
            if userPassWord == res[0].password:
                return Response(dict([('ret', 0), ('userNickName', res[0].name)]))
            else:
                return Response(dict([('ret', 2)]))
        return Response(dict([('ret', 1)]))


# course operations 实现了返回学生可以选择的课程列表 即已经选择的课程不能出现在选课列表里
class getAllCourses(APIView):
    def get(self, request):
        # c1 = Course(name='1', id=1)
        # c2 = Course(name='2', id=2, introduction='ttttt')
        # c1.save()
        # c2.save()

        userName = str(request.GET.get('userName', None))
        # s1 = Student.objects.filter(id=1).first()
        # t = Course.objects.filter(id=1).first().students.add(s1)
        # userName=s1.id
        res = Course.objects.all()
        ans = []
        for item in res:
            flag = False
            for s in item.students.all():
                if s.id == userName:
                    flag = True
                    break
            if not flag:
                ans.append({'id': item.id, 'name': item.name, 'teacher': item.teacher.name, 'score': item.score, 'introduction': item.introduction})

        ans.sort(key=lambda y: y['id'], reverse=False)

        return Response(ans)


class getCourseList(APIView):
    def get(self, request):
        res = Course.objects.all()
        ans = []
        for item in res:
            ans.append({'id': item.id, 'name': item.name, 'teacher': item.teacher.name, 'score': item.score, 'introduction': item.introduction})
        ans.sort(key=lambda y: y['id'], reverse=False)

        return Response(ans)


class SelectCourse(APIView):
    def get(self, request):
        # t = CourseEval.objects.get(id=1)
        # t.delete()
        # ans = []
        # s = Course.objects.filter(id=1).first()
        # ans.append({'score': s.score})
        # return Response(ans)
        sid = str(request.GET.get('sid', None))
        cid = str(request.GET.get('cid', None))
        student = Student.objects.get(id=sid)
        course = Course.objects.get(id=cid)
        homeworks = HomeWork.objects.filter(course_id=course).all()
        for hm in homeworks:
            sh = Student_homework(sid_id=sid, hid_id=hm.id, state=0)
            sh.save()
        student.courses.add(course)
        return Response(0)


class GetCourseInfo(APIView):
    def get(self, request):
        courseId = int(str(request.GET.get('courseId', None)))
        res = Course.objects.filter(id=courseId).all()
        ans = []
        for item in res:
            ans.append({'id': item.id, 'name': item.name, 'score': item.score, 'introduction': item.introduction})
        ans.sort(key=lambda y: y['id'], reverse=False)
        ans = ans[0]
        return Response(ans)


class StudentPassWordChange(APIView):
    def get(self, request):
        sid = str(request.GET.get('id', None))  # 学号
        userPassWord0 = str(request.GET.get('PassWord0', None))  # 原密码
        userPassWord1 = str(request.GET.get('PassWord1', None))  # 新密码
        userPassWord2 = str(request.GET.get('PassWord2', None))  # 确认新密码
        res = Student.objects.get(id=sid)

        if res.password != userPassWord0:
            return Response(1)
        elif userPassWord1 != userPassWord2:
            return Response(2)
        else:
            Student.objects.filter(id= sid).update(password=userPassWord1)
            return Response(0)


class TeacherPassWordChange(APIView):
    def get(self, request):
        tid = str(request.GET.get('id', None))  # 学号
        userPassWord0 = str(request.GET.get('PassWord0', None))  # 原密码
        userPassWord1 = str(request.GET.get('PassWord1', None))  # 新密码
        userPassWord2 = str(request.GET.get('PassWord2', None))  # 确认新密码
        res = Teacher.objects.get(id=tid)

        if res.password != userPassWord0:
            return Response(1)
        elif userPassWord1 != userPassWord2:
            return Response(2)
        else:
            Teacher.objects.filter(id= tid).update(password=userPassWord1)
            return Response(0)


class AdminPassWordChange(APIView):
    def get(self, request):
        aid = str(request.GET.get('id', None))  # 学号
        userPassWord0 = str(request.GET.get('PassWord0', None))  # 原密码
        userPassWord1 = str(request.GET.get('PassWord1', None))  # 新密码
        userPassWord2 = str(request.GET.get('PassWord2', None))  # 确认新密码
        res = Admin.objects.get(id=aid)

        if res.password != userPassWord0:
            return Response(1)
        elif userPassWord1 != userPassWord2:
            return Response(2)
        else:
            Admin.objects.filter(id=aid).update(password=userPassWord1)
            return Response(0)


class GetStudentCourseList(APIView):
    def get(self, request):
        sid = str(request.GET.get('id', None))
        courses = Student.objects.filter(id=sid).first().courses
        res = []
        for course in courses.all():
            res.append({'id': course.id, 'teacher': course.teacher.name, 'name': course.name, 'introduction': course.introduction})
        res.sort(key=lambda y: y['id'], reverse=False)
        return Response(res)


class DropCourse(APIView):
    def get(self, request):
        sid = str(request.GET.get('sid', None))
        cid = str(request.GET.get('cid', None))
        student = Student.objects.get(id=sid)
        course = Course.objects.get(id=cid)
        student.courses.remove(course)

        homeworks = HomeWork.objects.filter(course_id=cid).all()
        for hm in homeworks:
            Student_homework.objects.filter(sid_id=sid).filter(hid_id=hm.id).all().delete()
        return Response(0)


class GetTeacherCourseList(APIView):
    def get(self, request):
        tid = str(request.GET.get('id', None))
        teacher = Teacher.objects.filter(id=tid).first()
        ans = []
        for course in teacher.course_set.all():
            ans.append({'id': course.id, 'teacher': course.teacher.name,  'name': course.name, 'introduction': course.introduction})
        ans.sort(key=lambda y: y['id'], reverse=False)
        return Response(ans)


class BuildCourse(APIView):
    def get(self, request):
        tid = str(request.GET.get('id', None))
        courseName = str(request.GET.get('name', None))
        courseIntro = str(request.GET.get('introduction', None))
        if courseName == "":
            return Response(1)
        course = Course(name=courseName, introduction=courseIntro, teacher_id=tid)
        course.save()
        return Response(0)


class ChangeCourse(APIView):
    def get(self, request):
        course_id = str(request.GET.get('cid', None))
        course_name = str(request.GET.get('name', None))
        introduction = str(request.GET.get('introduction', None))
        if course_name == '':
            return Response(1)
        res = Course.objects.filter(id=course_id).first()
        res.name, res.introduction = course_name, introduction
        res.save()
        return Response(0)


class CancelCourse(APIView):
    def get(self, request):
        cid = str(request.GET.get('cid', None))
        # 先删除和课程有关的作业、评价
        # cid = 4
        #Course.objects.filter(id=cid).first().courseeval_set.all().delete()
        #Course.objects.filter(id=cid).first().homework_set.all().delete()
        # 删除课程
        Course.objects.filter(id=cid).delete()
        return Response(0)


class GetCommentList(APIView):
    def get(self, request):
        courseId = str(request.GET.get("cid", None))
        # courseId = '3'
        result = CourseEval.objects.filter(course_id=courseId).all()

        commentList = []

        for item in result:
            commentList.append({"id": item.id,
                                "userName": item.student.id,
                                "userNickName": item.student.name,
                                "content": item.content,
                                "time": item.time,
                                "degree": item.score})
        commentList.sort(key=lambda x: x['time'], reverse=True)
        return Response(commentList)


class CommentCourse(APIView):
    def get(self, request):
        # String courseId, String userName, String userNickName, String content, String time
        courseId = str(request.GET.get("cid", None))
        userId = str(request.GET.get("uid", None))
        content = str(request.GET.get("content", None))
        time = str(request.GET.get("time", None))
        score = str(request.GET.get('score', None))

        if score is None:
            score = 5
        Eval = CourseEval(time=time, course_id=courseId, student_id=userId, content=content, score=score)
        Eval.save()
        return Response(0)


class DeleteComment(APIView):
    def get(self, request):
        comment_id = str(request.GET.get("id", None))
        CourseEval.objects.filter(id=comment_id).delete()
        return Response(0)


class TeacherAddHomework(APIView):
    def get(self, request):
        teacher = str(request.GET.get("tid", None))
        course = str(request.GET.get("cid", None))
        end_time = str(request.GET.get("end_time", None))
        content = str(request.GET.get("content", None))
        # teacher = 3
        # course = 3
        # start_time = str(request.GET.get("start_time", None))
        # end_time = str(request.GET.get("end_time", None))
        # content = str(request.GET.get("content", None))

        hm = HomeWork(end=end_time, content=content,
                      isTeacher=1, teacher_id=teacher, course_id=course)
        hm.save()
        return Response(0)


class TeacherChangeHomework(APIView):
    def get(self, request):
        hid = str(request.GET.get("hid", None))
        end_time = str(request.GET.get("end_time", None))
        content = str(request.GET.get("content", None))
        HomeWork.objects.filter(id=hid).update(end=end_time, content=content)
        return Response(0)


class TeacherDeleteHomework(APIView):
    def get(self, request):
        hid = str(request.GET.get("hid", None))
        HomeWork.objects.filter(id=hid).delete()
        return Response(0)


class StudentAddHomework(APIView):
    def get(self, request):
        sid = str(request.GET.get("sid", None))
        course = str(request.GET.get("cid", None))
        end_time = str(request.GET.get("end_time", None))
        content = str(request.GET.get("content", None))

        # sid = 1
        # course = 3
        # start_time = str(request.GET.get("start_time", None))
        # end_time = str(request.GET.get("end_time", None))
        # content = str(request.GET.get("content", None))

        hm = HomeWork(end=end_time, content=content, isTeacher=0, course_id=course, student_id=sid)
        hm.save()
        # Student.objects.filter(id=sid).first().homeworks.add(hm)
        return Response(0)


class StudentChangeHomework(APIView):
    def get(self, request):
        hid = str(request.GET.get("hid", None))
        end_time = str(request.GET.get("end_time", None))
        content = str(request.GET.get("content", None))
        HomeWork.objects.filter(id=hid).update(end=end_time, content=content)
        # homework.end, homework.content = end_time, content
        # homework.save()
        return Response(0)


class StudentDeleteHomework(APIView):   ### delete self not influence other
    def get(self, request):
        hid = str(request.GET.get("hid", None))
        # sid = str(request.GET.get("sid", None))
        HomeWork.objects.filter(id=hid).delete()
        # Student.objects.filter(id=sid).first().homeworks.remove(hm)
        return Response(0)


class StudentChangeHomeworkState(APIView):
    def get(self, request):
        hid = str(request.GET.get("hid", None))
        sid = str(request.GET.get("sid", None))
        state = str(request.GET.get("state", None))
        sh = Student_homework.objects.filter(sid=sid).filter(hid=hid).first()
        sh.state = state
        sh.save()
        return Response(0)


class TeacherHomeworkList(APIView):
    def get(self, request):
        tid = str(request.GET.get("tid", None))
        res = HomeWork.objects.filter(teacher_id=tid).all()
        ret = []
        for hm in res:
            ret.append({'id': hm.id, 'courseName': hm.course.name, 'endTime': hm.end, 'content': hm.content})
        return Response(ret)


class StudentHomeworkList(APIView):
    def get(self, request):
        sid = str(request.GET.get("sid", None))
        ret = []
        # sCourses = Student.objects.filter(id=sid).first().courses.all()
        # for cour in sCourses:
        #     res += HomeWork.objects.filter(isTeacher=1).filter(course=cour).all()
        # res += HomeWork.objects.filter(student_id=sid).all()
        howoks = Student_homework.objects.filter(sid_id=sid).all()
        for sh in howoks:
            hm = sh.hid
            st = False
            md = 0
            if sh.state == 1:
                st = True
            if sh.hid.isTeacher == 0:
                md = 1
            ret.append({'id': hm.id, 'courseName': sh.hid.course.name, 'modified': md, 'endTime': hm.end, 'content': hm.content, 'isTeacher': hm.isTeacher, 'state': st})
        return Response(ret)


class GetMainList(APIView):
    def get(self, request):
        res = MainComment.objects.all()
        postThemeList = []
        p = 0
        for i in res:
            postThemeList.append({"id": i.id,
                                  "userName": '',
                                  "userNickName": '',
                                  "title": i.title,
                                  "content": i.content,
                                  "time": i.time,
                                  "isTeacher": i.isTeacher})
            if i.teacher is not None:
                postThemeList[p]['userName'] = i.teacher.id
                postThemeList[p]['userNickName'] = i.teacher.name
            elif i.student is not None:
                postThemeList[p]['userName'] = i.student.id
                postThemeList[p]['userNickName'] = i.student.name
            else:
                postThemeList[p]['userName'] = i.admin.id
                postThemeList[p]['userNickName'] = i.admin.name
            p += 1
        postThemeList.sort(key=lambda x: x['id'], reverse=True)
        return Response(postThemeList)


class BuildMain(APIView):
    def get(self, request):
        uid = str(request.GET.get("uid", None))
        title = str(request.GET.get("title", None))
        content = str(request.GET.get("content", None))
        time = str(request.GET.get("time", None))
        mtype = int(str(request.GET.get("type", None)))

        # uid = 1
        # title = '1'
        # content = '2'
        # time = '12'
        # mtype = 1

        if mtype == 0:
            Stu = MainComment(title=title, content=content, time=time, student_id=uid, isTeacher=0)
            Stu.save()
        elif mtype == 1:
            Tea = MainComment(title=title, content=content, time=time, teacher_id=uid, isTeacher=1)
            Tea.save()
        else:
            adm = MainComment(title=title, content=content, time=time, admin_id=uid, isTeacher=2)
            adm.save()
        return Response(0)


class GetSecondList(APIView):
    def get(self, request):
        mainId = str(request.GET.get("mainId", None))
        res = SecondComment.objects.filter(mainComment__id=mainId).all()
        secondList = []
        p = 0
        for i in res:
            secondList.append({"id": i.id,
                               "userName": '',
                               "userNickName": '',
                               "content": i.content,
                               "time": i.time,
                               "isTeacher": i.isTeacher})
            if i.teacher is not None:
                secondList[p]['userName'] = i.teacher.id
                secondList[p]['userNickName'] = i.teacher.name
            elif i.student is not None:
                secondList[p]['userName'] = i.student.id
                secondList[p]['userNickName'] = i.student.name
            else:
                secondList[p]['userName'] = i.admin.id
                secondList[p]['userNickName'] = i.admin.name
            p += 1
        secondList.sort(key=lambda x: x['time'], reverse=True)
        return Response(secondList)


class BuildSecond(APIView):
    def get(self, request):
        uid = str(request.GET.get("uid", None))
        mainId = str(request.GET.get("mid", None))
        content = str(request.GET.get("content", None))
        time = str(request.GET.get("time", None))
        mtype = int(str(request.GET.get("type", None)))

        # uid = 1
        # mainId = 1
        # content = '2'
        # time = '12'
        # mtype = 1

        if mtype == 0:
            Stu = SecondComment(content=content, mainComment_id=mainId, time=time, student_id=uid, isTeacher=0)
            Stu.save()
        elif mtype == 1:
            Tea = SecondComment(content=content, mainComment_id=mainId, time=time, teacher_id=uid, isTeacher=1)
            Tea.save()
        else:
            adm = SecondComment(content=content, mainComment_id=mainId, time=time, admin_id=uid, isTeacher=2)
            adm.save()
        return Response(0)


class DeleteMain(APIView):
    def get(self, request):
        mainId = str(request.GET.get("mainId", None))
        MainComment.objects.filter(id=mainId).delete()
        return Response(0)


class DeleteSecond(APIView):
    def get(self, request):
        secondId = str(request.GET.get("secondId", None))
        SecondComment.objects.filter(id=secondId).delete()
        return Response(0)


class GetStudentCourseNum(APIView):
    def get(self, request):
        sid = str(request.GET.get("sid", None))
        cnt = Student.objects.filter(id=sid).first().courses.all().count()
        return Response(cnt)


class GetStudentCommentNum(APIView):
    def get(self, request):
        sid = str(request.GET.get("sid", None))
        cnt = Student.objects.get(id=sid).evalCnt
        return Response(cnt)


class GetStudentDiscussNum(APIView):
    def get(self, request):
        sid = str(request.GET.get("sid", None))
        cnt = Student.objects.filter(id=sid).first().discussCnt
        return Response(cnt)


class GetTeacherCourseNum(APIView):
    def get(self, request):
        tid = str(request.GET.get("tid", None))
        cnt = Teacher.objects.filter(id=tid).first().courseCnt
        return Response(cnt)


class GetTeacherDiscussNum(APIView):
    def get(self, request):
        tid = str(request.GET.get("tid", None))
        cnt = Teacher.objects.filter(id=tid).first().discussCnt
        return Response(cnt)


class GetStudentList(APIView):
    def get(self, request):
        result = Student.objects.all()
        studentList = []
        for item in result:
            studentList.append(dict([("id", item.id), ("name", item.name)]))
        return Response(studentList)


class GetTeacherList(APIView):
    def get(self, request):
        result = Teacher.objects.all()
        teacherList = []
        for item in result:
            teacherList.append(dict([("id", item.id), ("name", item.name)]))
        return Response(teacherList)


class GetDegree(APIView):
    def get(self, request):
        cid = str(request.GET.get('id', None))
        cnt = Course.objects.filter(id=cid).first().score
        return Response(cnt)


class GetMain(APIView):
    def get(self, request):
        mainId = str(request.GET.get('mainId', None))
        r = MainComment.objects.filter(id=mainId).first()
        dic = {"id": r.id, "userName": '', "userNickName": '',
               "title": r.title, "content": r.content, "time": r.time,
               "isTeacher": r.isTeacher}
        print(dic)
        if r.isTeacher == 1:
            dic["userName"] = r.teacher.id
            dic["userNickName"] = r.teacher.name
        elif r.isTeacher == 0:
            dic["userName"] = r.student.id
            dic["userNickName"] = r.student.name
        else :
            dic["userName"] = r.admin.id
            dic["userNickName"] = r.admin.name
        return Response(dic)
