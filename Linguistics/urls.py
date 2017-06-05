
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^linguistics_list/$', views.linguistics_list, name='linguistics_list'),
    url(r'^linguistics_detail/(?P<pk>\d+)/$', views.linguistics_detail, name='linguistics_detail'),
    url(r'^linguistics_edit/(?P<pk>\d+)/edit/$', views.linguistics_edit, name='linguistics_edit'),
    url(r'^linguistics_new/$', views.linguistics_new, name='linguistics_new'),
    url(r'^linguistics_delete/(?P<pk>\d+)$', views.linguistics_delete, name='linguistics_delete'),
]

