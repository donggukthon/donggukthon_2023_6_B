from django.urls import path
from .views import TrashCanCreateView, TrashCanListView

urlpatterns = [
    path('create/', TrashCanCreateView.as_view(), name='create-trashcan'),
    path('list/', TrashCanListView.as_view(), name='trashcan-list'),
]