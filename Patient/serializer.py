from django.db.models import fields
from rest_framework import serializers
from rest_framework import response
from Patient import models
from rest_framework.views import APIView

from rest_framework.response import Response
import base64


# 添加医生
class DoctorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Doctors
        fields = '__all__'

    # 注册，读取用户名散列后形成密码
    def create(self, validated_data):
        doctors = models.Doctors(**validated_data)
        print(validated_data['user'], '=======')
        doctors.set_password(base64.b64encode(
            validated_data['user'].encode('utf-8')))
        doctors.save()
        return doctors


# 不带密码的医生个人信息
class DoctorInfoSer(serializers.ModelSerializer):
    class Meta:
        model = models.Doctors
        exclude = ('pwd',)


# 医生姓名
class DoctorNameSer(serializers.ModelSerializer):
    class Meta:
        model = models.Doctors
        fields = ('Did', 'name')


# 患者信息,添加患者
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Users
        fields = '__all__'


# 患者门诊信息
class OutpatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Outpatient
        fields = '__all__'


# 患者检查信息
class ExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Examination
        fields = '__all__'


# 患者的治疗信息
class TherapySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Therapy
        fields = '__all__'


# 患者的急救信息
class EmergencySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Emergency
        fields = '__all__'


# 患者的生理信息
class PhysiologicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Physiological
        fields = '__all__'
