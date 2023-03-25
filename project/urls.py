"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('profile/', views.profile, name="profile"),
    path('learn/', views.learn, name="learn"),
    path('course/<int:id>', views.course, name="course"),
    path('edit-profile/', views.edit_profile, name="edit_profile"),
    path('forgotpassword/', views.forgotpassword, name="forgotpassword"),
    path('blog/posts/<slug:slug>', views.blog_details, name="blog_details"),
    path('jobs/center', views.jobcenter, name="jobcenter"),
    path('jobs/post', views.postjob, name="postjob"),
    path('jobs/<int:id>', views.job, name="job"),
    path('jobs/<int:id>/job-application', views.apply, name="apply"),
    path('blog/', views.blog, name="blog"),
    path('logout/', views.logout, name="logout"),
    path('addComment/<slug:slug>', views.addComment, name="addComment"),
    path('addCommentLike/<int:id>', views.addCommentLike, name="addCommentLike")

    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
