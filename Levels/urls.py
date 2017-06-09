
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^level_list/$', views.level_list, name='level_list'),
    url(r'^level_Entrieslist/(?P<pk>\d+)/$', views.level_Entrieslist, name='level_Entrieslist'),
    url(r'^level_detail/(?P<pk>\d+)/$', views.level_detail, name='level_detail'),
    url(r'^level_edit/(?P<pk>\d+)/edit/$', views.level_edit, name='level_edit'),
    url(r'^level_new/(?P<id>\d+)$', views.level_new, name='level_new'),
    url(r'^level_delete/(?P<pk>\d+)$', views.level_delete, name='level_delete'),
]

