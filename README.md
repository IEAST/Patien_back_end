# Patien_back_end
---
## 写在最前面
本项目为毕业设计项目，写的较拉垮，请见谅。[前端项目](https://github.com/IEAST/Patient_front)

## 目前所用的插件

```bash
pip install django
pip install django-cors-headers
pip install django-rest-framework
```

## 使用方法

修改settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  //数据库驱动
        'NAME': '',   //数据库名称
        'USER': '',   //用户名
        'PASSWORD': '',  //密码
        'HOST': "localhost",
        'PORT': "3306"
    }
}
替换为自己的
```

 进入项目目录

运行启动三件套
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
