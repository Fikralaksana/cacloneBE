from django.db import models

# Create your models here.

class Course(models.Model):
    LANGUAGES=(("python","python"),)
    name=models.CharField(max_length=255)
    language=models.CharField(choices=LANGUAGES)


class Lesson(models.Model):
    name=models.CharField(max_length=255)
