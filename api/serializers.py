from .models import Course,Lesson,Code,Owner
from django.contrib.sessions.models import Session
from rest_framework import serializers



class LessonCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','name','language']
class LessonSerializer(serializers.ModelSerializer):
    course=LessonCourseSerializer(read_only=True)
    class Meta:
        model = Lesson
        fields = ["id","name","instructions","course"]
class CourseSerializer(serializers.ModelSerializer):
    lessons=LessonSerializer(many=True,read_only=True)
    class Meta:
        model = Course
        fields = ['id','name','language','lessons']

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Session
        fields=["id","session_key"]
class CodeSerializer(serializers.ModelSerializer):


    class Meta:
        model = Code
        fields = ["id","owner","code","lesson"]