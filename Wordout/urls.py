
from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^$', views.index, name='index'),
url(r'^wordout_associate/$', views.wordout_associate, name='wordout_associate'),
url(r'^wordout_list/$', views.wordout_list, name='wordout_list'),
url(r'^wordout_print/(?P<pk>\d+)/$', views.wordout_print, name='wordout_print'),
url(r'^wordout_add/(?P<pk>\d+)/$', views.wordout_add, name='wordout_add'),
url(r'^wordout_add_distractor/(?P<rpk>\d+)/(?P<gpk>\d+)/$', views.wordout_add_distractor, name='wordout_add_distractor'),
]

