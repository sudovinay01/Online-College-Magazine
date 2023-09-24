"""projectocm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic import TemplateView, ListView
from app1 import views
from app1.models import MemberModel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name="index.html")),
    path('home/',TemplateView.as_view(template_name="index.html")),
    path('adminlogin/', TemplateView.as_view(template_name="adminlogin.html")),
    path('admincheck/',views.AdminLogin.as_view()),
    path('adminnews/',views.getcollegenews),
    path('saveadminnews/',views.AddCollegeNews.as_view()),
    path('addmoderator/',views.AddModerator.as_view()),
    path('getmoderator/',views.GetModerator.as_view()),
    path('deletemoderator<int:pk>/',views.DeleteModerator.as_view()),
    path('adminlogout/',TemplateView.as_view(template_name="adminlogin.html")),
    path('adminhome/',TemplateView.as_view(template_name="welcomeadmin.html")),
    path('postarticles/',views.PostArticle.as_view()),
    path('updatearticle<int:pk>/',views.UpdateArticle.as_view()),
    path('updatemodarticle<int:pk>/',views.UpdateModArticle.as_view()),
    path('updatestuarticle<int:pk>/',views.UpdateStuArticle.as_view()),
    path('deletearticle<int:pk>/',views.DeleteArticle.as_view()),
    path('deletemodarticle<int:pk>/',views.DeleteModArticle.as_view()),
    path('deletestuarticle<int:pk>/',views.DeleteStuArticle.as_view()),
    path('moderatorlogin/',views.moderatorLogin),
    path('moderatorhome/',TemplateView.as_view(template_name="welcomemoderator.html")),
    path('postarticlesmod/',views.PostArticleMod.as_view()),
    path('updatemodprofile<int:pk>/',views.UpdateModeratorProfile.as_view()),
    path('member/',TemplateView.as_view(template_name="memberlogin.html")),
    path('memberregister/',views.SaveMember.as_view()),
    path('checkmember/',views.checkMember),
    path('memberhome/',views.memberHome),
    path('deletemember/',ListView.as_view(template_name="deletemember.html", model=MemberModel)),
    path('deletememberid/',views.deletemember),
    path('studentarticles/',views.PostStudentArticle.as_view()),
    path('updatestudentprofile<int:pk>/',views.UpdateStudentPro.as_view()),
    path('memberlogout/',TemplateView.as_view(template_name="memberlogin.html")),
    path('memberhome2/',TemplateView.as_view(template_name="welcomemember.html")),
    path('moderatorlogout/',TemplateView.as_view(template_name="moderatorlogin.html")),
    path('guest/',views.guest.as_view())
]
