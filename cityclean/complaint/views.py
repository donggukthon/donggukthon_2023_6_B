from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Trash
from .serializers import TrashListSerializer, TrashSerializer

class TrashCreateView(APIView):

    def post(self, request):
        data = request.data
        serializer = TrashSerializer(data=data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class TrashsView(APIView):
    def get(self, request):
        user_latitude = float(request.query_params.get('latitude', 0))
        user_longitude = float(request.query_params.get('longitude', 0))
        user_location = Point(user_longitude, user_latitude)

        # 반경 내의 쓰레기 필터링
        trash_queryset = Trash.objects.all()
        trash_in_radius = [
            trash for trash in trash_queryset
            if self.is_in_radius(user_location, (trash.latitude, trash.longitude), radius_km=3)
        ]

        serializer = TrashListSerializer(trash_in_radius, many=True)
        return Response(serializer.data)

    def is_in_radius(self, location1, location2, radius_km):
        distance = geodesic(location1, location2).kilometers
        return distance <= radius_km