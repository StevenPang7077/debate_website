"""Debate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from database import views

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('leaderboard/', views.leaderboard, name = 'leaderboard'),
    path('student/<int:pk>', views.student_detail_view, name='student-detail'),
    path('performance/<int:pk>', views.performance_detail_view, name='performance-detail'),
    path('students', views.student_list, name='students'),
    path('tournament/<int:pk>', views.tournament_detail_view, name='tournament-detail'),
    path('tournaments', views.tournament_list, name='tournaments'),
]