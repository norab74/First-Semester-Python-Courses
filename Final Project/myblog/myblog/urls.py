"""
URL configuration for myblog project.

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
from django.urls import include, path
from registration.views import *
import blog.views as views
import homepage.views as homeViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include("blog.urls")),
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register'),
    path('logout/', logout_page, name='logout_page'),
    path('newPost/', views.new_post_view, name='new_post'),
    path('aboutMe/', views.aboutTheOwner,    name='About Me'),
    path('character/', include('CharacterCreator.urls')),
    path('', homeViews.index, name='Home'),
]