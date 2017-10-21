from django.db import models

# Create your models here.
from django.db import models

KIND_CHOICES=(
    ('Python技术',"Python技术"),
    ("数据库技术","数据库技术"),
    ("经济学","经济学"),
    ("文体咨询",'文体咨询'),
    ("个人心情","个人心情"),
    ("其他","其他")
)

class Moment(models.Model):  # orm,对象关系映射
    content = models.CharField(max_length=200)
    user_name = models.CharField(max_length=20,default='SBT')
    kind = models.CharField(max_length=20,choices=KIND_CHOICES,default=KIND_CHOICES[0])




