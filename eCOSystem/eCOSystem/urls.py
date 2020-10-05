from django.contrib import admin
from django.urls import include,path
from django.conf.urls.static import static
from . import settings
from signin import views as views_signin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/', include('signin.urls'),name='signin'),
    path('oauth/', include('social_django.urls',namespace='social')),
    path('index/', include('index.urls'), name='index'),
    path('profiles/', include('profiles.urls'),name='profiles'),
    path('my_profile_feed/', include('my_profile_feed.urls'),name='my_profile_feed'),
    path('', include('django.contrib.auth.urls')),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('signin_auth/', views_signin.signin_auth, name='signin_auth'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
