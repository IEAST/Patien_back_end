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

新建 `Patien_back_end/Patien_back_end/conf.ini`文件，修改里面的内容或者修改`setting.py`中`cf.read("Patien_back_end/conf.ini")`指向的文件地址。
    ```ini
    [Database]
    ENGINE=django.db.backends.mysql 
    ;数据库名称
    NAME= 
    ;登陆的用户名
    USER=
    ;登陆密码
    PASSWORD=
    ;数据库地址
    HOST=
    ;端口号
    PORT=
    [SECRET_KEY]
    ;setting.py文件中的secret_key的值
    SECRET_KEY =  
    
    ```


进入项目目录

运行启动三件套
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
