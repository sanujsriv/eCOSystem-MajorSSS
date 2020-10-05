from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from signin.models import signup_model
from .forms import ExperienceForm, AddressForm, SkillForm, InterestForm, Education_detailsForm, CertificationsForm,ProfilepicForm
from .models import Experience, Address, Skill, Interest, Education_details, Certifications, user_profile, FollowNotification, Notification, Chats
from profiles.models import Follow, Following, Follower
from index.models import Posts
from django.utils import timezone
import datetime
import pytz
# Create your views here.

#FORM OBJECTS
experience_form = ExperienceForm()
address_form = AddressForm()
skill_form = SkillForm()
interest_form = InterestForm()
education_details_form = Education_detailsForm()
certifications_form = CertificationsForm()


#REGISTRATION VARIABLE
exp_registered = False
addr_registered = False
skl_registered = False
intrst_registered = False
edu_registered = False
cert_registered = False
over_registered = False

#OVERVIEW FIELDS DATA VARIABLE
data_overview = ""

#EXPERIENCE FIELDS DATA VARIABLES
data_company = ""
data_title = ""
data_location = ""
data_work_field = ""
data_from_date = None
data_to_date = None
data_descriptionExp = ""

#ADDRESS FIELD DATA VARIABLES
data_locality = ""
data_city = ""
data_zip = ""
data_country = ""

#SKILL FIELD DATA VARIABLES
data_skill_name = ""

#INTEREST FIELD DATA VARIABLES
data_interest_name = ""

#EDUCATION DETAILS FIELD DATA VARIABLES
data_school = ""
data_school_from = None
data_school_to = None
data_degree = ""
data_study_field = ""
data_descriptionEdu = ""

#CERTIFICATION DETAILS FIELD DATA VARIABLES
data_certification_name = ""
data_authority = ""
data_cert_from = None
data_cert_to = None
data_cert_pic = None


# TO CHAT WITH SOME ONE YOU HAVE TO FOLLOW HIM and HE HAS TO FOLLOW YOU BACK...??

chats = []
chat_name = ""
chat_email = ""
chat_image = None

def showchats(request):
    if request.session.has_key('username'):
        username = request.session['username']
        # user_details as ud
        ud = user_profile.objects.get(user_email=username)
        user_name = ud.user_name
        # chats = []
        # chat_name = ""
        # chat_email = ""
        if request.method == "POST":
            global chat_name
            global chat_email
            global chat_image
            chat_name = request.POST.get('chat_name')
            chat_email = request.POST.get('chat_email')
            chat_image=user_profile.objects.get(user_email=chat_email).user_image
            chat_details = []
            for c in ud.chats:
                if c.receiver_email == chat_email:
                    chat_details.append(c)
                elif c.sender_email == chat_email:
                    chat_details.append(c)


            # chat_timestap = [c.created_on for c in chat_details]
            # zipped_pairs = zip(chat_timestap, chat_details)
            # z = [x for _, x in sorted(zipped_pairs)]
            # z.reverse()
            # chats = z
            global chats
            chats = chat_details
        return chatView(request, chat_email, chat_name, chats, chat_image)
    else:
        return HttpResponseRedirect(reverse_lazy('signin:signin'))

def sendChats(request):
    if request.session.has_key('username'):
        username = request.session['username']
        # user_details as ud
        ud = user_profile.objects.get(user_email=username)
        user_name = ud.user_name
        # chats = []
        # chat_name = ""
        # chat_email = ""

        if request.method == "POST":
            recipient_name = request.POST.get('chat_name')
            recipient_email = request.POST.get('chat_email')

            global chat_name
            global chat_email
            global chat_image
            chat_name = recipient_name
            chat_email = recipient_email
            chat_image = user_profile.objects.get(user_email=chat_email).user_image
            message = request.POST.get('message')

            dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
            created_on = dt_utcnow.astimezone(pytz.timezone('Asia/Kolkata'))
            print(created_on)
            print()
            print()
            print()

            # current user's chats list as chats_list1
            chats_list1 = ud.chats
            chats_list1.append(Chats(sender_name=user_name, sender_email=username, receiver_name=recipient_name, receiver_email=recipient_email, message=message, created_on=created_on))

            user_profile.objects.update_or_create(user_email=username , defaults={'chats': chats_list1,})

            # recipient_details as rd
            rd = user_profile.objects.get(user_email=recipient_email)

            # current user's frined's chats list as chats_list2
            chats_list2 = rd.chats
            chats_list2.append(Chats(sender_name=user_name, sender_email=username, receiver_name=recipient_name, receiver_email=recipient_email, message=message, created_on=created_on))

            user_profile.objects.update_or_create(user_email=recipient_email, defaults={'chats': chats_list2,})

            chat_details = []
            for c in ud.chats:
                if c.receiver_email == chat_email:
                    chat_details.append(c)
                elif c.sender_email == chat_email:
                    chat_details.append(c)

            # chat_timestap = [c.created_on for c in chat_details]
            # zipped_pairs = zip(chat_timestap, chat_details)
            # z = [x for _, x in sorted(zipped_pairs)]
            # z.reverse()
            # chats = z
            global chats
            chats = chat_details
            request.method = ""
        return chatView(request, chat_email, chat_name, chats,chat_image)
    else:
        return HttpResponseRedirect(reverse_lazy('signin:signin'))
    pass


