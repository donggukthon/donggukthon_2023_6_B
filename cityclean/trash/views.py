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
        trash_queryset = Trash.objects.all()
        serializer = TrashListSerializer(trash_queryset, many=True)
        return Response(serializer.data)