from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.shortcuts import render

from .models import Follow, Following, Follower
from my_profile_feed.models import user_profile, FollowNotification
from django.utils import timezone


profiles = user_profile.objects.all()
def profileView(request):
    if request.session.has_key('username'):
        username = request.session['username']
        user_name = user_profile.objects.get(user_email=username).user_name
        user_img = user_profile.objects.get(user_email=username).user_image
        # profiles = user_profile.objects.all()
        current_user_followings = []
        if request.method == "POST":
            # follow_registered = False
            following_name = request.POST.get("follow_name")
            following_email = request.POST.get("follow_email")


            #FOLLOW LOGIC HERE
            username = request.session['username']
            follower_list = []
            following_list = []
            if Follow.objects.filter(user_name=username).exists():
                follow_details1 = Follow.objects.get(user_name = username)

                for i in follow_details1.follower:
                    follower_list.append(Follower(name=i.name, email=i.email))
                for i in follow_details1.following:
                    following_list.append(Following(name=i.name, email=i.email))

            following_list.append(Following(name=following_name, email=following_email))
            following_update_details = {'user_name':username, 'follower':follower_list, 'following':following_list}
            Follow.objects.update_or_create(user_name=username, defaults=following_update_details)
            current_user_followings = following_list

            follower_list = []
            following_list = []
            if Follow.objects.filter(user_name=following_email).exists():
                follow_details2 = Follow.objects.get(user_name = following_email)
                for i in follow_details2.follower:
                    follower_list.append(Follower(name=i.name, email=i.email))
                for i in follow_details2.following:
                    following_list.append(Following(name=i.name, email=i.email))
            follower_name = user_profile.objects.get(user_email=username).user_name
            follower_list.append(Follower(name=follower_name, email=username))
            follower_update_details = {'user_name':following_email, 'follower':follower_list, 'following':following_list}
            Follow.objects.update_or_create(user_name=following_email, defaults=follower_update_details)
            # follow_details.

            user_details = user_profile.objects.get(user_email=following_email)
            notification_list = user_details.follow_notification
            noti_msg = str(user_name) + "(@" + str(username) + ") has followed you..."
            notification_list.append(FollowNotification(author=username, text=noti_msg, created_on=timezone.now()))
            user_updates = {'user_name': user_details.user_name, 'user_email': user_details.user_email,
                            'overview': user_details.overview,
                            'experience': user_details.experience, 'address': user_details.address,
                            'skills': user_details.skills, 'interests': user_details.interests,
                            'education_details': user_details.education_details,
                            'certifications': user_details.certifications, 'notification': user_details.notification, 'follow_notification': notification_list,
                            'chats': user_details.chats}
            user_profile.objects.update_or_create(user_email=user_details.user_email, defaults=user_updates)

        current_user_follow_details = Follow.objects.get(user_name = username)
        for i in current_user_follow_details.following:
            current_user_followings.append(i.email)

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
        return render(request, "profiles.html", {'profiles':profiles, 'username':username, 'user_name':user_name, 'user_img': user_img, 'current_user_followings':current_user_followings, 'notifications':notifications, 'chats':chats})
    else:
        return HttpResponseRedirect(reverse_lazy('signin:signin'))



def FollowingView(request):
    if request.session.has_key('username'):
        username = request.session['username']
        user_name = user_profile.objects.get(user_email=username).user_name
        user_img = user_profile.objects.get(user_email=username).user_image
        if request.method == "POST":
            if request.POST.get("follow_button") == "Follow":
                profileView(request)
            elif request.POST.get("follow_button") == "Unfollow":
                #UNFOLLOW LOGIC HERE
                following_name = request.POST.get("follow_name")
                following_email = request.POST.get("follow_email")

                follows1 = Follow.objects.get(user_name = username)
                followings = []
                followers = []
                for f in follows1.following:
                    if f.email == following_email:
                        pass
                    else:
                        followings.append(Following(name=f.name, email=f.email))
                for f in follows1.follower:
                    followers.append(Follower(name=f.name, email=f.email))
                follow_update_details1 = {'user_name':username, 'follower':followers, 'following':followings}
                Follow.objects.update_or_create(user_name=username, defaults=follow_update_details1)

                follows2 = Follow.objects.get(user_name = following_email)
                followings = []
                followers = []
                for f in follows2.following:
                    followings.append(Following(name=f.name, email=f.email))
                for f in follows2.follower:
                    if f.email == username:
                        pass
                    else:
                        followers.append(Follower(name=f.name, email=f.email))
                follow_update_details2 = {'user_name':following_email, 'follower':followers, 'following':followings}
                Follow.objects.update_or_create(user_name=following_email, defaults=follow_update_details2)

        current_user_follow_details = Follow.objects.get(user_name = username)
        current_user_followings = []
        for i in current_user_follow_details.following:
            current_user_followings.append(i.email)

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
        return render(request, "following.html", {'profiles':profiles, 'username':username, 'user_name':user_name, "user_img":user_img, 'current_user_followings':current_user_followings, 'notifications':notifications, 'chats':chats})
    else:
        return HttpResponseRedirect(reverse_lazy('signin:signin'))

def FollowersView(request):
    if request.session.has_key('username'):
        username = request.session['username']
        user_name = user_profile.objects.get(user_email=username).user_name
        user_img = user_profile.objects.get(user_email=username).user_image
        current_user_follow_details = Follow.objects.get(user_name = username)
        current_user_followers = []
        for i in current_user_follow_details.follower:
            current_user_followers.append(i.email)

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
        return render(request, "followers.html", {'profiles':profiles, 'username':username, 'user_name':user_name,'user_img':user_img, 'current_user_followers':current_user_followers,'notifications':notifications, 'chats': chats})
    else:
        return HttpResponseRedirect(reverse_lazy('signin:signin'))
