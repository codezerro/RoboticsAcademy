from rest_framework import viewsets
from rest_framework import permissions

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from academy.academy_rest_api.serializers.exercises import ExerciseSerializer
from exercises.models import Exercise


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class ExerciseViewSet2(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # No authentication required

    def get(self, request):
        # This will return a JSON response with `{"name": "hello"}`
        return Response({"name": "hello"})
    def post(self, request):
        # Extract data from the request (e.g., `name` from the body)
        name = request.data.get("name", None)
        
        if name:
            # Return a response with the received data
            return Response({"message": f"Hello, {name}!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Name not provided"}, status=status.HTTP_400_BAD_REQUEST)
