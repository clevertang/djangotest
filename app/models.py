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
province = (
    ("广东", "广东"),
    ("广西", "广西")
)


class Moment(models.Model):  # orm,对象关系映射
    name = models.CharField(max_length=200)
    site_name = models.CharField(max_length=20, default='广东法院网')
    topic = models.CharField(max_length=20, choices=KIND_CHOICES, default=KIND_CHOICES[0])
    province = models.CharField(max_length=20, choices=province, default=province[0])
    city = models.CharField(max_length=200)
