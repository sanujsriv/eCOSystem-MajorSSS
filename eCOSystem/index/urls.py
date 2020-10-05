from django.urls import path

from . import views

app_name='index'
urlpatterns=[
    path('',views.PostListView,name='index'),
    path('post_comments/',views.PostCommentsView, name='PostCommentsView'),
    path('commented/', views.CommentView, name='CommentView'),
    path('deleteCommentView/', views.deleteCommentView, name="deleteCommentView"),
    path('likeView/', views.likeView, name='likeView'),
    path('dislikeView/', views.dislikeView, name='dislikeView'),
    path('deletePostView/', views.deletePostView, name='deletePostView'),
    path('allnotifications/', views.allnotifications, name='allnotifications'),
    path('deletenotification/', views.deletenotification, name='deletenotification'),
    path('logout',views.signout,name='signout'),
    # path('social_logout',views.social_logout,name='social_logout')
    path('set_session_auth', views.set_session_auth, name='set_session_auth'),
    path('set_oauth_user_name', views.set_oauth_user_name, name='set_oauth_user_name'),

]
