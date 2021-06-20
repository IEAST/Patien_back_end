
from re import U
from typing import cast
from django.conf import settings
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView
from Patient import models
from Patient.utils import md5
from Patient import serializer as Ser
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from django.core import serializers
import base64


# 在治疗项目中显示医生名称
def seleDoc(data):
    Dmsg = []
    for d_data in data:
        try:
            doctor = models.Doctors.objects.get(
                Did=d_data['fields']['Did'])
            Dmsg.append(Ser.DoctorNameSer(doctor).data)
        except:
            return Response({'info': '系统错误'})
    return Dmsg


# 医生详情
class DoctorsViewSet(viewsets.ModelViewSet):
    queryset = models.Doctors.objects.all()
    serializer_class = Ser.DoctorInfoSer


# 修改医生密码
class UpdateDoctorsPwd(APIView):
    def post(self, request):
        Duser = request.data.get('user')
        Dpwd = request.data.get('pwd')
        Dnpwd = request.data.get('Npwd')
        if not all([Duser, Dpwd, Dnpwd]):
            return Response({'info': '参数不完整', 'code': 400})
        doctor = models.Doctors.objects.get(user=Duser)
        if not doctor.check_pwd(Dpwd):
            return Response({'info': '密码错误', 'code': 300})
        doctor.set_password(Dnpwd)
        print(doctor.pwd)
        doctor.save()
        res = {'info': '完成', 'code': 200,
               'data': Ser.DoctorInfoSer(doctor).data}
        return Response(res)


# 医生登陆验证
class LoginDoctors(APIView):

    authentication_classes = []

    def post(self, request):
        Duser = request.data.get('user')
        Dpwd = request.data.get('pwd')
        if not all([Duser, Dpwd]):
            return Response({'info': '参数不完整', 'code': 400})
        try:
            doctor = models.Doctors.objects.get(user=Duser)
        except:
            return Response({'info': '未找到该用户', 'code': 404})
        if not doctor.check_pwd(Dpwd):
            return Response({'info': '用户名密码错误', 'code': 300})
        token = md5(Duser)
        models.Token.objects.update_or_create(
            user=doctor, defaults={'token': token})
        res = {'info': 'success', 'token': token,
               'code': 200}
        res['data'] = Ser.DoctorInfoSer(doctor).data
        return Response(res)


# 医生注册
class AddDoctors(APIView):
    def post(self, request):
        name = request.data.get('name')
        user = request.data.get('user')
        sex = request.data.get('sex')
        department = request.data.get('department')
        if not all([user, sex, department, name]):
            return Response({'info': '参数不完整', 'code': 400})
        try:
            doctor = models.Doctors.objects.get(user=user)
            return Response({'info': '该用户名已存在', 'code': 300})
        except:
            doctor = models.Doctors()
        doctor.user = user
        doctor.sex = sex
        doctor.name = name
        doctor.set_password(base64.b64encode(user.encode('utf-8')))
        doctor.department = department
        doctor.save()
        res = {'info': '完成', 'code': 200,
               'data': Ser.DoctorInfoSer(doctor).data}
        return Response(res)


# 医生信息更新
class UpdataDoctors(APIView):
    def post(self, request):
        Did = request.data.get('Did')
        name = request.data.get('name')
        user = request.data.get('user')
        sex = request.data.get('sex')
        department = request.data.get('department')
        if not all([Did, user, sex, department, name]):
            return Response({'info': '参数不完整', 'code': 400})
        try:
            doctor = models.Doctors.objects.get(Did=Did)
        except:
            return Response({'info': '参数错误', 'code': 300})
        doctor.Did = Did
        doctor.user = user
        doctor.sex = sex
        doctor.name = name
        doctor.department = department
        doctor.save()
        res = {'info': '完成', 'code': 200,
               'data': Ser.DoctorInfoSer(doctor).data}
        return Response(res)


# 根据id删除医生信息
class DelDoctors(APIView):
    def post(self, request):
        Did = request.data.get('Did')
        try:
            doctor = models.Doctors.objects.get(Did=Did).delete()
        except:
            return Response({'info': '参数错误', 'code': 300})
        res = {'info': '完成', 'code': 200}
        return Response(res)


# 患者信息
class UserViewSet(viewsets.ModelViewSet):
    queryset = models.Users.objects.all()
    serializer_class = Ser.UserSerializer


# 患者注册
class AddUser(APIView):
    def post(self, request):
        name = request.data.get('name')
        sex = request.data.get('sex')
        age = request.data.get('age')
        phone = request.data.get('phone')
        allergy = request.data.get('allergy')
        remarks = request.data.get('remarks')
        if not all([name, sex, age, phone, allergy, remarks]):
            return Response({'info': '参数不完整', 'code': 400})
        try:
            user = models.Users.objects.get(phone=phone)
            return Response({'info': '该手机号以注册', 'code': 300})
        except:
            user = models.Users()
        user.name = name
        user.sex = sex
        user.age = age
        user.phone = phone
        user.allergy = allergy
        user.remarks = remarks
        user.save()
        res = {'info': '完成', 'code': 200,
               'data': Ser.UserSerializer(user).data}
        return Response(res)


