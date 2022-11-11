from django.urls import path,include
from caclone.urls import router
from .views import UserViewSet

router.register(r'courses', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]