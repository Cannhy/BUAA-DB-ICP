from django.db import models
from django.db.models.signals import post_save, post_delete, pre_delete
from django.db.models import Avg,Max,Min,Count,Sum  #   引入函数
from django.dispatch import receiver

# Create your models here.
import pymysql


class Student(models.Model):
    id = models.CharField(verbose_name='学号', max_length=40, primary_key=True)
    name = models.CharField(verbose_name='学生姓名', max_length=128)
    password = models.CharField(verbose_name='学生密码', max_length=128)
    evalCnt = models.IntegerField(verbose_name='课程评价总数', default=0)
    discussCnt = models.IntegerField(verbose_name='主次评论总数', default=0)
    courses = models.ManyToManyField('Course', related_name='students')
    # homeworks = models.ManyToManyField('HomeWork', related_name='students')

    class Meta:
        db_table = 'student'
        indexes = [models.Index(fields=['id'])]


class Teacher(models.Model):
    id = models.CharField(verbose_name='教师工号', max_length=40, primary_key=True)
    name = models.CharField(verbose_name='教师姓名', max_length=128)
    password = models.CharField(verbose_name='教师密码', max_length=128)
    discussCnt = models.IntegerField(verbose_name='主次评论总数', default=0)
    courseCnt = models.IntegerField(verbose_name='开设课程数', default=0)

    class Meta:
        db_table = 'teacher'
        indexes = [models.Index(fields=['id'])]


class Admin(models.Model):
    id = models.CharField(verbose_name='管理员账号', max_length=40, primary_key=True)
    name = models.CharField(verbose_name='管理员名称', max_length=128)
    password = models.CharField(verbose_name='管理员密码', max_length=128)

    class Meta:
        db_table = 'admin'
        indexes = [models.Index(fields=['id'])]


class Course(models.Model):
    id = models.AutoField(verbose_name='课程ID', primary_key=True)
    name = models.CharField(verbose_name='课程名字', max_length=128)
    score = models.DecimalField(verbose_name='课程评分', max_digits=10, decimal_places=2, default=5.00)
    introduction = models.CharField(verbose_name='课程介绍', max_length=1000)
    teacher = models.ForeignKey('Teacher', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'course'
        indexes = [models.Index(fields=['id'])]


@receiver(post_save, sender=Course)
def update_course_num_after_save(sender, instance, **kwargs):
    teacher = instance.teacher
    precnt = teacher.courseCnt
    teacher.courseCnt = precnt + 1
    teacher.save()


@receiver(pre_delete, sender=Course)
def update_course_num_after_del(sender, instance, **kwargs):
    teacher = instance.teacher
    precnt = teacher.courseCnt
    teacher.courseCnt = precnt - 1
    teacher.save()


class CourseEval(models.Model):
    id = models.AutoField(verbose_name='评价ID', primary_key=True)
    time = models.CharField(verbose_name='评价时间', max_length=128)
    content = models.CharField(verbose_name='评价内容', max_length=1000)
    score = models.IntegerField(verbose_name='课程评分', default=5)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)

    class Meta:
        db_table = 'courseEval'
        indexes = [models.Index(fields=['id'])]


@receiver(post_save, sender=CourseEval)  ### 此处不仅更新课程评分 也更新该学生的评价数量
def update_course_score_after_save(sender, instance, **kwargs):
    student = instance.student
    scnt = student.evalCnt
    student.evalCnt = scnt + 1
    student.save()
    ida = instance.course.id
    res = CourseEval.objects.filter(course_id=ida).aggregate(avgg=Avg("score"))
    obj = Course.objects.get(id=ida)
    obj.score = res['avgg']
    obj.save()


@receiver(pre_delete, sender=CourseEval)
def update_course_score_after_delete(sender, instance, **kwargs):
    student = instance.student
    scnt = student.evalCnt
    student.evalCnt = scnt - 1
    student.save()
    course = instance.course
    comments = CourseEval.objects.filter(course=course).exclude(id=instance.id)
    sc = sum([comment.score for comment in comments.all()])
    course.score = sc / comments.count() if comments.count() > 0 else 5.0
    course.save()


class HomeWork(models.Model):
    id = models.AutoField(verbose_name='作业ID', primary_key=True)
    end = models.CharField(verbose_name='作业结束时间', max_length=128)
    content = models.CharField(verbose_name='作业内容', max_length=1000)
    isTeacher = models.IntegerField(verbose_name='是否教师布置')
    teacher = models.ForeignKey('Teacher', blank=True, null=True, on_delete=models.CASCADE)
    student = models.ForeignKey('Student', blank=True, null=True, on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)

    class Meta:
        db_table = 'homework'
        indexes = [models.Index(fields=['id'])]


@receiver(post_save, sender=HomeWork)
def update_homework_after_add(sender, instance, **kwargs):
    if instance.isTeacher == 1:
        course = instance.course
        students = course.students.all()
        for student in students:
            sh = Student_homework(sid=student, hid=instance, state=0)
            sh.save()
    elif instance.isTeacher == 0:
        sh = Student_homework(sid=instance.student, hid=instance, state=0)
        sh.save()


@receiver(pre_delete, sender=HomeWork)
def update_homework_after_del(sender, instance, **kwargs):
    if instance.isTeacher == 1:
        homeworks = Student_homework.objects.filter(hid=instance).all()
        homeworks.delete()
    elif instance.isTeacher == 0:
        homeworks = Student_homework.objects.filter(hid=instance).filter(sid=instance.student).all()
        homeworks.delete()


