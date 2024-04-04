from django.urls import path
from .views import Home, CharacterList, CharacterDetail, ConditionListCreate, ConditionDetail, AddAccessoryToCharacter, RemoveAccessoryFromCharacter

urlpatterns = [
    path('', Home.as_view(), name='home'),
    # new routes below
    path('characters/', CharacterList.as_view(), name='character-list'),
    path('characters/<int:id>/', CharacterDetail.as_view(), name='character-detail'),
    path('characters/<int:character_id>/conditions/',
         ConditionListCreate.as_view(), name='condition-list-create'),

    path('characters/<int:character_id>/conditions/<int:id>/',
         ConditionDetail.as_view(), name='condition-detail'),

    path('characters/int:character_id>/add_accessory/int:accessory_id>/',
         AddAccessoryToCharacter.as_view(), name='add-accessory-to-character'),

    path('characters/int:character_id>/remove_accessory/int:accessory_id>/',
         RemoveAccessoryFromCharacter.as_view(), name='remove-accessory-from-character')
]
