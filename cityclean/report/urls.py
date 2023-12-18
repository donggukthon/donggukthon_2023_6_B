from django.urls import path
from .views import TrashCanCreateView

urlpatterns = [
    path('create/', TrashCanCreateView.as_view(), name='create-trashcan'),
]