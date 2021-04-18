from django.contrib import admin
from embed_video.admin import AdminVideoMixin
# Register your models here.
from .models import *


admin.site.register(Contact)


admin.site.register(forumcomment)
admin.site.register(commentblog)
# admin.site.register(QA)
admin.site.register(courses)
admin.site.register(download)

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(notes)
admin.site.register(forum)
admin.site.register(QA)
class MyModelAdmin(AdminVideoMixin,admin.ModelAdmin):
    pass
admin.site.register(Vedios,MyModelAdmin)
# @admin.register(forum)
# class forumadmin(admin.ModelAdmin):
#     class Media:
#         js = ('js/tinyInject.js',)
