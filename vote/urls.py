"""vote URL Configuration

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

from song import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.VoteList.as_view(), name='vote_list'),
    path('add_song/', views.AddSong.as_view(), name='add_song'),
    path('vote_song/', views.VoteSong.as_view(), name='vote_song'),
    path('covered_song/', views.CoveredSong.as_view(), name='covered_song'),
]
