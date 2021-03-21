from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Contact)
# admin.site.register(Blog)
admin.site.register(question)
admin.site.register(forum)
admin.site.register(forumcomment)
admin.site.register(commentblog)
admin.site.register(notes)
admin.site.register(QA)
admin.site.register(courses)
admin.site.register(download)
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/tinyInject.js',)