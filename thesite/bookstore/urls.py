from django.conf.urls import url

from . import views

app_name='bookstore'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(),name='home'),
    url(r'^bookdetails/(?P<pk>[0-9]+)', views.BookDetails.as_view(), name='bookdetails'),
]
