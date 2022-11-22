import pathlib
import subprocess
from .models import Course,Lesson,Owner,Code
from django.views import View
from django.http import HttpResponse
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
from django.views.decorators.clickjacking import xframe_options_exempt,xframe_options_sameorigin
from django.utils.decorators import method_decorator
import json


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

class CodeView(View):
    def get(self,request:Request,lesson,format=None):
        if not request.session or not request.session.session_key:
            request.session.save()
        key=request.session.session_key
        owner_qset=Session.objects.filter(session_key=key)
        file=BytesIO(b"halooo")
        owner=owner_qset.last()
        lessons_qset=owner.codes.filter(lesson__id=lesson)
        if Lesson.objects.filter(id=lesson).first().course.language.first().type=="console":
            file.name="main.py"
        elif Lesson.objects.filter(id=lesson).first().course.language.first().type=="browser":
            file.name="index.html"
        file=File(file)
        if len(lessons_qset)==0:   
            code=CodeSerializer(data={"lesson":lesson,"code":file,"owner":owner})
            if code.is_valid():
                code.save()
        else:
            code=CodeSerializer(lessons_qset.last())
        return HttpResponse(json.dumps(code.data))
        

class CodeViewSet(viewsets.ModelViewSet):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer

    def partial_update(self, request, *args, **kwargs):
        path=self.get_object().code.path
        with open(path,"w") as f:
            f.write(request.data.get('code_string'))

        return super().partial_update(request, *args, **kwargs)

    def finalize_response(self, request:Request, response:Response, *args, **kwargs):
        if request.method=="PATCH":
            code=self.get_object()
            path=code.code.path
            if code.lesson.course.language.first().type=='console':
                shell=subprocess.run(["python",path],capture_output=True)
                response.data['output']=shell.stdout
            elif code.lesson.course.language.first().type=='browser':
                response.data['output']=code.code.url
        return super().finalize_response(request, response, *args, **kwargs)





