
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^readit/$', views.readit, name='readit'),
    url(r'^write/$', views.write, name='write'),
    url(r'^post_list/$', views.post_list, name='post_list'),
    url(r'^entry_list/$', views.entry_list, name='entry_list'),
    url(r'^entry/$', views.entry, name='entry'),
    url(r'^$', views.entry_list, name='entry_list'),
    url(r'^entry/(?P<pk>\d+)/$', views.entry_detail, name='entry_detail'),
    url(r'^entry/(?P<pk>\d+)/edit/$', views.entry_edit, name='entry_edit'),
    url(r'^entry/new/(?P<pk>\d+)/$', views.entry_new, name='entry_new'),
]

