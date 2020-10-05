from django.urls import path

from . import views

app_name='profiles'

urlpatterns = [
    path('',views.profileView, name='profiles'),
    path('followingview/',views.FollowingView, name='FollowingView'),
    path('followersview/', views.FollowersView, name='FollowersView'),
    ]
