from django.urls import path

from robots.views import ReportViewSet

urlpatterns = [
    path('api/report/', ReportViewSet.as_view()),
]
