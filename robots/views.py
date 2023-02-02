from drf_excel.mixins import XLSXFileMixin
from drf_excel.renderers import XLSXRenderer
from rest_framework.viewsets import ReadOnlyModelViewSet

# Create your views here.

from .models import Robot
from .serializers import RobotSerializer


class ReportViewSet(XLSXFileMixin, ReadOnlyModelViewSet):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer
    renderer_classes = [XLSXRenderer]
    filename = 'Production_report.xlsx'
