# 视频监控项目_web

## 使用方法

1. 修改数据库密码

```python
# 文件路径 Video_Surveillance\Video_Surveillance\settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # 无需修改
        'NAME': '',  # 数据库名称
        'USER': '',  # 数据库用户名
        'PASSWORD': '',  # 数据库密码
        'HOST': '127.0.0.1',  # 无需修改
        'PORT': '3306',  # 一般为此端口，请根据自己的需要修改
    }
}
```

2. 进入前端目录 

```
cd appfront
```

3. 安装所需依赖

```
npm install
```
4. 构建项目

```
npm build
```
5. 进入项目根目录

```
cd ..
```

6. 迁移文件

```python
python manage.py makemigrations
python manage.py migrate
```

7. 运行项目

## 配置要求
+ 后端框架 Django
+ python3
+ 前端框架 Vue and element
+ 配置数据库 MySQL



