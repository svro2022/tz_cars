from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CargoViewSet, LocationViewSet, CarViewSet, CargoList, CargoDetail

router = DefaultRouter()
router.register('cargo', CargoViewSet)
router.register('location', LocationViewSet)
router.register('car', CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('list-cargo/', CargoList.as_view(), name='cargo-list'),
    path('detail-cargo/<int:pk>/', CargoDetail.as_view(), name='cargo-detail'),
]
