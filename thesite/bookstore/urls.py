from django.conf.urls import url

from . import views

app_name='bookstore'

urlpatterns = [
    url(r'^home', views.IndexView.as_view(),name='home'),
    url(r'^bookdetails/(?P<pk>[0-9]+)', views.BookDetails.as_view(), name='bookdetails'),
    url(r'^authordetails/(?P<pk>[0-9]+)', views.AuthorDetails.as_view(), name='authordetails'),
    url(r'^$', views.login, name='login'),
    url(r'register', views.register, name='register'),
]
