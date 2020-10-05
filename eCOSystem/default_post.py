import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eCOSystem.settings')

import django
django.setup()

from index.models import Posts
from django.utils import timezone

admin_author='admin1'
admin_author_name='sanujsriv@gmail.com'
Posts(author=admin_author,author_name=admin_author_name,title='Default Post',text='Hi! Welcome to eCOSystem!',created_on=timezone.now(), comments_count=0, comments=[],
            likes_count=0, likes=[]).save()

