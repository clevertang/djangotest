
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'moments_input', views.moments_input),
    url(r'wc', views.welcome, name='welcome'),
]
