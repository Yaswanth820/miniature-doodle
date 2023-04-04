from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LaptopViewSet

router = DefaultRouter()
router.register('laptops', LaptopViewSet)

urlpatterns = [
    path('', include(router.urls)),
]