from django.urls import path,include
from rest_framework import routers
from .views import CourseViewSet,LessonViewSet,OwnerView

router = routers.DefaultRouter()

router.register(r'courses', CourseViewSet)
router.register(r'lessons', LessonViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('code/<int:lesson>', OwnerView.as_view(),name="owner"),
]