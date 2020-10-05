from djongo import models
# from django_mongodb_engine.storage import GridFSStorage
# from .forms import ExperienceForm, AddressForm, SkillForm, InterestForm, Education_detailsForm, CertificationsForm
# Create your models here.

class Notification(models.Model):
    post_title = models.CharField(max_length=50)
    post_author = models.EmailField()
    author =  models.EmailField()
    text = models.TextField(max_length = 200)
    created_on = models.DateTimeField(blank=True)

class FollowNotification(models.Model):
    author =  models.EmailField()
    text = models.TextField(max_length = 200)
    created_on = models.DateTimeField(blank=True)

class Chats(models.Model):
    sender_name = models.CharField(max_length=50)
    sender_email = models.EmailField()
    receiver_name = models.CharField(max_length=50)
    receiver_email = models.EmailField()
    message = models.TextField(max_length=200)
    created_on = models.DateTimeField(blank=True)

class Experience(models.Model):
    company = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    work_field = models.CharField(max_length=200)
    from_date = models.DateField(blank=True)
    to_date = models.DateField(blank=True)
    descriptionExp = models.TextField()

class Address(models.Model):
    locality = models.CharField(max_length=120)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=6)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=50)

class Skill(models.Model):
    skill_name = models.CharField(max_length=50)


class Interest(models.Model):
    interest_name = models.CharField(max_length=50)


class Education_details(models.Model):
    school = models.CharField(max_length=50)
    school_from = models.DateField(blank=True)
    school_to = models.DateField(blank=True)
    degree = models.CharField(max_length=50)
    study_field = models.CharField(max_length=50)
    descriptionEdu = models.TextField()


class Certifications(models.Model):
    certification_name = models.CharField(max_length=200)
    authority = models.CharField(max_length=200)
    cert_from = models.DateField(blank=True)
    cert_to = models.DateField(blank=True)
    cert_pic = models.ImageField(upload_to='certificate_pics', blank=True)

class user_profile(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    user_image = models.ImageField(upload_to='profile_images', blank=True, default='pf-icon1.png')
    overview = models.TextField()
    experience = models.ArrayModelField(
        model_container = Experience,
    )
    address = models.EmbeddedModelField(
        model_container = Address,
    )
    skills = models.ArrayModelField(
        model_container = Skill,
    )
    interests = models.ArrayModelField(
        model_container = Interest,
       )
    education_details = models.ArrayModelField(
        model_container = Education_details,
    )
    certifications = models.ArrayModelField(
        model_container = Certifications,
    )
    notification = models.ArrayModelField(
        model_container=Notification,
    )
    follow_notification = models.ArrayModelField(
        model_container = FollowNotification
    )

    chats = models.ArrayModelField(
        model_container = Chats
    )

    objects = models.DjongoManager()
    def __str__(self):
        return self.user_email
