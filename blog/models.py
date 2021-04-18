from django.db import models
from django_resized import ResizedImageField
from datetime import datetime,date
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=255)
    
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural= "Categories"
        ordering = ['-category']
    def __str__(self):
        return self.category
        
    def get_absolute_url(self):
        return reverse('blog')
class Blog(models.Model):
    title = models.CharField(max_length=100,null=True)
    image = models.ImageField(null=True)
    content = RichTextUploadingField(null=True,blank=True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)
    published = models.BooleanField(default=None)
    category = models.CharField(max_length=255, default='')
    categories = models.ForeignKey(Category,verbose_name='Category',on_delete=models.PROTECT)
    snippet = models.CharField(max_length=500,default="click to read more",null=True)
    
    def __str__(self):
        return self.title
class commentblog(models.Model):
    Blog = models.ForeignKey(Blog,related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    body = models.TextField(null=True)
    
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s - %s' % (self.Blog.title, self.name)
    
class courses(models.Model):
    title = models.CharField(max_length=100)
    course = models.CharField(max_length=500)
    def __str__(self):
        return self.title
    
class notes(models.Model):
    title = models.CharField(max_length=100)
    notes = RichTextUploadingField(blank=True,null=True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)
    published = models.BooleanField(default=True)
    pdf_file = models.FileField(upload_to='documents',default='')
    snippet = models.CharField(max_length=500,default="click to read more")
    def __str__(self):
        return self.title
class download(models.Model):
    title = models.CharField(max_length=100)
    download = models.FileField(upload_to='documents')
class QA(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField(null=True,blank=True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)
    published = models.BooleanField(default=True)
    snippet = models.CharField(max_length=500,default="click to read more")
    def __str__(self):
        return self.title

# class question(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField(null=True,blank=True)
#     pub_date = models.DateTimeField(auto_now_add=True,null=True)
#     published = models.BooleanField(default=True)
#     def __str__(self):
#         return self.title
class forum(models.Model):
    title = models.CharField(max_length=100)
    # content = RichTextField(blank=True,null=True)
    content = RichTextUploadingField(null=True,blank=True)
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


class Vedios(models.Model):
    title = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()  # same like models.URLField()
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-added']
    



    
 
