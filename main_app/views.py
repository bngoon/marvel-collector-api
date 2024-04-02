from rest_framework.views import APIView
from rest_framework.response import Response


from rest_framework import generics
from .models import Character
from .serializers import CharacterSerializer
# Define the home view


class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to the marvel-collector api home route!'}
        return Response(content)


class CharacterList(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class CharacterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    lookup_field = 'id'
