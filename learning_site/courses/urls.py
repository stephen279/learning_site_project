from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.course_list, name='list'),
    url(r'(?P<course_pk>\d+)/t(?P<step_pk>\d+)/$', views.text_details,
        name='text'),
    url(r'(?P<course_pk>\d+)/q(?P<step_pk>\d+)/$', views.quiz_detail,
        name='quiz'),
    url(r'(?P<course_pk>\d+)/qy(?P<step_pk>\d+)/$', views.query_detail,
        name='query'),
    url(r'(?P<course_pk>\d+)/create_quiz/$', views.quiz_create,
        name='create_quiz'),
    url(r'(?P<course_pk>\d+)/(?P<step_pk>\d+)/create_query/$', views.query_create,
        name='create_query'),

    url(r'(?P<pk>\d+)/$', views.course_detail, name='detail'),

]