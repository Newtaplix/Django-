from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
# Create your models here.\
class GeneralInfo(models.Model):
    company_name = models.CharField(max_length=100, unique=True, default="Company")
    location = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    open_hours =models.CharField(max_length=100, blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedIn = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.company_name

class Services(models.Model):
    icon = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class Testemonail(models.Model):
    user_image = models.CharField(max_length=255, null=True, blank=True)

    star_count = [
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five'),
    ]
    rating_count = models.IntegerField(choices=star_count)
    username = models.CharField(max_length=50, unique=True)
    user_job_title = models.CharField(max_length=50)
    review = models.TextField()

    def __str__(self):
        return f"{self.username} - {self.user_job_title}"
    
class FrequentlyAskedQuestions(models.Model):
    question = models.TextField()
    anwser = models.TextField()

    def __str__(self):
        return self.question

class ContactFormLog(models.Model):
    name  = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    action_time = models.DateTimeField(null=True, blank=True)
    is_success = models.BooleanField(default=False)
    is_error = models.BooleanField(default=True)
    error_message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.email
    
class Authur(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50)
    join_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.firstname
class Blog(models.Model):
    blog_image = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=60, null=True, blank=True)
    title = models.CharField(max_length=255)
    # authur = models.CharField(max_length=50)
    authur = models.ForeignKey(Authur, on_delete=models.PROTECT, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    content = RichTextField()

    def __str__(self):
        return self.title
    