def chatView(request, chat_email="", chat_name="", chats=[],chat_image=None):
    if request.session.has_key('username'):
        username = request.session['username']
        user_name = user_profile.objects.get(user_email=username).user_name
        user_img = user_profile.objects.get(user_email=username).user_image
        # follow_details as fd
        fd = Follow.objects.get(user_name=username)
        # user_details as ud
        ud = user_profile.objects.all()
        following_list = [f.email for f in fd.following]
        follower_list = [f.email for f in fd.follower]
        chats_list = []
        for f in following_list:
            if f in follower_list:
                chats_list.append(ud.filter(user_email=f)[0])
        return render(request, "chat.html", {'chat_image':chat_image,'user_img':user_img,'username':username, 'user_name':user_name, 'chats_list':chats_list, 'chat_email':chat_email, 'chat_name':chat_name, 'chats':chats})
    else:
        return HttpResponseRedirect(reverse_lazy('signin:signin'))

def my_profile_feed(request):
    if request.session.has_key('username'):
        global over_registered
        global exp_registered
        global addr_registered
        global skl_registered
        global intrst_registered
        global edu_registered
        global cert_registered
        over_registered = False
        exp_registered = False
        addr_registered = False
        skl_registered = False
        intrst_registered = False
        edu_registered = False
        cert_registered = False
        username = request.session['username']
        user_name = user_profile.objects.get(user_email=username).user_name
        profile_details = user_profile.objects.get(user_email = username)
        user_img = user_profile.objects.get(user_email=username).user_image

        overview = profile_details.overview
        experience_list = []
        address = profile_details.address
        skill_list = []
        interest_list = []
        edu_details_list = []
        cert_list = []
        experience_list = profile_details.experience
        experience_list.reverse()
        skill_list = profile_details.skills
        skill_list.reverse()
        interest_list = profile_details.interests
        interest_list.reverse()
        edu_details_list = profile_details.education_details
        edu_details_list.reverse()
        cert_list = profile_details.certifications
        cert_list.reverse()

        experience_form = ExperienceForm()
        address_form = AddressForm()
        skill_form = SkillForm()
        interest_form = InterestForm()
        education_details_form = Education_detailsForm()
        certifications_form = CertificationsForm()
        profilepic= ProfilepicForm()
        if request.method == 'POST':
            file = request.POST.get('image_upload')

            if file == 'image_up':
                profilepic = ProfilepicForm(request.POST, request.FILES)
                if profilepic.is_valid():
                    if 'user_image' in request.FILES:
                        user_image = request.FILES['user_image']

                        user_details = user_profile.objects.get(user_email=username)
                        updated_details = {'user_name': user_details.user_name,
                                           'user_email': user_details.user_email,
                                           'overview': user_details.overview,
                                           'user_image': user_image,
                                           'experience': user_details.experience,
                                           'address': user_details.address,
                                           'education_details': user_details.education_details,
                                           'skills': user_details.skills,
                                           'interests': user_details.interests,
                                           'certifications': user_details.certifications
                                           }
                        user_profile.objects.update_or_create(user_email=username, defaults=updated_details)
                    return HttpResponseRedirect(request.path_info)
            # print("O: "+request.POST.get("save_overview"))
            if request.POST.get('save_overview') == "Save":
                print("OVERVIEW: "+request.POST.get('save_overview'))
                overview = request.POST.get('overview')
            if request.POST.get("save_experience") == "Save":
                print("EXPERIENCE: "+request.POST.get("save_experience"))

                data_company = request.POST.get("company")
                data_title = request.POST.get("title")
                data_location = request.POST.get("location")
                data_work_field = request.POST.get("work_field")
                data_from_date = request.POST.get("from_date")
                data_to_date = request.POST.get("to_date")
                data_descriptionExp = request.POST.get("descriptionExp")

                experience_list.append(Experience(company=data_company, title = data_title, location=data_location, work_field=data_work_field,
                                                        from_date=data_from_date, to_date=data_to_date, descriptionExp=data_descriptionExp))
            if request.POST.get("save_edu_details") == "Save":
                print("EDUCATION: "+request.POST.get("save_edu_details"))
                education_details_form = Education_detailsForm(request.POST)
                if education_details_form.is_valid():
                    data_school = education_details_form.cleaned_data['school']
                    data_school_from = education_details_form.cleaned_data['school_from']
                    data_school_to = education_details_form.cleaned_data['school_to']
                    data_degree = education_details_form.cleaned_data['degree']
                    data_study_field = education_details_form.cleaned_data['study_field']
                    data_descriptionEdu = education_details_form.cleaned_data['descriptionEdu']
                    edu_details_list.append(Education_details(school=data_school, school_from=data_school_from, school_to=data_school_to, degree=data_degree,
                                                                study_field=data_study_field, descriptionEdu=data_descriptionEdu))

            if request.POST.get("save_address") == "Save":
                print("ADDRESS: "+request.POST.get("save_address"))
                address_form = AddressForm(request.POST)
                if address_form.is_valid():
                    data_locality = address_form.cleaned_data['locality']
                    data_city = address_form.cleaned_data['city']
                    data_zip = address_form.cleaned_data['zip']
                    data_state = address_form.cleaned_data['state']
                    data_country = address_form.cleaned_data['country']
                    address = Address(locality=data_locality, city=data_city, zip=data_zip, state=data_state, country=data_country)

            if request.POST.get("save_interest") == "Save":
                print("INTEREST: "+request.POST.get("save_interest"))
                interest_form = InterestForm(request.POST)
                if interest_form.is_valid():
                    data_interest_name = interest_form.cleaned_data['interest_name']
                    interest_list.append(Interest(interest_name=data_interest_name))

            if request.POST.get("save_cert_details") == "Save":
                print("CERTIFICATION: "+request.POST.get("save_cert_details"))
                certifications_form = CertificationsForm(request.POST)
                if certifications_form.is_valid():
                    data_certification_name = certifications_form.cleaned_data['certification_name']
                    data_authority = certifications_form.cleaned_data['authority']
                    data_cert_from = certifications_form.cleaned_data['cert_from']
                    data_cert_to = certifications_form.cleaned_data['cert_to']
                    data_cert_pic = certifications_form.cleaned_data['cert_pic']
                    cert_list.append(Certifications(certification_name=data_certification_name, authority=data_authority, cert_from=data_cert_from,
                                                    cert_to=data_cert_to, cert_pic=data_cert_pic))

            if request.POST.get("save_skill") == "Save":
                print("SKILL: "+request.POST.get("save_skill"))
                skill_form = SkillForm(request.POST)
                if skill_form.is_valid():
                    data_skill_name = skill_form.cleaned_data['skill_name']
                    skill_list.append(Skill(skill_name=data_skill_name))

            updated_details = {'user_name':user_name, 'user_email':username, 'overview':overview, 'experience':experience_list,
                                    'address':address, 'skills':skill_list, 'interests':interest_list,
                                    'education_details':edu_details_list, 'certifications':cert_list}
            user_profile.objects.update_or_create(user_email=username, defaults=updated_details)
        profile_details = user_profile.objects.get(user_email = username)
        if Follow.objects.filter(user_name=username).exists():
            nfollower = len(Follow.objects.get(user_name=username).follower)
            nfollowing = len(Follow.objects.get(user_name=username).following)
        else:
            nfollower = 0
            nfollowing = 0
        count = 0
        postlist = []
        postlist = Posts.objects.filter(author=username, created_on__lte=timezone.now()).order_by('-created_on')

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
        return render(request, "my_profile_feed.html", {'profilepic': profilepic,'user_img':user_img,'user_name': user_name, 'username': username, 'postlist':postlist, 'experience_form':experience_form, 'address_form':address_form, 'skill_form':skill_form,
                                                        'interest_form':interest_form, 'education_details_form':education_details_form, 'certifications_form':certifications_form,
                                                        'profile_details':profile_details, 'experience_list':experience_list, 'skill_list':skill_list, 'interest_list':interest_list,
                                                         'edu_details_list':edu_details_list, 'cert_list':cert_list, 'follower':nfollower,'following':nfollowing, 'notifications':notifications, 'chats':chats})
    else:
        return HttpResponseRedirect(reverse_lazy('signin:signin'))

