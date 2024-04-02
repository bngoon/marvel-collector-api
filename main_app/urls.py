from django.urls import path
from .views import Home, CharacterList, CharacterDetail

urlpatterns = [
    path('', Home.as_view(), name='home'),
    # new routes below
    path('chracters/', CharacterList.as_view(), name='character-list'),
    path('chracters/<int:id>/', CharacterDetail.as_view(), name='chracter-detail'),
]
