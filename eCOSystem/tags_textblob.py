import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eCOSystem.settings')

import django
django.setup()

from textblob import TextBlob as tb
from index.models import Posts
import json
from html2text import html2text
from pymongo import MongoClient
posts = Posts.objects.all()

user_list = []
title_list = []
timestamp_list = []
post_list = []
post_tag_list = []

for post in posts:
    user_list.append(str(post.author))
    title_list.append(str(post.title))
    timestamp_list.append(str(post.created_on))

# for i in range(1, len(posts)+1):
#     post_list.append("post-"+str(i))
dbclient = MongoClient('localhost', 27017)
db = dbclient['eCOSystem']
collection = db['index_posts']

for i in range(len(posts)):
    c = collection.find_one({"author": user_list[i], "title": title_list[i]})
    post_list.append(str(c.get("_id")))


for post in posts:
    post_textblob = tb(str(html2text(post.title)) + " - " + str(html2text(post.text)))
    # print(html2text(post.text))
    tag_list = []
    for t in post_textblob.tags:
        if t[1] == 'NNP':
            tag = ''.join(e for e in t[0] if e.isalnum())
            if tag != '':
                tag_list.append(tag)

    post_tag_list.append(list(set(tag_list)))

# for i in post_tag_list:
#     print(i)


user_post_interactions = []
post_properties = {}
for i in range(len(posts)):
    user_id = user_list[i]
    item_id = post_list[i]
    timestamp = timestamp_list[i]
    user_post_dic = {"user_id":user_id,
                     "item_id":item_id,
                     "timestamp":timestamp
                     }
    user_post_interactions.append(user_post_dic)

    title = title_list[i]
    tags = post_tag_list[i]

    post_dic = {
        "title": title,
        "author":user_id,
        "tags": tags,
        "timestamp":timestamp,
    }
    post_properties[item_id] = post_dic

print(user_post_interactions)
print()
print()
print()
print(post_properties)

upi= open('user_post_interactions.json',"a")
string_upi=str(user_post_interactions)
string_upi=string_upi.replace("\'","\"")
parsed_upi = json.loads(string_upi)
string_upi_indent=json.dumps(parsed_upi, indent=2, sort_keys=True)
upi.write(string_upi_indent)
upi.close()

pp= open('post_properties.json',"a")
string_pp=str(post_properties)
string_pp=string_pp.replace("\'","\"")
parsed_pp= json.loads(string_pp)
string_pp_indent=json.dumps(parsed_pp, indent=2, sort_keys=True)
pp.write(string_pp_indent)
pp.close()
