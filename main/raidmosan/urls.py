from django.conf.urls import url
from django.contrib.auth.views import login,logout
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    # login / logout urls
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),

    url(r'^reglement',          views.reglement,        name='reglement'),
    url(r'^contact',            views.contact,          name='contact'),
    url(r'^classement',         views.classement,       name='classement'),
    url(r'^photos',             views.photos,           name='photos'),
    url(r'^inscription',        views.inscription,      name='inscription'),
    url(r'^inscription/list/$', views.inscriptions,     name='inscriptions'),
    url(r'^inscription2/list/$', views.test,     name='inscriptions2'),
    url(r'^add_inscription/$',  views.inscription_add,  name='add_inscription'),
    url(r'^test/$',  views.test,  name='test'),
    url(r'^xls_inscriptions/$',  views.xls_inscriptions,  name='xls_inscriptions'),


]
