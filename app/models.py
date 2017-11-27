#!/usr/bin/Python
# coding=utf-8
from django.db import models

# Create your models here.
from django.db import models

KIND_CHOICES = (
    ('裁判文书', "裁判文书"),
    ("开庭公告", "开庭公告"),
    ("招中标", "招中标"),
)
province = ("广东", "广西")


class Moment(models.Model):  # orm,对象关系映射
    入口链接 = models.CharField(max_length=200)
    站点名称 = models.CharField(max_length=20, default='广东法院网')
    主题 = models.CharField(max_length=20, choices=KIND_CHOICES, default=KIND_CHOICES[0])
    省份 = models.CharField(max_length=20, choices=KIND_CHOICES, default=province[0])
    城市 = models.CharField(max_length=200)
