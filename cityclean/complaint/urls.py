from django.urls import path
from .views import TrashCreateView, TrashsView

urlpatterns = [
    path('create/', TrashCreateView.as_view(), name='create-trash'),
    path('trashs/', TrashsView.as_view(), name='trashs-list'),
]