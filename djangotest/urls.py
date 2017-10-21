from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^app/', include('app.urls')), # 建立与app/urls的路由建立连接关系
]