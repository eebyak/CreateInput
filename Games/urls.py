
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^game_list/$', views.game_list, name='game_list'),
    url(r'^gametype_list/$', views.gametype_list, name='gametype_list'),
    url(r'^game_detail/(?P<pk>\d+)/$', views.game_detail, name='game_detail'),
    url(r'^gametype_detail/(?P<pk>\d+)/$', views.gametype_detail, name='gametype_detail'),
    url(r'^game_edit/(?P<pk>\d+)/edit/$', views.game_edit, name='game_edit'),
    url(r'^gametype_edit/(?P<pk>\d+)/edit/$', views.gametype_edit, name='gametype_edit'),
    url(r'^game_new/new/(?P<pk>\d+)/$', views.game_new, name='game_new'),
    url(r'^gametype_new/new/(?P<pk>\d+)/$', views.gametype_new, name='gametype_new'),
]

