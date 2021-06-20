from django.db import models
from django.db.models.fields import AutoField
from django.contrib.auth.hashers import make_password, check_password


# 医生表
class Doctors(models.Model):
    Did = models.AutoField('编号', primary_key=True)
    name = models.CharField('姓名', max_length=100, null=False)
    sex = models.CharField(verbose_name='性别', max_length=6, choices=(
        ('male', '男'), ('female', '女')), default='male')
    user = models.CharField('用户名', max_length=30, null=False, unique=True)
    pwd = models.CharField('密码', max_length=100, null=False)
    department = models.IntegerField('科室')

    def __str__(self):
        return self.user

    def set_password(self, password):
        self.pwd = make_password(password)
        return None

    def check_pwd(self, password):
        return check_password(password, self.pwd)


# 急救表
class Emergency(models.Model):
    id = models.AutoField('编号', primary_key=True)
    Did = models.IntegerField('医生编号')
    Uid = models.IntegerField('患者编号')
    Esummary = models.TextField('急救小结')
    Etime = models.DateTimeField('急救时间', auto_now_add=True)


# 检查表
class Examination(models.Model):
    id = models.AutoField('编号', primary_key=True)
    Did = models.IntegerField('医生编号')
    Uid = models.IntegerField('患者编号')
    Ename = models.CharField('项目名称', max_length=100)
    Eresult = models.TextField('检查结果')
    Etime = models.DateTimeField('检查时间', auto_now_add=True)


# 生理信息表
class Physiological(models.Model):
    id = models.AutoField('编号', primary_key=True)
    Did = models.IntegerField('护士编号')
    Uid = models.IntegerField('患者编号')
    Physiological = models.TextField('生理信息')
    Ptime = models.DateTimeField('记录时间', auto_now_add=True)


# 治疗表
class Therapy(models.Model):
    id = models.AutoField('编号', primary_key=True)
    Did = models.IntegerField('医生编号')
    Uid = models.IntegerField('患者编号')
    Tprograms = models.TextField('治疗建议', null=True)
    Ttime = models.DateTimeField('修改时间', auto_now=True)


# 患者表
class Users(models.Model):
    Uid = models.AutoField('编号', primary_key=True)
    name = models.CharField('姓名', max_length=100, null=False)
    sex = models.CharField(verbose_name='性别', max_length=6, choices=(
        ('male', '男'), ('female', '女')), default='male')
    age = models.IntegerField('年龄')
    phone = models.CharField('电话', max_length=11, unique=True, null=False)
    allergy = models.TextField('过敏情况')
    remarks = models.TextField('其他注意事项')


# 门诊表
class Outpatient(models.Model):
    id = models.AutoField('编号', primary_key=True)
    Uid = models.IntegerField('患者编号')
    Did = models.IntegerField('医生编号')
    diagnosis = models.TextField('诊断建议')
    Otime = models.DateTimeField('就诊时间', auto_now_add=True)


# Token表
class Token(models.Model):
    user = models.OneToOneField(Doctors, on_delete=models.CASCADE)  # 与用户一对一关系
    token = models.CharField(max_length=64, verbose_name='token')

    class Meta:
        db_table = 'token'
        verbose_name = 'token表'
        verbose_name_plural = verbose_name
