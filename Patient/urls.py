from re import I
from django.db import models
from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from Patient import views

router = DefaultRouter()
router.register('doctors', views.DoctorsViewSet)  # 医生列表
router.register('user', views.UserViewSet)  # 患者信息
router.register('addOutpatient', views.OutpatientViewSet)  # 添加患者门诊信息
router.register('addExamination', views.ExaminationViewSet)  # 添加患者检查信息
router.register('addTherapy', views.TherapyViewSet)  # 添加患者治疗信息
router.register('addEmergency', views.EmergencyViewSet)  # 添加患者急救信息
router.register('addPhysiological', views.PhysiologicalViewSet)  # 添加患者急救信息
urlpatterns = [
    path('', include(router.urls)),
    url(r'^login/$', views.LoginDoctors.as_view()),  # 医生登陆
    url(r'^updatePwd/$', views.UpdateDoctorsPwd.as_view()),  # 修改密码
    url(r'^addDoctors/$', views.AddDoctors.as_view()),  # 添加医生
    url(r'^updateDoctors/$', views.UpdataDoctors.as_view()),  # 更新医生信息
    url(r'^delDoctors/$', views.DelDoctors.as_view()),  # 删除医生信息
    url(r'^userInfo/$', views.UserInfo.as_view()),  # 根据电话查询患者信息
    url(r'^userInfoUid/$', views.UserInfoUid.as_view()),  # 根据Uid查询患者信息
    url(r'^addUser/$', views.AddUser.as_view()),  # 添加患者信息
    url(r'^delUser/$', views.DelUser.as_view()),  # 删除患者
    url(r'^updateUser/$', views.UpdataUserInfo.as_view()),  # 更新患者信息
    url(r'^outpatientInfo/$', views.OutpatientInfo.as_view()),  # 患者门诊信息
    url(r'^examinationInfo/$', views.ExaminationInfo.as_view()),  # 根据Uid显示患者检查信息
    url(r'^therapyInfo/$', views.TherapyInfo.as_view()),  # 患者治疗信息
    url(r'^emergencyInfo/$', views.EmergencyInfo.as_view()),  # 根据id查询患者急救信息
    url(r'^physiologicalInfo/$', views.PhysiologicalInfo.as_view()),  # 患者生理信息
]