def deleteDetailsView(request):
    if request.session.has_key('username'):
        username = request.session['username']
        user_details = user_profile.objects.get(user_email = username)
        overview = user_details.overview
        experience = user_details.experience
        address = user_details.address
        skills = user_details.skills
        interests = user_details.interests
        education_details = user_details.education_details
        certifications = user_details.certifications
        notification = user_details.notification


        if request.GET.get('exp-delete') == 'delete':
            index = request.GET.get('counter')
            experience.remove(experience[int(index)-1])

        if request.GET.get('addr-delete') == 'delete':
            address = Address()

        if request.GET.get('edu-delete') == 'delete':
            index = request.GET.get('counter')
            education_details.remove(education_details[int(index)-1])

        if request.GET.get('cert-delete') == 'delete':
            index = request.GET.get('counter')
            certifications.remove(certifications[int(index)-1])

        if request.GET.get('skill-delete') == 'delete':
            index = request.GET.get('counter')
            skills.remove(skills[int(index)-1])

        if request.GET.get('interest-delete') == 'delete':
            index = request.GET.get('counter')
            interests.remove(interests[int(index)-1])

        updated_details = {
                        'user_name': user_details.user_name,
                        'user_email': user_details.user_email,
                        'overview': overview,
                        'experience': experience,
                        'address': address,
                        'skills': skills,
                        'interests': interests,
                        'education_details': education_details,
                        'certifications': certifications,
                        'notification': notification,
                            }

        user_profile.objects.update_or_create(user_email=username, defaults=updated_details)
        return my_profile_feed(request)
    else:
        return HttpResponseRedirect(reverse_lazy('signin:signin'))

