from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path,re_path,include
from . import views
from .views import *

admin.site.header = "CMICS"
admin.site.site_title = "Welcome to CMICS Dashboard"
admin.site.index_title = "CMICS"
urlpatterns = [
    # path('',views.home, name ='home'),
    path('',HomeView.as_view(), name ='home'),
    path('about',views.about, name ='about'),
    path('blog/<int:pk>',blogDetailview.as_view(), name ='blog-detail'),
    
    path('contact',views.contact, name='contact'),
    # path('CurrentAffairs', views.CurrentAffairs,name='CurrentAffairs')
    path('blog',BlogView.as_view(),name='blog'),
    path('forum/<int:pk>',forumdetailview.as_view(),name='forum-detail'),
    path('courses', views.courses,name='courses'),
    path('forum', forumView.as_view(),name='forum'),
    # path('question', views.question,name='question'),
    path('downloads', downloads.as_view(),name='downloads'),
    path('blogcomment/<int:pk>/comment/',blogcomment.as_view(),name='blogcomment'),
    path('forumcomment/<int:pk>/comment/',forumcomment.as_view(),name='forumcomment'),
    path('another', views.another,name='another'),
    path('onlinquiz',views.onlinequiz,name='onlinequiz'),
    path('question',questionView.as_view(),name='question'),
    path('note',NoteView.as_view(),name='note'),
    path('register', views.register,name='register'),
    path('searchblogs', views.searchBlogs,name='searchblogs'),
 
    path('login', views.loginpage,name='login'),
    path('logout', views.logoutUser,name='logout'),
    path('note/<int:pk>',Notedetailview.as_view(), name ='notes_detail'),
    path('question/<int:pk>',Questiondetailview.as_view(), name ='QA_detail'),
    
]