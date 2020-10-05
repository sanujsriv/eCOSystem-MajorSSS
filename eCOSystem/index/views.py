from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from eCOSystem import settings
from django.contrib.auth import logout as auth_logout
from social_django.models import UserSocialAuth
from django.contrib.auth.decorators import login_required
from django.urls import reverse,reverse_lazy
from django.db.models import Q
from pymongo import MongoClient
from bson.objectid import ObjectId
dbclient = MongoClient('localhost', 27017)
db = dbclient['eCOSystem']
collection = db['index_posts']

from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import *

client=RecombeeClient('sa-games-post','YQdgn1kUr1c8jFuYaL3WXth8FQO7HI23ugQ92jUtKGjm8JiKntxvSFEloshzU0CJ')

from textblob import TextBlob as tb
import json
from html2text import html2text

from profiles.models import Follow, Follower
from signin.models import signup_model
from my_profile_feed.models import user_profile, Notification,Address
from .models import Posts, Comment, Like
from .forms import CommentForm
from django.utils import timezone
from . import views

# #########################################

### Social Auth#######


all_profiles=user_profile.objects.all()
all_profile_names = [[p.user_email, p.user_name] for p in all_profiles]
user_follower_counts = []
for profile in all_profiles:
    current_user_follower_list = Follow.objects.get(user_name=profile.user_email).follower
    user_follower_counts.append(len(current_user_follower_list))

zipped_pairs = zip(user_follower_counts, all_profile_names)
z = [x for _, x in sorted(zipped_pairs)]
top_profiles = [Follower(email=i[0], name=i[1]) for i in z]
top_profiles.reverse()
top_profiles = top_profiles[0:5]
print('WWWWWWW')
print(top_profiles)
print('WWWWWWW')

count=5
def pagination(postlist):
    global count
    count=count+5
    if count > len(postlist):
        count=len(postlist)
        final_post=postlist[0:count]
    else:
        final_post=postlist[0:count]
    return final_post

def set_oauth_user_name(request):
    if request.method=='POST':
        oauth_user_name=request.POST.get('oauth_user_name')
        if(oauth_user_name):
            username=request.session['username']
            user_profile(user_name=oauth_user_name,user_email=username,overview="",
                    experience=[],
                    address=Address(locality="", city="", zip="", country=""),
                    skills=[],
                    interests=[],
                    education_details=[],
                    certifications=[],
                    notification = [],
                    follow_notification = [],
                    chats = []).save()
            Follow(user_name=username, follower=[], following=[]).save()

            r = AddDetailView(
                user_id=username,
                item_id="5cf02380063c452270540057",
                timestamp=str(timezone.now()),
                cascade_create=True
            )
            client.send(r)
            request.method=None
            return HttpResponseRedirect(reverse('index:index'))
    return HttpResponseRedirect(request.path_info)


def set_session_auth(request):
    if request.method=='POST':
        uname_auth=request.POST.get('auth_uid')
        if(uname_auth):
           print(uname_auth)
           request.session['username'] = uname_auth
           if (user_profile.objects.filter(user_email=uname_auth).exists()):
              request.method=None
              return PostListView(request)
           else:
               return render(request,'set_username_auth.html')

    return HttpResponseRedirect(reverse('signin:signin'))

###############

