from django.urls import path, include
from . import views

urlpatterns = [
    path('latest-products/', views.LatestProductAPIView.as_view())
]
