from django.conf.urls import patterns, url

from experiments_admin import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^assignments/', views.assignments, name='assignments'),
    url(r'^experiments/', views.experiments, name='experiments'),
    url(r'^subjects/', views.subjects, name='subjects'),
    url(r'^reucruitment_environments/', views.recruitment_environments, name='recruitment_environments'),
)
