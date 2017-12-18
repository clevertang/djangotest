#!/usr/bin/Python
# coding=utf-8
from django.db import models

# Create your models here.
from django.db import models

KIND_CHOICES = (
    (u'裁判文书', u"裁判文书"),
    (u"开庭公告", u"开庭公告"),
    (u"招中标", u"招中标"),

)
province = (
    (u"广东", u"广东"),
    (u"广西", u"广西")
)
is_exist = (
    (u"是", u'是'),
    (u'否', u'否')
)

principal = (
    (u"柏杨", u'柏杨'),
    (u'俊杰', u'俊杰'),
    (u"唐新", u'唐新'),
    (u'陈志超', u'陈志超'),
)


class Moment(models.Model):  # orm,对象关系映射
    topic = models.CharField(u'主题', max_length=20, choices=KIND_CHOICES, default=KIND_CHOICES[0])
    province = models.CharField(u'省份', max_length=20, choices=province, default=province[0])
    city = models.CharField(u'城市', max_length=20, null=True)
    area = models.CharField(u'区域', max_length=20, null=True)
    weight = models.CharField(u'权重', max_length=20, null=True)
    webname = models.CharField(u'网站名称', max_length=20, null=True)
    is_exists = models.CharField(u'是否存在', max_length=20, choices=is_exist, default=is_exist[0])
    enter_module = models.CharField(u'模块名/入口名', max_length=20, null=True)
    url = models.CharField(u'列表页url', max_length=20, null=True)
    cur_total = models.CharField(u'当前数据总量', max_length=20, null=True)
    principal = models.CharField(u'调研人', max_length=20, choices=principal, default=principal[2])
    research_date = models.DateField(u'调研时间', max_length=20, null=True)
    source_of_demand = models.CharField(u'需求来源', max_length=20, null=True)
    remake = models.CharField(u'备注', max_length=20, null=True)
    ctime = models.DateTimeField(max_length=20, auto_now_add=True, auto_created=True)
    utime = models.DateTimeField(max_length=20, auto_now=True, auto_created=True)
