from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from datetime import datetime
from django.shortcuts import render,HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.http import JsonResponse
from django.http import Http404
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render,redirect,reverse
from . import forms,models
from .forms import CommentForm,BlogForm
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView
from django.conf import settings
from datetime import date, timedelta
from django.db.models import Q
from django.core.mail import send_mail
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
from .models import Vedios
# from .forms import ContactForm

# Create your views here.
# def home(request):
   
#     blog = Blog.objects.all().filter(published=True).order_by('pub_date')[0:1]
#     return render(request,'home.html',{'blogs':blog})

class HomeView(ListView):
    model = Blog
    template_name = 'another.html'
    ordering = ['id']

class blogDetailview(DetailView):
    model = Blog
    template_name = 'blog_details.html'
class forumdetailview(DetailView):
    model = forum
    template_name = 'forum-detail.html'

class BlogView(ListView):
     model = Blog
     template_name = 'blog.html'
     ordering = ['-id']
     paginate_by = 4
     paginate_orphans = 1
     def get_context_data(self,*args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(BlogView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context
def CategoryView(request, cats):
    category_posts = Blog.objects.filter(category= cats)
    
    return render(request,'categories.html',{'cats':cats,'category_posts':category_posts})


def courses(request):
    
    return render(request,'course.html')
# class courses(ListView):
#     model = courses
#     template_name = 'course.html'
#     ordering = ['id']

class NoteView(ListView):
    model= notes
    fields = ['pdf_file']
    template_name = 'note.html' 
    paginate_by = 4
    paginate_orphans = 1
    ordering = ['-id']
class Notedetailview(DetailView):
    model = notes
    fields = ['pdf_file']
    template_name = 'notes_detail.html'
      
class questionView(ListView):
    model = QA
    template_name = 'Q&A.html'
    paginate_by = 4
    paginate_orphans = 1
    ordering = ['-id']

def video(request):
    V = Vedios.objects.all()
    context = {
        'vedios':V
    }
    return render(request,'video.html',context)

class Questiondetailview(DetailView):
    model = QA
    template_name = 'Q&A_detail.html'


    
def onlinequiz(request):
    return render(request,'onlinequiz.html')
class downloads(ListView):
    model = download
    fields = ['download']
    template_name ='downloads.html' 
    ordering = ['-id']    

# def downloads(request):
#     return render(request,'downloads.html')
class forumView(ListView):
    model = forum
    template_name = 'forum.html'
    ordering = ['-id']

class forumcomment(CreateView):
    model = forumcomment
    form_class = CommentForm
    template_name = 'forumcomment.html'
    ordering = ['pk']
    def form_valid(self,form):
        form.instance.forum_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('forum')
class blogcomment(CreateView):
    model = commentblog
    form_class = BlogForm
    template_name = 'blogcomment.html'
    ordering = ['pk']
    def form_valid(self,form):
        form.instance.forum_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('blog')

class commentblog(CreateView):
    model = commentblog
    template_name = 'forumcomment.html'
    fields = '__all__'

def contact(request):
    # form = ContactForm()
    if  request.method=="POST":
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        desc = request.POST.get('desc', '')
        
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')
def another(request):
    return render(request,'another.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid:
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account is created with username ' + user )
            return redirect('login')
    context = {'form':form}
    return render(request,'accounts/register.html',context)
    
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password in incorrect')
    context = {}        
    return render(request,'accounts/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')
def searchBlogs(request):
    query = request.GET.get('query')
    if len(query) > 60:
        allblogs = Blog.objects.none()
    else:
        allblogstitle = Blog.objects.filter(title__icontains = query)
        allblogscontent = Blog.objects.filter(content__icontains= query)
        allblogs = allblogstitle.union(allblogscontent)
    if allblogs.count() == 0:
        messages.error(request,"No search result found")
    params = {'allblogs': allblogs,'query':query}
    return render(request,'searchblog.html',params)