#############################################
def makecurrentjson(post, username, created_on):
    post_textblob = tb(str(html2text(post.title)) + " - " + str(html2text(post.text)))

    tag_list = []
    for t in post_textblob.tags:
        if t[1] == 'NNP':
            tag = ''.join(e for e in t[0] if e.isalnum())
            if tag != '':
                tag_list.append(tag)

    # user_post_interactions = []
    post_properties = {}

    c = collection.find_one({"author": username, "created_on": created_on})

    user_id = username
    item_id = str(c.get("_id"))
    timestamp = str(created_on)
    # user_post_dic = {"user_id":user_id,
    #                  "item_id":item_id,
    #                  "timestamp":timestamp
    #                  }
    user_post_interactions = {"user_id":user_id,
                     "item_id":item_id,
                     "timestamp":timestamp
                     }
    # user_post_interactions.append(user_post_dic)

    title = post.title
    tags = tag_list

    post_dic = {
        "title": title,
        "author":user_id,
        "tags": tags,
        "timestamp":timestamp,
    }

    post_properties[item_id] = post_dic

    cupi= open('current_user_post_interactions.json',"w")
    string_upi=str(user_post_interactions)
    string_upi=string_upi.replace("\'","\"")
    parsed_upi = json.loads(string_upi)
    string_upi_indent=json.dumps(parsed_upi, indent=2, sort_keys=True)
    cupi.write(string_upi_indent)
    cupi.close()

    cpp= open('current_post_properties.json',"w")
    string_pp=str(post_properties)
    string_pp=string_pp.replace("\'","\"")
    parsed_pp= json.loads(string_pp)
    string_pp_indent=json.dumps(parsed_pp, indent=2, sort_keys=True)
    cpp.write(string_pp_indent)
    cpp.close()

    # requests = []

    with open('current_user_post_interactions.json') as upi:
        interaction = json.loads(upi.read())

        r = AddDetailView(
                user_id=interaction["user_id"],
                item_id=interaction["item_id"],
                timestamp=interaction["timestamp"],
                cascade_create=True
            )

        r.timeout = 10000
        client.send(r)
    upi.close()

    with open('current_post_properties.json') as pp:
        interactions = json.loads(pp.read())
        for item_id,values in interactions.items():
            q = SetItemValues(item_id,
                              values,
                              cascade_create=True)
            client.send(q)



