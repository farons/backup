# backup
### 简介
  * 用于服务端的存储
### 技术框架
  * python 3.6.4
  * mysql
  * flask
  * docker
  
### 版本规则
  * [规范后既定的版本规则](https://blog.csdn.net/yzlll/article/details/84259242)

### 数据库使用
  * 正在构建完成后开始使用mysql数据库
  
### 使用Python包列表
  python freeze -> requirements.txt

### 部署
  * 调整目录结构
  * 获取镜像,启动

### 数据表更新
  * 创建伊始删除migrations文件夹
  * manage.py中导入app.models的数据表模块
  * 初始化: python manage.py db init
  * 创建迁移脚本: python manage.py db migrate
  * 更新数据库: python manage.py db upgrade