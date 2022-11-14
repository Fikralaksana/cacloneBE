from django.db import models

# Create your models here.

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
    