def PostListView(request):
    if request.session.has_key('username'):

        username = request.session['username']

        user_img = user_profile.objects.get(user_email=username).user_image
        user_name = user_profile.objects.get(user_email=username).user_name



        recommendation=client.send(RecommendItemsToUser(username, 10))

        recommended_profiles=client.send(RecommendUsersToUser(username,5,return_properties=True))
        # filter = "'city' == \"New York\" AND 'date' >= now() AND \"ballet\" in 'genres'"
        # interests_objects_list = user_profile.objects.get(user_email=username).interests
        # interests_list = [str(i.interest_name) for i in interests_objects_list]
        # filter_interest_str = ""
        # for i in range(len(interests_list)-1):
        #     filter_interest_str += '\"'+interests_list[i]+'\"'+ " in 'tags' OR "
        # filter_interest_str += '\"'+interests_list[:-1]+'\"'+ " in 'tags'"


        print()
        print()
        print(recommended_profiles)

        rec_profiles_list = []

        user_followings = Follow.objects.get(user_name = username).following
        user_followings_list = [a.email for a in user_followings]
        for rp in recommended_profiles['recomms']:
            rec_email = rp['id']
            print(rec_email)
            print()
            print()
            rec_name =  user_profile.objects.get(user_email=rec_email).user_name
            if rec_email not in user_followings_list:
                rec_profiles_list.append(Follower(name=rec_name, email=rec_email))

        if request.method == "POST" and request.POST.get("load_more") != "load_more":
            # post = PostForm(request.POST)

            data_created_on = timezone.now()
            # if post.is_valid():
            data_author = username
                # author_name = profiles.objects.get(email = username).full_name
            data_author_name = user_name
            data_title = request.POST.get('title')
            data_text = request.POST.get('text')
                # data_created_on = timezone.now()

                # post_list = []
                # if Post_Model.objects.filter(author = username).exists():
                #     post_details = Post_Model.objects.get(author = username)
                #
                #     for i in post_details.post:
                #         post_list.append(Post(title=i.title, text=i.text, created_on=i.created_on, comments=i.comments))
            post = Posts(author=data_author, author_name=data_author_name, title=data_title, text=data_text, created_on=data_created_on, comments_count=0, comments=[], likes_count=0, likes=[])
            post.save()
            makecurrentjson(post, username, data_created_on)

            followers_email_list = []

            for e in Follow.objects.get(user_name=username).follower:
                followers_email_list.append(e.email)

            user_details = []
            user_details = user_profile.objects.filter(user_email__in=followers_email_list)


            for ud in user_details:
                postnotification_list = ud.notification
                postnoti_msg = str(user_name) + "(@" + str(username) + ") has posted new story..." + "TITLE: " + str(
                    data_title)
                postnotification_list.append(
                    Notification(post_title=data_title, post_author=data_author, author=username, text=postnoti_msg, created_on=timezone.now()))
                user_updates = {'user_name': ud.user_name, 'user_email': ud.user_email,
                                'overview': ud.overview,
                                'experience': ud.experience, 'address': ud.address,
                                'skills': ud.skills, 'interests': ud.interests,
                                'education_details': ud.education_details,
                                'certifications': ud.certifications, 'notification': postnotification_list, 'follow_notification': ud.follow_notification,
                                'chats': ud.chats}
                user_profile.objects.update_or_create(user_email=ud.user_email, defaults=user_updates)

            return HttpResponseRedirect(request.path_info)
                # updated_posts = {'author': data_author, 'author_name': data_author_name, 'post':post_list}
                # Post_Model.objects.update_or_create(author=username, defaults=updated_posts)
        # return render(request, "index.html", {'post':'post', 'postlist':'postlist'})

        ###-----

        # postlist = Posts.objects.filter(created_on__lte=timezone.now()).order_by('-created_on')
        # user_followings = Follow.objects.get(user_name = username).following
        # user_followings_list = [a.email for a in user_followings]
        universal_postlist = Posts.objects.all()
        user_followings_list.append(username)
        all_postlist = []
        all_postlist = universal_postlist.filter(author__in = user_followings_list)

        # recomm_post_id_list = [collection.find_one({"_id": ObjectId(str(r['id']))}) for r in recommendation['recomms']]
        # print(recomm_post_id_list[0])

        #######################################
        ####################################

        recomm_post_object_list = []
        for recom in recommendation['recomms']:
           for reco in recom:
            r=recom[reco]
            if str(r) == "5cf02380063c452270540057":
                pass
            elif collection.find_one({"_id": ObjectId(str(r))}):
                c = collection.find_one({"_id": ObjectId(str(r))})
                recomm_post_object_list.append(universal_postlist.filter(author=str(c.get("author")), title=str(c.get("title")))[0])
        print(recomm_post_object_list)


        postlist = [p for p in all_postlist]
        recomm_post_list = [r for r in recomm_post_object_list]



        postlist.extend(recomm_post_list)
        postlist = list(set(postlist))
        print()
        print()
        print("Final post list")

        post_timestamp_list = [p.created_on for p in postlist]
        zipped_pairs = zip(post_timestamp_list, postlist)
        z = [x for _, x in sorted(zipped_pairs)]
        postlist = z
        postlist.reverse()
        postlist = postlist[:9]
        # postlist = Posts.objects.filter(created_on__lte=timezone.now()).order_by('-created_on')

        universal_likes_list = []

        for post in postlist:
            likes_list = []
            for l in post.likes:
                likes_list.append(l.user_email)
            universal_likes_list.append(likes_list)
        for i in range(len(postlist)):
            postlist[i].likes = universal_likes_list[i]




        profiles = []
        query = request.GET.get("q")
        search_type = request.GET.get("search_type")
        if search_type == "By Profiles":
            profiles_list = user_profile.objects.all()
            if query:
                postlist = []
                profiles = []

                for pro in profiles_list:
                    if query.upper() in pro.user_name.upper():
                        profiles.append(pro)
                    elif query.upper() in pro.user_email.upper():
                        profiles.append(pro)
                    for p in pro.skills:
                        if query.upper() in p.skill_name.upper():
                            profiles.append(pro)
                            break
                    for p in pro.interests:
                        if query.upper() in p.interest_name.upper():
                            profiles.append(pro)
                            break
                profiles = list(set(profiles))

        elif search_type == "By Posts":
            if query:
                profiles = []
                postlist = universal_postlist.filter(
                                    Q(title__icontains=query) |
                                    Q(text__icontains=query) |
                                    Q(author__icontains=query) |
                                    Q(author_name__icontains=query)
                                    )

        if Follow.objects.filter(user_name=username).exists():
            nfollower = len(Follow.objects.get(user_name=username).follower)
            nfollowing = len(Follow.objects.get(user_name=username).following)
            print(request.session['username'])
        else:
            nfollower = 0
            nfollowing = 0

        if user_profile.objects.filter(user_email=username).exists():
            # latest 5 notifications
            notifications = user_profile.objects.get(user_email=username).notification[-5:] + user_profile.objects.get(user_email=username).follow_notification[-5:]
            notifications_timestamp = [n.created_on for n in notifications]
            zipped_pairs = zip(notifications_timestamp, notifications)
            z = [x for _, x in sorted(zipped_pairs)]
            notifications = z[-5:]

            chats_list = user_profile.objects.get(user_email=username).chats
            chats_list.reverse()
            chats = []
            chats_count = 0
            for c in chats_list:
                if chats_count < 5:
                    if c.sender_email != username:
                        chats.append(c)
                        chats_count += 1
                else:
                    break
        else:
            notifications = []
            chats = []

        all_profiles = user_profile.objects.all()
        current_user_follow_details = Follow.objects.get(user_name=username)
        current_user_followings = []
        for i in current_user_follow_details.following:
            current_user_followings.append(i.email)

        print()
        print()
        print(len(postlist))
        if (request.method == 'POST' and request.POST.get('load_more') == 'load_more'):
            final_postlist = pagination(postlist)
        else:
            global count
            final_postlist = postlist[0:count]
        return render(request,'index.html',{'user_img':user_img,'postlist':final_postlist, 'profiles':profiles, 'top_profiles':top_profiles,'all_profiles':all_profiles, 'current_user_followings':current_user_followings, 'follower':nfollower,'following':nfollowing, 'username':username, 'user_name':user_name, 'notifications':notifications, 'chats': chats, 'rec_profiles_list':rec_profiles_list})

    else:
        return HttpResponseRedirect(reverse_lazy('signin:signin'))

