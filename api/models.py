from django.db import models
from django.contrib.sessions.models import Session
import datetime

# Create your models here.

def setToken():
    return str(datetime.datetime.timestamp(datetime.datetime.now())*1000)

def getUploadPath(instance,filename):
    return f'code/{instance.owner.session_key}/{instance.lesson.id}/{filename}'

class Course(models.Model):
    LANGUAGES=(("python","python"),)
    name=models.CharField(max_length=255)
    language=models.CharField(choices=LANGUAGES,max_length=50)
    def __str__(self) -> str:
        return self.name


class Lesson(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name="lessons")
    name=models.CharField(max_length=255)
    instructions=models.TextField()
    def __str__(self) -> str:
        return self.name

class Owner(models.Model):
    token=models.CharField(max_length=255,default=setToken)
class Code(models.Model):
    lesson=models.ForeignKey(Lesson,on_delete=models.CASCADE)
    owner=models.ForeignKey(Session,on_delete=models.CASCADE,related_name="codes")
    code=models.FileField(upload_to=getUploadPath)
    def __str__(self) -> str:
        return self.code.name
    

