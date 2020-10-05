import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eCOSystem.settings')

import django
django.setup()

from django.contrib.auth.models import User
from signin.models import signup_model
from index.models import Posts
from my_profile_feed.models import user_profile
from profiles.models import Follow


all_profiles = [
    {
        "full_name" : "Curtis Riley",
        "phone" : "(553)540-3723",
        "email" : "qjohnson@yahoo.com",
        "password" : "argon2$argon2i$v=19$m=512,t=2,p=2$TzNGdjNtcU5tN0dv$skzOqg5ngZRDwf8cbqHDtg",
        "repeat_password" : "31547161"
    },
    {
        "full_name" : "Vanessa Mack",
        "phone" : "0003449334",
        "email" : "terrellmark@yahoo.com",
        "password" : "argon2$argon2i$v=19$m=512,t=2,p=2$T0xsSXVyWmt4b05F$Yjt4STlh21saq0RvavkZdQ",
        "repeat_password" : "99096489"
    },
    {
        "full_name" : "Alicia Leach DDS",
        "phone" : "(480)528-2730",
        "email" : "sotobenjamin@gmail.com",
        "password" : "argon2$argon2i$v=19$m=512,t=2,p=2$YnpFdGFWYTgxejhX$koqA5SHL84qD5QdI0X+vbQ",
        "repeat_password" : "41634493"
    },
    {
        "full_name" : "Megan Curtis",
        "phone" : "870-879-4368",
        "email" : "kathrynhernandez@yahoo.com",
        "password" : "argon2$argon2i$v=19$m=512,t=2,p=2$d1dkemhsR09Bb3N5$6Qrce6qHDQaAR+GcQtqP6A",
        "repeat_password" : "57225944"
    },
    {
        "full_name" : "Sarah Porter",
        "phone" : "4599217024",
        "email" : "fullerrebecca@gmail.com",
        "password" : "argon2$argon2i$v=19$m=512,t=2,p=2$OW9vb1RUU3N5NXRL$/A5pCBrSTuReqOmoftSnRA",
        "repeat_password" : "12503278"
    },
    {
        "full_name" : "Tony Davis",
        "phone" : "431-082-3662x30906",
        "email" : "vrodriguez@rice.biz",
        "password" : "argon2$argon2i$v=19$m=512,t=2,p=2$YXVwQ2ZSTnZHajhP$YRtonZw237U6fOgiZjF/JQ",
        "repeat_password" : "82793180"
    },
    {
        "full_name" : "Sherri Wright",
        "phone" : "(527)242-3559",
        "email" : "hreese@schwartz.net",
        "password" : "argon2$argon2i$v=19$m=512,t=2,p=2$cnlzcWpLOW5nVEtz$SVO4YU5MhqHZrTq1V1V3GA",
        "repeat_password" : "96205624"
    },
]

def delete():
    for i in range(len(all_profiles)):
        User.objects.filter(email=all_profiles[i]['email']).delete()
        signup_model.objects.filter(email=all_profiles[i]['email']).delete()
        user_profile.objects.filter(user_email=all_profiles[i]['email']).delete()
        Follow.objects.filter(user_name=all_profiles[i]['email']).delete()
        Posts.objects.filter(author=all_profiles[i]['email']).delete()


if __name__ == '__main__':
    print('deletion script running!...')
    delete()
    print('deletion script complete')
