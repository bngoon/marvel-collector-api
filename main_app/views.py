from rest_framework.views import APIView
from rest_framework.response import Response


from rest_framework import generics
from .models import Character, Condition
from .serializers import CharacterSerializer, ConditionSerializer
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


class ConditionListCreate(generics.ListCreateAPIView):
    serializer_class = ConditionSerializer

    def get_queryset(self):
        character_id = self.kwargs['character_id']
        return Condition.objects.filter(character_id=character_id)

    def perform_create(self, serializer):
        character_id = self.kwargs['character_id']
        character = Character.objects.get(id=character_id)
        serializer.save(character=character)


class ConditionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ConditionSerializer
    lookup_field = 'id'

    def get_queryset(self):
        character_id = self.kwargs['cracter_id']
        return Condition.objects.filter(character_id=character_id)