def deletePostView(request):
    if request.session.has_key('username'):
        username = request.session['username']
        post_author = request.GET.get('author')
        post_title = request.GET.get('title')

        posts = Posts.objects.all()

        c = collection.find_one({"author": username, "title": post_title})
        client.send(DeleteDetailView(username, str(c.get("_id"))))
        client.send(DeleteItem(str(c.get("_id"))))
        Posts.objects.filter(title=post_title, author=post_author).delete()

        return PostListView(request)

    else:
        return HttpResponseRedirect(reverse_lazy('signin:signin'))


###########################################

def allnotifications(request):
    if request.session.has_key('username'):
        username = request.session['username']
        user_img = user_profile.objects.get(user_email=username).user_image
        user_name = user_profile.objects.get(user_email=username).user_name
        if Follow.objects.filter(user_name=username).exists():
            nfollower = len(Follow.objects.get(user_name=username).follower)
            nfollowing = len(Follow.objects.get(user_name=username).following)
            print(request.session['username'])
        else:
            nfollower = 0
            nfollowing = 0
        # all notifications
        notifications = user_profile.objects.get(user_email=username).notification + user_profile.objects.get(user_email=username).follow_notification
        notifications_timestamp = [n.created_on for n in notifications]
        zipped_pairs = zip(notifications_timestamp, notifications)
        z = [x for _, x in sorted(zipped_pairs)]
        notifications = z[-5:]
        allnotifications = z
        allnotifications.reverse()
        return render(request, "allnotifications.html", {'user_img':user_img,'allnotifications':allnotifications, 'notifications':notifications, 'follower':nfollower,'following':nfollowing, 'username':username, 'user_name':user_name})
    else:
        return HttpResponseRedirect(reverse_lazy('signin:signin'))

