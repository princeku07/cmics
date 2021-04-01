from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Contact)
# admin.site.register(Blog)
# admin.site.register(question)

admin.site.register(forumcomment)
admin.site.register(commentblog)
# admin.site.register(QA)
admin.site.register(courses)
admin.site.register(download)
admin.site.register(Profile)
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/tinyInject.js',)
    
@admin.register(forum)
class forumadmin(admin.ModelAdmin):
    class Media:
        js = ('js/tinyInject.js',)

@admin.register(notes)
class notesadmin(admin.ModelAdmin):
    class Media:
        js = ('js/notes.js',)

@admin.register(QA)
class QAadmin(admin.ModelAdmin):
    class Media:
        js = ('js/tinyInject.js',)
