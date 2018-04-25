from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    # /music/
    url(r'^$',views.index,name ='index'),
    # path('', views.index, name='index'),

    # /music/71/
    url(r'^(?P<album_id>[0-9a-z]+)/$', views.detail, name='detail'),
]
