from django.urls import path
from .views import SnackListView, SnackDetailView, SnackCreateView, SnackDeleteView

urlpatterns = [
    path('',SnackListView.as_view(),name='snacks/snack-list'),
    path('<int:pk>/',SnackDetailView.as_view(),name='snacks/snack-detail'),
    path('create/',SnackCreateView.as_view(),name='snacks/snack-create'),
    path('<int:pk>/delete/', SnackDeleteView.as_view(),name='snacks/snack-delete')
]