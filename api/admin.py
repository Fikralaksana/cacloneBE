from django.contrib import admin
from .models import Course,Lesson,Owner,Code

# Register your models here.

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Owner)
admin.site.register(Code)
