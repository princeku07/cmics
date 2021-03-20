from django.db import models
from django_resized import ResizedImageField
from datetime import datetime,date

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True,blank=True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)
    published = models.BooleanField(default=True)
    snippet = models.CharField(max_length=500,default="click to read more")
    def __str__(self):
        return self.title
class commentblog(models.Model):
    Blog = models.ForeignKey(Blog,related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    body = models.TextField(null=True)
    
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s - %s' % (self.Blog.title, self.name)
    

class question(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True,blank=True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)
    published = models.BooleanField(default=True)
    def __str__(self):
        return self.title
class forum(models.Model):
    title = models.CharField(max_length=100)
    # content = RichTextField(blank=True,null=True)
    content = models.TextField(null=True,blank=True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)
    published = models.BooleanField(default=True)
    snippet = models.CharField(max_length=500,default="read more")
    def __str__(self):
        return self.title
# class downloads(models.Model):
#     title 
class forumcomment(models.Model):
    forum = models.ForeignKey(forum,related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    body = models.TextField(null=True,)
    image = models.ImageField(null=True,blank=True,upload_to="images/")
    
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default= '')
    phone = models.CharField(max_length=70, default= '')
    email = models.CharField(max_length=70, default= '')
    desc = models.CharField(max_length=5000, default= '')

    def __str__(self):
        return self.name





    
 