def customViewProfile(request):
    if request.session.has_key('username'):
        username = request.session['username']
        user_name = user_profile.objects.get(user_email=username).user_name
        profile_user_email = request.GET.get('profile_user_email')
        profile_user_name = user_profile.objects.get(user_email=profile_user_email).user_name
        user_profile_details = user_profile.objects.get(user_email = profile_user_email)
        user_img = user_profile_details.user_image

        if request.method == "GET" and request.GET.get("follow_button") == "Follow":
            # follow_registered = False
            following_email = request.GET.get("profile_user_email")
            following_name = user_profile.objects.get(user_email=following_email).user_name
            print(following_name)
            print()
            print()
            print()
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

            # follower_list.append(Follower(name=, email=foll)))
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
                            'certifications': user_details.certifications, 'notification': user_details.notification, 'follow_notification': notification_list}
            user_profile.objects.update_or_create(user_email=user_details.user_email, defaults=user_updates)
            print(request.path_info)
            print()
            print()

        elif request.GET.get("follow_button") == "UnFollow":
            #UNFOLLOW LOGIC HERE
            following_name = request.GET.get("profile_user_name")
            following_email = request.GET.get("profile_user_email")

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

        if Follow.objects.filter(user_name=username).exists():
            nfollower = len(Follow.objects.get(user_name=profile_user_email).follower)
            nfollowing = len(Follow.objects.get(user_name=profile_user_email).following)
        else:
            nfollower = 0
            nfollowing = 0
        count = 0

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
        return render(request, "customViewProfile.html", {'user_img':user_img, 'username':username, 'user_name':user_name, 'profile_user_name':profile_user_name, 'profile_user_email':profile_user_email, 'current_user_followings':current_user_followings, 'user_profile_details':user_profile_details, 'follower':nfollower,'following':nfollowing, 'notifications':notifications, 'chats': chats})
    else:
        return HttpResponseRedirect(reverse_lazy('signin:signin'))
