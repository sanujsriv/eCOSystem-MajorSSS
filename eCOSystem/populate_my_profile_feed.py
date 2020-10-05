import os

from django.template.defaultfilters import title
from faker.providers import company

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eCOSystem.settings')

import django
django.setup()

from faker import Faker
# from test_djongo2.basic_app.models import Skill, Interest, user_profile, Experience, Address, Education_details, Certifications
from my_profile_feed.models import Skill, Interest, user_profile, Experience, Address, Education_details, Certifications
import random

fakegen = Faker()
fake_skills = ["PYTHON", "DJANGO", "MONGODB", "HTML", "CLOUD_COMPUTING"]
fake_interests = ["DATA_SCIENCE", "BLOCK_CHAIN", "COOKING", "CRICKET", "SINGING"]
fake_work_fields = ["DATA_SCIENCE","MACHINE_LEARNING","MEAN STACK","DJANGO_DEVELOPER"]
fake_study_fields = ["SCIENCE", "CHEMISTRY", "MATHEMATICS", "STATISTICS"]
fake_certificates = ["CCNA","OSCP","JAVA","DJANGO", "PROGRAMMING & DATA STRUCTURE USING PYTHON"]

def populate(N=5):
    for entry in range(N):
        #FAKE NAME
        fake_name = fakegen.name()
        #FALE EMAIL
        fake_email = fakegen.email()
        #FALE OVERVIEW
        fake_overview = fakegen.text(max_nb_chars=200, ext_word_list=None)
        #FAKE EXPERIENCE
        fake_company = fakegen.company()
        fake_title =  fakegen.job()
        fake_location = fakegen.address()
        fake_work_field = random.choice(fake_work_fields)
        fake_from_date = fakegen.date(pattern="%Y-%m-%d", end_datetime=None)
        fake_to_date = fakegen.date(pattern="%Y-%m-%d", end_datetime=None)
        fake_description_exp = fakegen.text(max_nb_chars=200, ext_word_list=None)
        #FAKE ADDRESS
        fake_locality = fakegen.street_address()
        fake_city = fakegen.city()
        fake_zip = fakegen.postcode()
        # state = models.ChoiceField(choices=STATES)
        fake_country = fakegen.country()
        #FAKE SKILL
        fake_skill_name = random.choice(fake_skills)
        #FAKE INTEREST
        fake_interest_name = random.choice(fake_interests)
        #FAKE EDUCATION DETAILS
        fake_school = fakegen.company()
        fake_school_from = fakegen.date(pattern="%Y-%m-%d", end_datetime=None)
        fake_school_to = fakegen.date(pattern="%Y-%m-%d", end_datetime=None)
        fake_degree = "INTERMEDIATE"
        fake_study_field = random.choice(fake_study_fields)
        fake_description_edu = fakegen.text(max_nb_chars=200, ext_word_list=None)
        #FAKE CERTIFICATION DETAILS
        fake_certification_name = random.choice(fake_certificates)
        fake_authority = fakegen.company()
        fake_cert_from = fakegen.date(pattern="%Y-%m-%d", end_datetime=None)
        fake_cert_to = fakegen.date(pattern="%Y-%m-%d", end_datetime=None)
        # fake_cert_pic = fakegen.image.avatar()

        #get entry for User




        # skl = Skill.objects.get_or_create(skill_name = fake_skill_name)[0]
        #
        # intrst = Interest.objects.get_or_create(interest_name = fake_interest_name)[0]

        usr = user_profile(
                user_name=fake_name,
                user_email=fake_email,
                overview=fake_overview,
                experience=[Experience(company=fake_company, title=fake_title, location=fake_location, work_field=fake_work_field, from_date=fake_from_date,
                               to_date=fake_to_date, descriptionExp=fake_description_exp)],
                address=Address(locality=fake_locality, city=fake_city, zip=fake_zip, country=fake_country),
                skills = [Skill(skill_name=fake_skill_name)],
                interests = [Interest(interest_name=fake_interest_name)],
                education_details = [Education_details(school=fake_school, school_from=fake_school_from, school_to=fake_school_to,
                                                      degree=fake_degree, study_field=fake_study_field, descriptionEdu=fake_description_edu)],
                certifications = [Certifications(certification_name=fake_certification_name, authority=fake_authority, cert_from=fake_cert_from,
                                                cert_to=fake_cert_to)])


        # usr = user_profile(
        #             user_name="SANUJ KUMAR",
        #             user_email="SANUJ@GMAIL.COM",
        #             overview="GREAT EXP...",
        #             experience=Experience(company="XDA",title="ANDROID DEVELOPER",location="FROM HOME", work_field="ANDROID",
        #                                   from_date="2018-05-05", to_date="2018-05-05", descriptionExp="GREAT Exp.."),
        #             address=Address(locality="GARHI GAO", city="GHAZIABAD", zip="201002", country="INDIA"),
        #             skills=[Skill(skill_name="DJANGO")],
        #             interests=[Interest(interest_name="FOOD LOVER")],
        #             education_details=Education_details(school="ABC INTER COLLEGE", school_from="2018-05-05", school_to="2018-05-05",
        #                                                 degree="INTERMEDIATE", study_field="SCIENCE", descriptionEdu="GREAT Exp.."),
        #             certifications=Certifications(certification_name="JAVA", authority="NASSCOM",
        #                                           cert_from="2018-05-05", cert_to="2018-05-05"))
        usr.save()

if __name__ == '__main__':
    print('populating script running!...')
    populate(20)
    print('populating script complete')
