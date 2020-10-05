from django.urls import path
from . import views



app_name='my_profile_feed'

urlpatterns = [
   path('', views.my_profile_feed, name='my_profile_feed'),
   path('customViewProfile/', views.customViewProfile, name="customViewProfile"),
   path('deleteDetailsView/', views.deleteDetailsView, name="deleteDetailsView"),
   path('chatView/', views.chatView, name="chatView"),
   path('showchats/', views.showchats, name="showchats"),
   path('sendChats/', views.sendChats, name="sendChats"),
]
