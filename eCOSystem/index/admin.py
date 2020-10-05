from django.contrib import admin
from .models import Posts, Comment


admin.site.register([Posts, Comment])