def deletenotification(request):
    if request.session.has_key('username'):

        username = request.session['username']
        user_img = user_profile.objects.get(user_email=username).user_image
        if request.method == 'POST':
            # noti_post_title = request.POST.get('noti_post_title')
            # noti_post_author = request.POST.get('noti_post_author')
            noti_author = request.POST.get('noti_author')
            noti_text = request.POST.get('noti_text')
            noti_created_on = request.POST.get('noti_created_on')
            noti_index = request.POST.get('noti_index')

            user_details = user_profile.objects.get(user_email=username)

            all_notification_list = user_details.notification + user_details.follow_notification
            notifications_timestamp = [n.created_on for n in all_notification_list]
            zipped_pairs = zip(notifications_timestamp, all_notification_list)
            z = [x for _, x in sorted(zipped_pairs)]
            z.reverse()
            all_notification_list = z

            all_notification_list.remove(all_notification_list[int(noti_index) - 1])

            notification_list = []
            follow_notification_list = []

            for n in all_notification_list:
                if "followed" in n.text:
                    follow_notification_list.append(n)
                else:
                    notification_list.append(n)
            notification_list.reverse()
            follow_notification_list.reverse()

            user_updates = {'user_name': user_details.user_name, 'user_email': user_details.user_email,
                                'overview': user_details.overview,
                                'experience': user_details.experience, 'address': user_details.address,
                                'skills': user_details.skills, 'interests': user_details.interests,
                                'education_details': user_details.education_details,
                                'certifications': user_details.certifications, 'notification': notification_list,
                                'follow_notification': follow_notification_list,
                                'chats': user_details.chats}

            user_profile.objects.update_or_create(user_email=user_details.user_email, defaults=user_updates)

        if Follow.objects.filter(user_name=username).exists():
            nfollower = len(Follow.objects.get(user_name=username).follower)
            nfollowing = len(Follow.objects.get(user_name=username).following)
            print(request.session['username'])
        else:
            nfollower = 0
            nfollowing = 0

        # all notifications
        notifications = user_profile.objects.get(user_email=username).notification + user_profile.objects.get(user_email=username).follow_notification
        notifications_timestamp = [n.created_on for n in notifications]
        zipped_pairs = zip(notifications_timestamp, notifications)
        z = [x for _, x in sorted(zipped_pairs)]
        notifications = z[-5:]
        allnotifications = z
        allnotifications.reverse()

        chats_list = user_profile.objects.get(user_email=username).chats
        chats_list.reverse()
        chats = []
        chats_count = 0
        for c in chats_list:
            if chats_count < 5:
                if c.sender_email != username:
                    chats.append(c)
                    chats_count += 1
            else:
                break
        return render(request, "allnotifications.html", {'user_img':user_img,'allnotifications':allnotifications, 'notifications':notifications, 'follower':nfollower,'following':nfollowing, 'username':username, 'chats': chats})
    else:
        return HttpResponseRedirect(reverse_lazy('signin:signin'))


##########################################
# POST_COMMENT_VIEW
global_data_title = ""

def PostCommentsView(request):
    if request.session.has_key('username'):
        username = request.session['username']
        user_img = user_profile.objects.get(user_email=username).user_image
        user_name = user_profile.objects.get(user_email=username).user_name
        comment_form = CommentForm()
        post_title = ""
        if request.method == 'POST':
            post_author = request.POST.get('author')
            post_title = request.POST.get('title')
            # print(post_author)
            # print(post_title)

        elif request.method == 'GET':
            post_author = request.GET.get('author')
            post_title = request.GET.get('title')

        global global_data_title
        global_data_title = post_title
        post_details = Posts.objects.get(title=global_data_title)
        comment_list = []
        if Posts.objects.filter(title=global_data_title).exists():
            post_comment_details = Posts.objects.get(title=global_data_title)
            comment_list = post_comment_details.comments

        if Follow.objects.filter(user_name=username).exists():
            nfollower = len(Follow.objects.get(user_name=username).follower)
            nfollowing = len(Follow.objects.get(user_name=username).following)
            print(request.session['username'])
        else:
            nfollower = 0
            nfollowing = 0
        comment_list.reverse()
        # latest 5 notifications
        notifications = user_profile.objects.get(user_email=username).notification[-5:] + user_profile.objects.get(user_email=username).follow_notification[-5:]
        notifications_timestamp = [n.created_on for n in notifications]
        zipped_pairs = zip(notifications_timestamp, notifications)
        z = [x for _, x in sorted(zipped_pairs)]
        notifications = z[-5:]

        universal_likes_list = []


        likes_list = []
        for l in post_details.likes:
            likes_list.append(l.user_email)

        post_details.likes = likes_list

        chats_list = user_profile.objects.get(user_email=username).chats
        chats_list.reverse()
        chats = []
        chats_count = 0
        for c in chats_list:
            if chats_count < 5:
                if c.sender_email != username:
                    chats.append(c)
                    chats_count += 1
            else:
                break

        return render(request, "post_comments.html", {'user_img':user_img,'post_details':post_details, 'comment_form':comment_form, 'comment_list':comment_list,'following':nfollowing, 'follower':nfollower, 'user_name':user_name, 'username':username, 'notifications':notifications, 'comment_form':CommentForm(), 'chats': chats})
    else:
        return HttpResponseRedirect(reverse_lazy('signin:signin'))


