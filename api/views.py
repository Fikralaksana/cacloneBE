from .models import Course,Lesson,Owner,Code
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

class OwnerView(APIView):
    def get(self,request:Request,lesson,format=None):
        token=request.COOKIES.get("owner")
        owner_qset=Owner.objects.filter(token=token)
        file=BytesIO(b"halooo")
        file.name="main.py"
        file=File(file)
        if len(owner_qset)==0:
            owner=OwnerSerializer(data={})
            if owner.is_valid():
                owner.save()
            
            code= CodeSerializer(data={"owner":owner.instance.id,"code":file,"lesson":lesson})
            if code.is_valid():
                code.save()
        else:
            owner=OwnerSerializer(instance=owner_qset.first())
            code=CodeSerializer(Code.objects.filter(owner=owner.instance).first())
        response=Response(code.data)
        response.set_cookie(key="owner",value=owner.data.get("token"),max_age=60*60)
        return response