# 患者信息更新
class UpdataUserInfo(APIView):
    def post(self, request):
        Uid = request.data.get('Uid')
        name = request.data.get('name')
        sex = request.data.get('sex')
        age = request.data.get('age')
        phone = request.data.get('phone')
        allergy = request.data.get('allergy')
        remarks = request.data.get('remarks')
        if not all([Uid, name, sex, age, phone, allergy, remarks]):
            return Response({'info': '参数不完整', 'code': 400})
        user = models.Users.objects.get(Uid=Uid)
        user.name = name
        user.sex = sex
        user.age = age
        user.phone = phone
        user.allergy = allergy
        user.remarks = remarks
        user.save()
        res = {'info': 'success', 'code': 200}
        res['data'] = Ser.UserSerializer(user).data
        return Response(res)


# 根据电话查看单一患者信息
class UserInfo(APIView):
    def post(self, request):
        Uphone = request.data.get('phone')
        print(Uphone)
        try:
            user = models.Users.objects.get(phone=Uphone)
        except:
            return Response({'info': '此号码未注册,请确认输入正确', 'code': 300})
        res = {'info': '完成', 'code': 200,
               'data': Ser.UserSerializer(user).data}
        return Response(res)


# 通过Uid来查询用户信息
class UserInfoUid(APIView):
    def post(self, request):
        Uid = request.data.get('Uid')
        print(Uid)
        try:
            user = models.Users.objects.get(Uid=Uid)
        except:
            return Response({'info': '发生错误,请确认输入正确', 'code': 300})
        res = {'info': '完成', 'code': 200,
               'data': Ser.UserSerializer(user).data}
        return Response(res)


# 根据id删除患者信息
class DelUser(APIView):
    def post(self, request):
        Uid = request.data.get('Uid')
        print(id)
        try:
            models.Users.objects.get(Uid=Uid).delete()
        except:
            return Response({'info': '错误', 'code': 300})
        res = {'info': '完成', 'code': 200}
        return Response(res)


# 查看患者门诊信息,包含就诊时间和医生姓名
class OutpatientInfo(APIView):
    def post(self, request):
        Uid = request.data.get('Uid')
        try:
            outp = models.Outpatient.objects.filter(Uid=Uid)
        except:
            return Response({'info': '未找到该用户的就诊信息'})
        out_data = serializers.serialize('json', outp)
        out_data = json.loads(out_data)
        Dmsg = seleDoc(out_data)
        res = {'info': '完成', 'code': 200,
               'User_data': out_data,
               'Doctor_data': Dmsg}
        return Response(res)


# 添加患者门诊信息
class OutpatientViewSet(viewsets.ModelViewSet):
    queryset = models.Outpatient.objects.all()
    serializer_class = Ser.OutpatientSerializer


# 添加检查结果信息
class ExaminationViewSet(viewsets.ModelViewSet):
    queryset = models.Examination.objects.all()
    serializer_class = Ser.ExaminationSerializer


# 显示检查结果信息
class ExaminationInfo(APIView):
    def post(self, request):
        Uid = request.data.get('Uid')
        try:
            examinationInfo = models.Examination.objects.filter(Uid=Uid)
        except:
            return Response({'info': '未找到该用户的检查信息'})
        examination_data = serializers.serialize('json', examinationInfo)
        examination_data = json.loads(examination_data)
        Dmsg = seleDoc(examination_data)
        res = {'info': '完成', 'code': 200,
               'Examination_data': examination_data,
               'Doctor_data': Dmsg}
        return Response(res)


# 添加治疗信息
class TherapyViewSet(viewsets.ModelViewSet):
    queryset = models.Therapy.objects.all()
    serializer_class = Ser.TherapySerializer


# 显示患者的治疗信息
class TherapyInfo(APIView):
    def post(self, request):
        Uid = request.data.get('Uid')
        try:
            therapyInfo = models.Therapy.objects.filter(Uid=Uid)
        except:
            return Response({'info': '未找到该用户的治疗信息'})
        therapy_data = serializers.serialize('json', therapyInfo)
        therapy_data = json.loads(therapy_data)
        Dmsg = seleDoc(therapy_data)
        res = {'info': '完成', 'code': 200,
               'Therapy_data': therapy_data,
               'Doctor_data': Dmsg}
        return Response(res)


# 添加患者急救信息
class EmergencyViewSet(viewsets.ModelViewSet):
    queryset = models.Emergency.objects.all()
    serializer_class = Ser.EmergencySerializer


# 显示患者的急救信息
class EmergencyInfo(APIView):
    def post(self, request):
        Uid = request.data.get('Uid')
        try:
            emergencyInfo = models.Emergency.objects.filter(Uid=Uid)
        except:
            return Response({'info': '未找到该用户的检查信息'})
        emergency_data = serializers.serialize('json', emergencyInfo)
        emergency_data = json.loads(emergency_data)
        Dmsg = seleDoc(emergency_data)
        res = {'info': '完成', 'code': 200,
               'Emergency_data': emergency_data,
               'Doctor_data': Dmsg}
        return Response(res)


# 添加患者的生理信息
class PhysiologicalViewSet(viewsets.ModelViewSet):
    queryset = models.Physiological.objects.all()
    serializer_class = Ser.PhysiologicalSerializer


# 显示患者的生理信息
class PhysiologicalInfo(APIView):
    def post(self, request):
        Uid = request.data.get('Uid')
        try:
            physiologicalInfo = models.Physiological.objects.filter(Uid=Uid)
        except:
            return Response({'info': '未找到该用户的检查信息'})
        physiological_data = serializers.serialize('json', physiologicalInfo)
        physiological_data = json.loads(physiological_data)
        Dmsg = seleDoc(physiological_data)
        res = {'info': '完成', 'code': 200,
               'Physiological_data': physiological_data,
               'Doctor_data': Dmsg}
        return Response(res)
