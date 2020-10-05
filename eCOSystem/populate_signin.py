import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eCOSystem.settings')

import django
django.setup()
from faker import Faker
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from signin.models import signup_model
from my_profile_feed.models import user_profile, Address
from profiles.models import Follow, Follower, Following
fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_name = fakegen.name()
        fake_phone = fakegen.phone_number()
        fake_email = fakegen.email()
        fake_password = fakegen.ean8()
        fake_repeat_password = fake_password

        hashed_password = make_password(fake_password)
        #get entry for User
        user = signup_model.objects.get_or_create(full_name=fake_name, phone=fake_phone, email=fake_email, password=hashed_password,
        repeat_password=fake_repeat_password)[0]

        usr = user_profile(
                user_name=fake_name,
                user_email=fake_email,
                overview="",
                experience=[],
                address=Address(),
                skills = [],
                interests = [],
                education_details = [],
                certifications = [],
                notification = [],
                follow_notification = [],
                chats = [])

        usr.save()
        Follow(user_name = fake_email, follower=[], following=[]).save()
        User(username=fake_name, email=fake_email, password=hashed_password).save()


if __name__ == '__main__':
    print('populating script running!...')
    populate(20)
    print('populating script complete')
