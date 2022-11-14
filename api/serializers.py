from .models import Course,Lesson
from rest_framework import serializers



class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["id","name","instructions"]
class CourseSerializer(serializers.ModelSerializer):
    lessons=LessonSerializer(many=True,read_only=True)
    class Meta:
        model = Course
        fields = ['id','name','language','lessons']