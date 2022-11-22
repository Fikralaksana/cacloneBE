from django.contrib import admin
from django.contrib.sessions.models import Session
from .models import Course,Lesson,Owner,Code,Language

# Register your models here.

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Owner)
admin.site.register(Code)
admin.site.register(Session)
admin.site.register(Language)
