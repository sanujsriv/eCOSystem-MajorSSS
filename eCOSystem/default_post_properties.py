import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eCOSystem.settings')

import django
django.setup()

from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import *
from django.utils import timezone

client=RecombeeClient('sa-games-post','YQdgn1kUr1c8jFuYaL3WXth8FQO7HI23ugQ92jUtKGjm8JiKntxvSFEloshzU0CJ')
# client.send(AddItem("5cf02380063c452270540057"))
# client.send(AddItemProperty('title','string'))
# client.send(AddItemProperty('author','string'))
# client.send(AddItemProperty('tags','set'))
# client.send(AddItemProperty('timestamp','timestamp'))

# interaction = {
#         "5cf02380063c452270540057" : {
#                         "author" : "sanujsriv@gmail.com" ,
#                         "tags" : [],
#                         "timestamp": str(timezone.now()),
#                         "title": "Default Post"
#                 }
#         }
#
# for item_id, values in interaction.items():
#     q = SetItemValues(item_id,
#                       values,
#                       cascade_create=True)
# client.send(q)
client.send(DeleteItem("5cefb4ec063c450484247e7e"))
# client.send(DeleteUser("skymishramsk@gmail.com")

