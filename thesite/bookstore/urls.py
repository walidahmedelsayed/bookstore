from django.conf.urls import url

from . import views

app_name='bookstore'

urlpatterns = [
    url(r'^$', views.IndexView.as_view()),

]
