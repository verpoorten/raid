from django.conf.urls import url
from django.contrib.auth.views import login,logout
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    # login / logout urls
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),

    url(r'^reglement', views.reglement, name='reglement'),
    url(r'^inscription', views.inscription, name='inscription'),
    url(r'^inscriptions', views.inscriptions, name='inscriptions'),
    url(r'^inscription/add', views.inscription_add, name='add_inscription'),

]
