from django.shortcuts import render, redirect
from .models import Careers, Careers_comments
import random
from django.contrib import messages
import datetime
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.hashers import make_password
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    rdm1 = random.randint(0,7)
    rdm2 = random.randint(6,14)
    specializations = Careers.objects.all()[rdm1: rdm2]
   

    return render(request, 'index.html', {"specializations": specializations})

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Incorrect email address or password")
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        gender = request.POST['gender']
        billing_address = request.POST['billing_address']
        specialization = request.POST['specialization']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        random_no = random.randint(10, 100)
        username = first_name +  str(random_no)
        if cpassword == password:
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, "Email Address already taken")
            elif CustomUser.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
            else:
                CustomUser.objects.create(first_name=first_name, last_name=last_name, email=email, gender=gender, billing_address=billing_address, specialization=specialization, password=make_password(password), username=username)
        else:
            messages.error(request, "Password does not match")
    specializations = Careers.objects.all()
    return render(request, 'register.html', {"specializations": specializations})

@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'dashboard.html')

def forgotpassword(request):
    return render(request, 'forgotpassword1.html')

def blog_details(request, slug):
    spec = Careers.objects.get(slug=slug)
    post_comments = Careers_comments.objects.filter(course=spec.specialization).all().order_by('-id')[:5]
    count = Careers_comments.objects.filter(course=spec.specialization).count()
    context = {
        "course" : spec,
        "comments" : post_comments,
        "count":  count
    }
    return render(request, 'blog_details.html', context)

def jobcenter(request):
    p = Paginator(Job.objects.all(), 10)
    page = request.GET.get("page")
    jobs = p.get_page(page)
    job_count = Job.objects.all().count()
    return render(request, 'jobcenter.html', {"jobs": jobs, "job_count": job_count})

@login_required(login_url='/login/')
def postjob(request):
    if request.method == "POST":
        company_name = request.POST['company_name']
        address = request.POST['address']
        country = request.POST['country']
        website = request.POST['website']
        role = request.POST['role']
        work_experience = request.POST['work_experience']
        job_description = request.POST['job_description']
        requirement = request.POST['requirement']
        Job.objects.create(company_name=company_name, address=address,country=country, website=website, role=role, work_experience=work_experience, job_description=job_description, requirement=requirement)
        messages.success(request, "Job posted successsfully")
    return render(request, 'postjob.html',)

def blog(request):
    randomPost = random.randint(4, 10)
    specializations = Careers.objects.all().order_by('?')[:randomPost]
    

    context= {
        "specializations" : specializations,
        
    }
    return render(request, 'blog.html', context)

@login_required(login_url='/login/')
def logout(request):
    auth.logout(request)
    return redirect("login")

@login_required(login_url='/login/')
def addComment(request, slug):
     if request.method == "POST":
        comment = request.POST['comment']
        user = request.user
        spec = Careers.objects.get(slug=slug)
        comments = Careers_comments.objects.create(comment=comment, course=spec.specialization, user=user)
        if comments:
            print("Success")
            return redirect('course', slug=slug)
        else:
            print("An error occured")


def addCommentLike(request, id):
    comment = Careers_comments.objects.get(id=id) 
    isLike = False
    for like in comment.likes.all():
        if like == request.user:
            isLike = True
            break
    if not isLike:
        comment.likes.add(request.user)
    if isLike:
        comment.likes.remove(request.user)

def newsletter_subscription(request):
    if request.method == "POST":
        email = request.POST['email']
        if Newsletter.objects.filter(email=email).exists():
            return render(request, 'newletter_email_exists.html', {"email": email})
        else:
            Newsletter.objects.create(email=email)
            return render(request, "newsletter_subscription.html", {"email": email})

def job(request, id):
    try:
        job_id = Job.objects.get(id=id)
    except Job.DoesNotExist:
        return render(request, 'not_found.html')

    return render(request, 'job.html', {"job":job_id})

def apply(request, id):
    try:
        job_id = Job.objects.get(id=id)
    except Job.DoesNotExist:
        return render(request, 'not_found.html')
    if request.method == "POST" and request.FILES['resume']:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        portfolio = request.POST['portfolio']
        resume = request.FILES['resume']
        fs = FileSystemStorage()
        file = fs.save(resume.name, resume)
        fss = fs.url(file)
        Apply.objects.create(first_name=first_name, last_name=last_name,email=email,portfolio=portfolio,resume=fss)
        messages.success(request, "You have successfully applied for this job")

    return render(request, 'apply.html', {"job": job_id})

@login_required(login_url='/login/')
def profile(request):
    return render(request, "profile.html")

@login_required(login_url='/login/')
def edit_profile(request):
    return render(request, "edit_profile.html")

def learn(request):
    p = Paginator(Course.objects.all(), 1)
    page = request.GET.get("page")
    courses = p.get_page(page)
    course_count = Course.objects.all().count()
    return render(request, 'learn.html', {"courses": courses, "course_count": course_count})

def course(request, id):
    try:
        course_id = Course.objects.get(id=id)
    except Course.DoesNotExist:
        return redirect("learn")

    topics = Course_topic.objects.filter(course= course_id).all()
    return render(request, "course.html", {"course": course_id, "topics": topics})






        









