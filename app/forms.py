# -*- coding: utf-8 -*-
"""
@author: clevertang
@license: Apache Licence 
@contact: 961577196@qq.com

@software: PyCharm Community Edition
@file: forms.py
@time: 2017/10/9 22:22
"""
from django.forms import ModelForm
from app.models import Moment

class MomentForm(ModelForm):
    class Meta:
        model=Moment
        fields='__all__'

