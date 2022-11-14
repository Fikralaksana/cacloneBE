from .models import Course,Lesson
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import CourseSerializer,LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LessonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer