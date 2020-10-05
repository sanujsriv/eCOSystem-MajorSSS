from django.urls import include,path

from django.contrib.auth import views as auth_views
from . import views

app_name='signin'

urlpatterns = [

    path('signup', views.signup, name='signup'),
    # path('oauth', include('social_django.urls',namespace='social')),
    path('',views.signin,name='signin'),
    path('signin_auth', views.signin_auth, name='signin_auth'),

    ]