def CommentView(request):
    if request.session.has_key('username'):
        username = request.session['username']
        user_name = user_profile.objects.get(user_email=username).user_name
        user_img = user_profile.objects.get(user_email=username).user_image
        comment_form = CommentForm()
        data_title = global_data_title
        comment_list = []
        if Posts.objects.filter(title=data_title).exists():
            post_details = Posts.objects.get(title = data_title)
            comment_list = post_details.comments

        if request.method == 'POST':
            data_author = user_name
            comment_created_on = timezone.now()
            data_title = request.POST.get('title')
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                data_text = comment_form.cleaned_data['text']
                comment_list.append(Comment(user_name=data_author, user_email=username, text=data_text, created_on=comment_created_on))
            updated_posts = {'author':post_details.author, 'author_name':post_details.author_name, 'title':post_details.title, 'text':post_details.text,
                            'created_on':post_details.created_on, 'comments_count':post_details.comments_count+1, 'comments':comment_list, 'likes_count':post_details.likes_count, 'likes':post_details.likes}
            Posts.objects.update_or_create(title=post_details.title, defaults=updated_posts)
            comment_form = CommentForm()

            # c = collection.find_one({"author": post_details.author, "title": post_details.title})
            # r = AddDetailView(
            #         user_id=username,
            #         item_id=str(c.get("_id")),
            #         cascade_create=True
            #     )
            # client.send(r)

            if username != post_details.author:
                user_details = user_profile.objects.get(user_email = post_details.author)
                commentnotification_list = user_details.notification
                commentnoti_msg = str(user_name) + " has commented on your post..." + "TITLE: " + str(
                    data_title)


                commentnotification_list.append(
                    Notification(post_title=data_title, post_author=username, author=username, text=commentnoti_msg, created_on=timezone.now()))
                user_updates = {'user_name': user_details.user_name, 'user_email': user_details.user_email,
                                'overview': user_details.overview,
                                'experience': user_details.experience, 'address': user_details.address,
                                'skills': user_details.skills, 'interests': user_details.interests,
                                'education_details': user_details.education_details,
                                'certifications': user_details.certifications, 'notification': commentnotification_list,
                                'follow_notification': user_details.follow_notification,
                                'chats': user_details.chats}
                user_profile.objects.update_or_create(user_email=user_details.user_email, defaults=user_updates)

            return HttpResponseRedirect(request.path_info)

        comment_list.reverse()
        if Follow.objects.filter(user_name=username).exists():
            nfollower = len(Follow.objects.get(user_name=username).follower)
            nfollowing = len(Follow.objects.get(user_name=username).following)
            print(request.session['username'])
        else:
            nfollower = 0
            nfollowing = 0

        # latest 5 notifications
        notifications = user_profile.objects.get(user_email=username).notification[-5:] + user_profile.objects.get(user_email=username).follow_notification[-5:]
        notifications_timestamp = [n.created_on for n in notifications]
        zipped_pairs = zip(notifications_timestamp, notifications)
        z = [x for _, x in sorted(zipped_pairs)]
        notifications = z[-5:]

        universal_likes_list = []


        likes_list = []
        for l in post_details.likes:
            likes_list.append(l.user_email)

        post_details.likes = likes_list

        chats_list = user_profile.objects.get(user_email=username).chats
        chats_list.reverse()
        chats = []
        chats_count = 0
        for c in chats_list:
            if chats_count < 5:
                if c.sender_email != username:
                    chats.append(c)
                    chats_count += 1
            else:
                break
        return render(request, "post_comments.html", {'user_img':user_img,'post_details':post_details, 'comment_form':comment_form, 'comment_list':comment_list, 'following':nfollowing, 'follower':nfollower, 'username':username,
                                                      'user_name':user_name, 'notifications':notifications, 'chats':chats})
    else:
        return HttpResponseRedirect(reverse_lazy('signin:signin'))

