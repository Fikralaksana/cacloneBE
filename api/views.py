import pathlib
from .models import Course,Lesson,Owner,Code
from django.contrib.sessions.models import Session
from django.conf import settings
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import permissions
from api.serializers import CourseSerializer,LessonSerializer,OwnerSerializer,CodeSerializer
from django.core.files import File
from io import BytesIO


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

class CodeView(APIView):
    def get(self,request:Request,lesson,format=None):
        if not request.session or not request.session.session_key:
            request.session.save()
        key=request.session.session_key
        owner_qset=Session.objects.filter(session_key=key)
        file=BytesIO(b"halooo")
        file.name="main.py"
        file=File(file)
        owner=owner_qset.last()
        lessons_qset=owner.codes.filter(lesson__id=lesson)
        if len(lessons_qset)==0:
            code=CodeSerializer(data={"lesson":lesson,"code":file,"owner":owner})
            if code.is_valid():
                code.save()
        else:
            code=CodeSerializer(lessons_qset.last())
        response=Response(code.data)
        return response

class CodeViewSet(viewsets.ModelViewSet):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer
    def partial_update(self, request, *args, **kwargs):
        path=self.get_object().code.path
        with open(path,"w") as f:
            f.write(request.data.get('code_string'))

        return super().partial_update(request, *args, **kwargs)





