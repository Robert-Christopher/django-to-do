from django.conf.urls import url

from . import views

app_name = 'tasks'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.new, name='new'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<task_id>[0-9]+)/$', views.show, name='show'),
    url(r'^edit/(?P<task_id>[0-9]+)/$', views.edit, name='edit'),
    url(r'^delete/(?P<task_id>[0-9]+)/$', views.delete, name='delete'),
]
