from django.urls import path

from .views import RobotAPIView

urlpatterns = [
    path('', RobotAPIView.as_view()),
]
