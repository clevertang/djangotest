from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import os
from app.forms import MomentForm
from django.core.urlresolvers import reverse
from django.shortcuts import render


# Create your views here.
def moments_input(request):
    if request.method == 'POST':
        form = MomentForm(request.POST)
        if form.is_valid():
            moment = form.save()
            moment.save()
            return HttpResponseRedirect(reverse('welcome'))  # reverse连接urls内的name值，来进行反向查找网址
    else:
        form = MomentForm()
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return render(request, os.path.join(PROJECT_ROOT, 'app/templates', 'moment_input.html'),
                  {'form': form})  # 连接到模版文件路径


def welcome(request):
    return HttpResponse('HELLO')
