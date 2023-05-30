"""
URL configuration for cms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cmsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adduser/', views.add_user, name="add-user"),
    path('updateuser/<int:id>/', views.update_user, name="update-user"),
    path('user/<int:id>/deleteuser/',views.delete_user, name="delete-user"),
    path('allusers/', views.view_users, name='view_users'),

    path('allposts/', views.view_posts.as_view(), name='view_posts'),
    path('addposts/', views.add_posts, name="add-post"),
    path('updatepost/<int:id>/', views.update_post, name="update-post"),
    path('post/<int:id>/deletepost/', views.delete_post, name="delete-post"),

    path('alllikes/', views.view_likes, name='view_likes'),
    path('addlikes/',views.add_likes, name="add-likes"),
    path('updatelike/<int:id>/', views.update_like, name="update-like"),
    path('like/<int:id>/deletelike/', views.delete_like, name="delete-like"),

    path('allpostlikes/',views.view_all.as_view(), name="view_all"),

]
