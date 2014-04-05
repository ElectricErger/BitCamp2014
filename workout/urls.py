from django.conf.urls import patterns, url

from workout import views

urlpatterns = patterns('',
    # ex: /workout/
    url(r'^$', views.index, name='index'),
    # ex: /workout/5/
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # ex: /workout/5/results/
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /workout/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^applejack/$', views.makeEvent, name='event'),
)