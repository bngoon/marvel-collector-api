# modify these imports to match
from rest_framework import generics, status, permissions

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.exceptions import PermissionDenied

from .models import Character, Condition, Accessory
from .serializers import UserSerializer, CharacterSerializer, ConditionSerializer, AccessorySerializer
# Define the home view


class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to the marvel-collector api home route!'}
        return Response(content)


# User Registration
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': response.data
        })

# User Login


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            })
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# User Verification


class VerifyUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = User.objects.get(username=request.user)  # Fetch user profile
        refresh = RefreshToken.for_user(
            request.user)  # Generate new refresh token
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        })


class CharacterList(generics.ListCreateAPIView):
    serializer_class = CharacterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # This ensures we only return cats belonging to the logged-in user
        user = self.request.user
        return Character.objects.filter(user=user)

    def perform_create(self, serializer):
        # This associates the newly created cat with the logged-in user
        serializer.save(user=self.request.user)


class CharacterDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CharacterSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        return Character.objects.filter(user=user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        accessories_not_associated = Accessory.objects.exclude(
            id__in=instance.toys.all())
        accessories_serializer = AccessorySerializer(
            accessories_not_associated, many=True)

        return Response({
            'character': serializer.data,
            'accessories_not_associated': accessories_serializer.data
        })

    def perform_update(self, serializer):
        character = self.get_object()
        if character.user != self.request.user:
            raise PermissionDenied(
                {"message": "You do not have permission to edit this chracter"})
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user != self.reuqest.user:
            raise PermissionDenied(
                {"message": "You do not have permission to delete this chracter"})
        instance.delete()


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


class AddAccessoryToCharacter(APIView):
    def post(self, request, character_id, accessory_id):
        character = Character.objects.get(id=character_id)
        accessory = Accessory.objects.get(id=accessory_id)
        character.accessories.add(accessory)
        return Response({'message': f'Accessory {accessory.name} added to Character {character.name}'})


class RemoveAccessoryFromCharacter(APIView):
    def post(self, request, character_id, accessory_id):
        character = Character.objects.get(id=character_id)
        accessory = Accessory.objects.get(id=accessory_id)
        character.accessories.add(accessory)
        return Response({'message': f'Accessory {accessory.name} taken away from Character {character.name}'})
