from django.urls import path
from .views import TCAPIView

urlpatterns = [
    path('', TCAPIView.as_view()),
    path('<str:pk>', TCAPIView.as_view()) # to capture our ids
]