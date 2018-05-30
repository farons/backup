# coding=utf-8
from django.db import models


# Create your models here.
class UserKind(models.Model):
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
        db_table = "UserKind"  # 定义数据库的名称

# TODO: 添加用户类，并将UserKind作为它的外键