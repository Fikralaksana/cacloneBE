from .models import Course
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import CourseSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer