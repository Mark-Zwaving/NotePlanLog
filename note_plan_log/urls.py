"""Plan_and_Log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from . views import ( home_view,  write_log_view, write_plan_view,
                      read_log_view, read_plan_view, about_view,
                      register_view, login_view, language_view,
                      notes_view, logout_view
                      )

urlpatterns = [
    path('secret-path/',   admin.site.urls),
    path( '',              home_view,         name = 'Home' ),
    path( 'write-log/',    write_log_view,    name = 'Write logs' ),
    path( 'write-plan/',   write_plan_view,   name = 'Write plans' ),
    path( 'read-log/',     read_log_view,     name = 'Read logs' ),
    path( 'read-plan/',    read_plan_view,    name = 'Read plans' ),
    path( 'about/',        about_view,        name = 'About this page' ),
    path( 'register/',     register_view,     name = 'Register' ),
    path( 'login/',        login_view,        name = 'Login' ),
    path( 'logout/',       logout_view,       name = 'Logout' ),
    path( 'language/',     language_view,     name = 'Language' ),
    path( 'notes/',        notes_view,        name = 'Notes' ),
]
