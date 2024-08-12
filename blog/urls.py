from django.urls import include, path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='index'),
    path('"<slug:slug>/"/', views.post_detail,  name='post'),
    path('search/', views.blog, name='search'),
   

    ]