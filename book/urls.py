"""
URL configuration for book project.

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
from django.urls import path, re_path
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register),
    path('login/', views.login),
    path('home/', views.home),
    # 展示所有图书
    path('book/list/', views.book_list, name='book_list'),
    # 添加图书
    path('book/add/', views.book_add, name='book_add'),
    # 展示所有出版社
    path('publish/list/', views.publish_list, name='publish_list'),
    # 添加出版社
    path('publish/add/', views.publish_add, name='publish_add'),
    # 展示所有作者
    path('author/list/', views.author_list, name='author_list'),
    # 添加作者
    path('author/add/', views.author_add, name='author_add'),
    # 编辑图书
    re_path('book/edit/(?P<edit_id>\d+)', views.book_edit, name='book_edit'),
    # 删除图书
    re_path('book/delete/(?P<delete_id>\d+)', views.book_delete, name='book_delete'),
    # 编辑出版社
    re_path('publish/edit/(?P<edit_id>\d+)', views.publish_edit, name='publish_edit'),
    # 删除出版社
    re_path('publish/delete/(?P<delete_id>\d+)', views.publish_delete, name='publish_delete'),
    # 编辑作者
    re_path('author/edit/(?P<edit_id>\d+)', views.author_edit, name='author_edit'),
    # 删除作者
    re_path('author/delete/(?P<delete_id>\d+)', views.author_delete, name='author_delete')
]
