from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from . import models
from registration.views import logout_page, login_page, register_page

urlpatterns=[
    path('',     views.listPostView,     name='All Posts'),  
    path('<int:blog_post_id>/', views.singlePostView,   name='Single Post'),
    path('aboutMe/', views.aboutTheOwner,    name='About Me'),
    path('sTB/', views.searchTheBlog,    name='Search for Post'),
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register'),
    path('logout/', logout_page, name='logout_page'),
    path('newPost/', views.new_post_view, name='New Post'),
]
urlpatterns+= staticfiles_urlpatterns()