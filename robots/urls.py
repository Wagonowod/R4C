from django.urls import path


from .views import RobotAPIView

urlpatterns = [
    path('api/robots/', RobotAPIView.as_view()),
]