class MainComment(models.Model):
    id = models.AutoField(verbose_name='主评论ID', primary_key=True)
    title = models.CharField(verbose_name='主评论标题', max_length=1000)
    time = models.CharField(verbose_name='主评论发表时间', max_length=100)
    isTeacher = models.IntegerField(verbose_name='是否教师发帖')
    content = models.CharField(verbose_name='主评论内容', max_length=1000)
    student = models.ForeignKey('Student', blank=True, null=True, on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', blank=True, null=True, on_delete=models.CASCADE)
    admin = models.ForeignKey('Admin', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'mainComment'
        indexes = [models.Index(fields=['id'])]


@receiver(post_save, sender=MainComment)
def update_user_MdiscussCnt_after_add(sender, instance, **kwargs):
    if instance.isTeacher == 1:
        teacher = instance.teacher
        preCnt = teacher.discussCnt
        teacher.discussCnt = preCnt + 1
        teacher.save()
    elif instance.isTeacher == 0:
        student = instance.student
        preCnt = student.discussCnt
        student.discussCnt = preCnt + 1
        student.save()


@receiver(pre_delete, sender=MainComment)
def update_user_MdiscussCnt_after_del(sender, instance, **kwargs):
    if instance.isTeacher == 1:
        teacher = instance.teacher
        preCnt = teacher.discussCnt
        teacher.discussCnt = preCnt - 1
        teacher.save()
    elif instance.isTeacher == 0:
        student = instance.student
        preCnt = student.discussCnt
        student.discussCnt = preCnt - 1
        student.save()


class SecondComment(models.Model):
    id = models.AutoField(verbose_name='次评论ID', primary_key=True)
    time = models.CharField(verbose_name='次评论发表时间', max_length=100)
    isTeacher = models.IntegerField(verbose_name='是否教师发帖')
    content = models.CharField(verbose_name='次评论内容', max_length=1000)
    mainComment = models.ForeignKey('MainComment', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', blank=True, null=True, on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', blank=True, null=True, on_delete=models.CASCADE)
    admin = models.ForeignKey('Admin', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'secondComment'
        indexes = [models.Index(fields=['id'])]


@receiver(post_save, sender=SecondComment)
def update_user_SdiscussCnt_after_add(sender, instance, **kwargs):
    if instance.isTeacher == 1:
        teacher = instance.teacher
        preCnt = teacher.discussCnt
        teacher.discussCnt = preCnt + 1
        teacher.save()
    elif instance.isTeacher == 0:
        student = instance.student
        preCnt = student.discussCnt
        student.discussCnt = preCnt + 1
        student.save()


@receiver(pre_delete, sender=SecondComment)
def update_user_SdiscussCnt_after_del(sender, instance, **kwargs):
    if instance.isTeacher == 1:
        teacher = instance.teacher
        preCnt = teacher.discussCnt
        teacher.discussCnt = preCnt - 1
        teacher.save()
    elif instance.isTeacher == 0:
        student = instance.student
        preCnt = student.discussCnt
        student.discussCnt = preCnt - 1
        student.save()


class Student_homework(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True)
    sid = models.ForeignKey('Student', on_delete=models.CASCADE)
    hid = models.ForeignKey('HomeWork', on_delete=models.CASCADE)
    state = models.IntegerField('是否完成')

    class Meta:
        db_table = 'student_homework'
        indexes = [models.Index(fields=['id'])]


class Student_main(models.Model):
    sid = models.ForeignKey('Student', on_delete=models.CASCADE)
    mid = models.ForeignKey('MainComment', on_delete=models.CASCADE)

    class Meta:
        db_table = 'student_main'
        indexes = [models.Index(fields=['sid', 'mid'])]


class Teacher_main(models.Model):
    tid = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    mid = models.ForeignKey('MainComment', on_delete=models.CASCADE)

    class Meta:
        db_table = 'teacher_main'
        indexes = [models.Index(fields=['tid', 'mid'])]


class Admin_main(models.Model):
    aid = models.ForeignKey('Admin', on_delete=models.CASCADE)
    mid = models.ForeignKey('MainComment', on_delete=models.CASCADE)

    class Meta:
        db_table = 'admin_main'
        indexes = [models.Index(fields=['aid', 'mid'])]


class Student_second(models.Model):
    sid = models.ForeignKey('Student', on_delete=models.CASCADE)
    secid = models.ForeignKey('SecondComment', on_delete=models.CASCADE)

    class Meta:
        db_table = 'student_second'
        indexes = [models.Index(fields=['sid', 'secid'])]


class Teacher_second(models.Model):
    tid = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    secid = models.ForeignKey('SecondComment', on_delete=models.CASCADE)

    class Meta:
        db_table = 'teacher_second'
        indexes = [models.Index(fields=['tid', 'secid'])]


class Admin_second(models.Model):
    aid = models.ForeignKey('Admin', on_delete=models.CASCADE)
    secid = models.ForeignKey('SecondComment', on_delete=models.CASCADE)

    class Meta:
        db_table = 'admin_second'
        indexes = [models.Index(fields=['aid', 'secid'])]


class student_add_homework(models.Model):
    sid = models.ForeignKey('Student', on_delete=models.CASCADE)
    hid = models.ForeignKey('HomeWork', on_delete=models.CASCADE)

    class Meta:
        db_table = 'student_add_homework'
        indexes = [models.Index(fields=['hid', 'sid'])]


class teacher_add_homework(models.Model):
    tid = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    hid = models.ForeignKey('HomeWork', on_delete=models.CASCADE)

    class Meta:
        db_table = 'teacher_add_homework'
        indexes = [models.Index(fields=['hid', 'tid'])]