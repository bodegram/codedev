from django.db import models
from django.contrib.auth.models import User, AbstractUser
import datetime
# Create your models here.


class Careers(models.Model):
    specialization = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(null=True, blank=True)
    title = models.CharField(max_length=2000, blank=True)
    details1 = models.TextField(max_length=20000, blank=True)
    details2 = models.TextField(max_length=20000, blank=True)
    image = models.ImageField(upload_to='media', blank=True)
    dateupdate = models.DateField(blank=True)
    author = models.CharField(max_length=2000, blank=True)

    def __str__(self):
        return self.specialization

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    gender = models.CharField(blank=True, max_length=1000)
    billing_address = models.CharField(max_length=100000000, blank=True)
    specialization = models.CharField(max_length=1000000000, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Careers_comments(models.Model):
    course = models.CharField(blank=True, max_length=2000)
    comment = models.TextField(max_length=20000, blank=True)
    slug = models.SlugField(null=True, blank=True)
    likes = models.ManyToManyField(CustomUser, blank=True, related_name="likes")
    user = models.CharField(max_length=2000, blank=True)
    
    

    def __str__(self):
        return self.course 

class Newsletter(models.Model):
    email = models.EmailField(unique=True)

class Job(models.Model):
    company_name = models.CharField(max_length=10000000, blank=True)
    address = models.CharField(max_length=10000000, blank=True)
    country = models.CharField(max_length=10000000, blank=True)
    website = models.CharField(max_length=10000000, blank=True)
    role = models.CharField(max_length=10000000, blank=True)
    work_experience = models.CharField(max_length=10000000, blank=True)
    job_description = models.TextField(max_length=10000000, blank=True)
    requirement = models.TextField(max_length=10000000, blank=True)
    date_added = models.DateField(auto_created=datetime.date.today(), blank=True)

class Apply(models.Model):
    first_name = models.CharField(max_length=100000, blank=True)
    last_name = models.CharField(max_length=100000, blank=True)
    email = models.EmailField(blank=True)
    portfolio = models.URLField(blank=True)
    resume = models.FileField(upload_to='')
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    date_added = models.DateField(auto_created=datetime.date.today(), blank=True)


class Course(models.Model):
    title = models.CharField(max_length=10000, blank=True)
    description = models.TextField()
    group = models.CharField(max_length=100000, blank=True)

    def __str__(self):
        return self.title



class Course_topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    topic =  models.CharField(max_length=10000, blank=True)
    video = models.FileField(upload_to='', blank=True)
    description = models.TextField()
    lesson = models.CharField(max_length=100000, blank=True)

    def __str__(self):
        return self.topic




