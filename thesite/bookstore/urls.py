from django.conf.urls import url

from . import views

app_name='bookstore'

urlpatterns = [
    url(r'^home', views.index,name='home'),
    url(r'^bookdetails/(?P<id>[0-9]+)', views.bookdetails, name='bookdetails'),
    url(r'^authordetails/(?P<id>[0-9]+)', views.authordetails, name='authordetails'),
    url(r'^$', views.login, name='login'),
    url(r'register', views.register, name='register'),
]
