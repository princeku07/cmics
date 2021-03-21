
from datetime import datetime
from django.shortcuts import render,HttpResponse
from .models import *
from django.http import JsonResponse
from django.http import Http404
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render,redirect,reverse
from . import forms,models
from .forms import CommentForm
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.views.generic import ListView,DetailView,CreateView
from django.conf import settings
from datetime import date, timedelta
from django.db.models import Q
from django.core.mail import send_mail
from django.views import generic
from django.contrib.auth.models import User



# from .forms import ContactForm

# Create your views here.
# def home(request):
   
#     blog = Blog.objects.all().filter(published=True).order_by('pub_date')[0:1]
#     return render(request,'home.html',{'blogs':blog})
class HomeView(ListView):
    model = Blog
    template_name = 'home.html'
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
     ordering = ['id']
def courses(request):
    
    return render(request,'course.html')
# class courses(ListView):
#     model = courses
#     template_name = 'course.html'
#     ordering = ['id']
class NoteView(ListView):
    model= notes
    template_name = 'note.html'   
class questionView(ListView):
    model = QA
    template_name = 'question.html'

    
def onlinequiz(request):
    return render(request,'onlinequiz.html')
class downloads(ListView):
    model = download
    fields = ['download']
    template_name ='downloads.html'     

# def downloads(request):
#     return render(request,'downloads.html')
class forumView(ListView):
    model = forum
    template_name = 'forum.html'
    ordering = ['id']

class forumcomment(CreateView):
    model = forumcomment
    form_class = CommentForm
    template_name = 'forumcomment.html'
    ordering = ['pk']
    def form_valid(self,form):
        form.instance.forum_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('forum')

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
