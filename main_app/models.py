# coding=utf-8
from django.db import models


# Create your models here.
class UserKind(models.Model):
    """
    用户的类型表，其实没用的，用于学习django中表的关系应用
    """
    TOURIST = 'T'
    USER = 'U'
    # U、T是存入数据库的值，游客和用户是用于显示的值
    USER_KIND = (
        (TOURIST, '游客'),
        (USER, '用户')
    )
    id = models.AutoField("用户分类的id", primary_key=True)  # 使用自己的id重写默认的id
    userKind = models.CharField("用户的分类", max_length=5, choices=USER_KIND, default=TOURIST)

    def is_short_class(self):
        return self.userLevel in (self.TOURIST, self.USER)

    class Meta:
        db_table = "UserKind"  # 定义用户类型数据表的名称

    def __str__(self):
        return self.userKind


class User(models.Model):
    """
    用户表
    """
    MAN = 'man'
    WOMAN = 'woman'
    ACTIVE = 'active'
    FREEZE = 'freeze'
    SEX_KIND = (
        (MAN, '男'),
        (WOMAN, '女' )
    )
    STATUS_KIND = (
        (ACTIVE, '正常'),
        (FREEZE, '冻结')
    )
    id = models.AutoField("用户的id", primary_key=True)
    name = models.CharField("用户的姓名，汉字", max_length=25)
    username = models.CharField("用户名", max_length=25)
    password = models.CharField("用户的登录密码", max_length=15)
    email = models.EmailField("用户的Email")
    sex = models.CharField("用户的性别", choices=SEX_KIND, default=MAN, max_length=5)
    image = models.CharField("用户的头像地址", max_length=50)
    belongKind = models.ForeignKey('UserKind')
    status = models.CharField("用户的状态", choices=STATUS_KIND, default=ACTIVE, max_length=15)

    class Meta:
        db_table = "User"  # 定义用户数据表名称

    def __str__(self):
        return self.username


class Resource(models.Model):
    """
    用户云端同步的文件
    """
    MUSIC = 'music'
    VIDEO = 'video'
    DOCUMENT = 'document'

    RE_KIND = (
        (MUSIC, '音频'),
        (VIDEO, '视频'),
        (DOCUMENT, '文档'),
    )

    id = models.AutoField("文件的ID", primary_key=True)
    title = models.CharField("文件的标题", max_length=50)
    address = models.CharField("文件的地址", max_length=50)
    size = models.IntegerField("文件的大小")
    createTime = models.DateTimeField("文件初次上传的时间")
    modifyTime = models.DateTimeField("文件修改的时间")
    belongUser = models.ForeignKey('User')
    status = models.CharField("文件的状态,保留吧，暂时用不到", max_length=10)
    belongKind = models.CharField("文件的类型", choices=RE_KIND, default=DOCUMENT, max_length=10)

    class Meta:
        db_table = "Resource"

    def __str__(self):
        return self.title


# TODO: 建立日志类型表，日志表，暂时不用，