from django.urls import path,include
from .views import UI



urlpatterns = [
    path('', UI.as_view(), name='ui')
]