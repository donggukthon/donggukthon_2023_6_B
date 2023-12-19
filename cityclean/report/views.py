from rest_framework.views import APIView
from rest_framework.response import Response
from .models import trashCans
from .serializers import TrashCanSerializer, TrashCanListSerializer, TrashCansListSerializer

class TrashCanCreateView(APIView):

    def post(self, request):
        data = request.data
        serializer = TrashCanSerializer(data=data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class TrashCanListView(APIView):
    def get(self, request):
        # 유저 1이 작성한 쓰레기통만 필터링
        trash_cans_queryset = trashCans.objects.filter(user=1)
        serializer = TrashCanListSerializer(trash_cans_queryset, many=True)
        return Response(serializer.data)

class TrashCansView(APIView):
    def get(self, request):
        user_latitude = float(request.query_params.get('latitude', 0))
        user_longitude = float(request.query_params.get('longitude', 0))
        user_location = (user_latitude, user_longitude)

        # 반경 내의 쓰레기통 필터링
        trash_cans_queryset = trashCans.objects.all()
        trash_cans_in_radius = [
            trash_can for trash_can in trash_cans_queryset
            if self.is_in_radius(user_location, (trash_can.latitude, trash_can.longitude), radius_km=3)
        ]

        serializer = TrashCansListSerializer(trash_cans_in_radius, many=True)
        return Response(serializer.data)

    def is_in_radius(self, location1, location2, radius_km):
        distance = geodesic(location1, location2).kilometers
        return distance <= radius_km


