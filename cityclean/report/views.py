from rest_framework.views import APIView
from rest_framework.response import Response
from .models import trashCans
from .serializers import TrashCanSerializer, TrashCanListSerializer

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
        trash_cans_queryset = trashCans.objects.all()
        serializer = TrashCanListSerializer(trash_cans_queryset, many=True)
        return Response(serializer.data)
