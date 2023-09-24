from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic import View, FormView
from django.shortcuts import render
from .models import AdminModel, AddCollegeNewsModel, ModeratorModel, ArticleModel, MemberModel
from .forms import ModeratorForm
from django.contrib.messages.views import SuccessMessageMixin


class guest(CreateView,ListView):
    template_name = "guest.html"
    model = ArticleModel
    fields = ('articleid', 'category', 'tag', 'article')
    success_url = '/guest/'    

class AdminLogin(View):
    def post(self,request):
        username=request.POST.get("uname")
        password=request.POST.get("upass")
        qs=AdminModel.objects.filter(username=username,password=password)
        if not qs:
            return render(request,"adminlogin.html",{"msg":"Please enter correct details"})
        else:
            return render(request,"welcomeadmin.html")

def getcollegenews(request):
    qs=AddCollegeNewsModel.objects.all()
    return render(request,"adminnews.html",{"data":qs})

class AddCollegeNews(View):
    def post(self,request):
        heading=request.POST.get("heading")
        enternews=request.POST.get("enternews")
        ac=AddCollegeNewsModel(heading=heading,enternews=enternews)
        ac.save()
        qs = AddCollegeNewsModel.objects.all()
        return render(request,"adminnews.html",{"msg":"News has been saved succesfully","data":qs})

class AddModerator(FormView,ListView):
    form_class = ModeratorForm
    template_name = "moderatordetails.html"
    queryset = ModeratorModel.objects.values('category', 'moderator_name', 'userid', 'password', 'mobile_num',
                                             'email_id')
    success_url = '/getmoderator/'
    def form_valid(self, form):
        category=form.cleaned_data['category']
        moderator_name=form.cleaned_data['moderator_name']
        userid=form.cleaned_data['userid']
        password=form.cleaned_data['password']
        mobile_num=form.cleaned_data['mobile_num']
        email_id=form.cleaned_data['email_id']
        ModeratorModel(category=category,moderator_name=moderator_name,userid=userid,password=password,
                       mobile_num=mobile_num,email_id=email_id).save()
        return super().form_valid(self)

class GetModerator(ListView,FormView):
    form_class = ModeratorForm
    model = ModeratorModel
    template_name = "moderatordetails.html"
    queryset = ModeratorModel.objects.values('category','moderator_name','userid','password','mobile_num','email_id')

class DeleteModerator(DeleteView):
    template_name = "moderatordetails.html"
    model = ModeratorModel
    success_url = '/addmoderator/'

class PostArticle(CreateView,ListView):
    template_name = "postarticle.html"
    model = ArticleModel
    fields = ('articleid','category','tag','article')
    success_url = '/postarticles/'

class UpdateArticle(UpdateView,ListView):
    template_name = "postarticle.html"
    model = ArticleModel
    fields = ('category', 'tag', 'article')
    success_url = '/postarticles/'

class UpdateStuArticle(UpdateView,ListView):
    template_name = "studentarticles.html"
    model=ArticleModel
    fields = ('category', 'tag', 'article')
    success_url = '/studentarticles/'


class DeleteArticle(DeleteView):
    template_name = "postarticle.html"
    model = ArticleModel
    success_url = '/postarticles/'


def moderatorLogin(request):
    userid=request.POST.get("userid")
    password=request.POST.get("password")
    qs=ModeratorModel.objects.filter(userid=userid,password=password)
    if not qs:
        return render(request,"moderatorlogin.html",{"msg":"Invalid user"})
    else:
        return render(request,"welcomemoderator.html",{"data":qs})


class PostArticleMod(CreateView,ListView):
    template_name = "moderatorarticle.html"
    model = ArticleModel
    fields = ('articleid', 'category', 'tag', 'article')
    success_url = '/postarticlesmod/'

class UpdateModeratorProfile(UpdateView):
    template_name = "moderatorupdate.html"
    model = ModeratorModel
    fields = ('category','moderator_name','password','mobile_num','email_id')
    success_url = '/moderatorhome/'

class SaveMember(CreateView):
    template_name = "memberregistration.html"
    model = MemberModel
    fields = ('member_name','member_id','password','mobile_num','email_id','address')
    success_url = '/member/'

def checkMember(request):
    memberid=request.POST.get("memberid")
    password=request.POST.get("mempass")
    request.session['memid']=memberid
    qs=MemberModel.objects.filter(member_id=memberid,password=password)
    if not qs:
        return render(request,"memberlogin.html",{"msg":"Invalid"})
    else:
        return render(request, "welcomemember.html", {"data": qs})



class PostStudentArticle(CreateView,ListView):
    template_name = "studentarticles.html"
    model = ArticleModel
    fields = ('articleid', 'category', 'tag', 'article')
    success_url = '/studentarticles/'


class UpdateStudentPro(SuccessMessageMixin,UpdateView):
    template_name = "memberupdate.html"
    model = MemberModel
    fields = ('member_name','password','mobile_num','email_id','address')
    success_url = '/memberhome/'
    success_message = "Updated successfully"

class DeleteStuArticle(DeleteView):
    model = ArticleModel
    success_url = '/studentarticles/'


def memberHome(request):
    qs=MemberModel.objects.all()
    return render(request,"welcomemember.html",{"data":qs})


def deletemember(request):
    mid=request.POST.get("mid")
    MemberModel.objects.filter(member_id=mid).delete()
    print(mid)
    return render(request,"welcomeadmin.html")


class UpdateModArticle(UpdateView,ListView):
    template_name = "moderatorarticle.html"
    model=ArticleModel
    fields = ('category', 'tag', 'article')
    success_url = '/postarticlesmod/'


class DeleteModArticle(DeleteView):
    model = ArticleModel
    success_url = '/postarticlesmod/'

