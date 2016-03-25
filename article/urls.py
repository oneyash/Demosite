from django.conf.urls import url

from article import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>\d+)/detail/$', views.detail, name='detail'),
]