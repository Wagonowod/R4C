from django.urls import path

from robots.views import ReportViewSet

urlpatterns = [
    path('report/', ReportViewSet.as_view()),
]