def deleteCommentView(request):
    if request.session.has_key('username'):
        username = request.session['username']
        post_author = request.GET.get('author')
        post_title = request.GET.get('title')
        comment_author = request.GET.get('comment_author')
        comment_text = request.GET.get('comment_text')
        post_details = Posts.objects.get(title = post_title, author = post_author)
        comment_list = post_details.comments
        for c in comment_list:
            if c.user_email == comment_author and c.text == comment_text:
                comment_list.remove(c)


        updated_posts = {'author':post_details.author, 'author_name':post_details.author_name, 'title':post_details.title, 'text':post_details.text,
                        'created_on':post_details.created_on, 'comments_count':post_details.comments_count-1, 'comments':comment_list, 'likes_count':post_details.likes_count, 'likes':post_details.likes}
        Posts.objects.update_or_create(title=post_title, author=post_author, defaults=updated_posts)
        return CommentView(request)

    else:
        return HttpResponseRedirect(reverse_lazy('signin:signin'))

#########################################

def likeView(request):
    if request.session.has_key('username'):
        username = request.session['username']
        user_img = user_profile.objects.get(user_email=username).user_image
        user_name = user_profile.objects.get(user_email=username).user_name
        post_title = request.GET.get('title')
        post_author = request.GET.get('author')
        post = Posts.objects.get(title=post_title, author=post_author)
        likes_list = post.likes
        likes_email_list = [l.user_email for l in post.likes]
        likes_count = post.likes_count




        if username not in likes_email_list:
            likes_list.append(Like(user_email=username))
            likes_count = likes_count + 1

            updated_post = {'author':post.author,
                            'author_name':post.author_name,
                            'title':post.title,
                            'text':post.text,
                            'created_on':post.created_on,
                            'comments_count':post.comments_count,
                            'comments':post.comments,
                            'likes_count':likes_count,
                            'likes':likes_list,}
            Posts.objects.update_or_create(title=post.title, defaults=updated_post)
            # Posts.objects.filter(title=post_title, author=post_author).update(likes=likes_list)

            c = collection.find_one({"author": post_author, "title": post_title})

            r = AddDetailView(
                    user_id=username,
                    item_id=str(c.get("_id")),
                    timestamp=str(timezone.now()),
                    cascade_create=True

                )
            r.timeout=10000
            client.send(r)

            if username != post_author:
                user_details = user_profile.objects.get(user_email = post_author)
                likenotification_list = user_details.notification
                likenoti_msg = str(user_name) + " has liked your post..." + "TITLE: " + str(
                    post_title)


                likenotification_list.append(
                    Notification(post_title=post_title, post_author=post_author, author=username, text=likenoti_msg, created_on=timezone.now()))
                user_updates = {'user_name': user_details.user_name, 'user_email': user_details.user_email,
                                'overview': user_details.overview,
                                'experience': user_details.experience, 'address': user_details.address,
                                'skills': user_details.skills, 'interests': user_details.interests,
                                'education_details': user_details.education_details,
                                'certifications': user_details.certifications, 'notification': likenotification_list,
                                'follow_notification':user_details.follow_notification,
                                'chats': user_details.chats}
                user_profile.objects.update_or_create(user_email=user_details.user_email, defaults=user_updates)



        return PostListView(request)

    else:
        return HttpResponseRedirect(reverse_lazy('signin:signin'))

def dislikeView(request):
    if request.session.has_key('username'):
        username = request.session['username']
        post_title = request.GET.get('title')
        post_author = request.GET.get('author')
        post = Posts.objects.get(title=post_title, author=post_author)
        likes_list = post.likes
        likes_email_list = [l.user_email for l in post.likes]

        if username in likes_email_list:
            for l in likes_list:
                if l.user_email == username:
                    likes_list.remove(l)



            updated_post = {'author':post.author,
                            'author_name':post.author_name,
                            'title':post.title,
                            'text':post.text,
                            'created_on':post.created_on,
                            'comments_count':post.comments_count,
                            'comments':post.comments,
                            'likes_count':post.likes_count-1,
                            'likes':likes_list,}
            Posts.objects.update_or_create(title=post.title, defaults=updated_post)

        # Posts.objects.filter(title=post_title, author=post_author).update(likes=likes_list)
        return PostListView(request)


    else:
        return HttpResponseRedirect(reverse_lazy('signin:signin'))

#########################################



def social_logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse_lazy('signin:signin'))

def signout(request):

    if request.session.has_key('username'):

        username = request.session['username']
        del request.session['username']
        if UserSocialAuth.objects.filter(uid=str(username)).exists():
            u = UserSocialAuth.objects.filter(uid=str(username)).delete()
            print(u)

    return HttpResponseRedirect(reverse('signin:signin'))
