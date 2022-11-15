from django.urls import path,include
from rest_framework import routers
from .views import CourseViewSet,LessonViewSet,CodeView, CodeViewSet

router = routers.DefaultRouter()

router.register(r'courses', CourseViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'codes', CodeViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('code/<int:lesson>', CodeView.as_view(),name="lesson"),
]