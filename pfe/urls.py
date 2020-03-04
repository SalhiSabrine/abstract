from django.conf.urls import url
from . import views

app_name='pfe'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.home, name='home'),
    url(r'^notfoundpage$', views.notfoundpage, name='notfoundpage'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^ajouter$', views.ajouter, name='ajouter'),
    
]
