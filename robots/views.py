from rest_framework.views import APIView
from rest_framework.response import Response

from robots.serializers import RobotSerializer


# Create your views here.


class RobotAPIView(APIView):
    def post(self, request):
        serializer = RobotSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})
