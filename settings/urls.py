from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GenderChoiceViewSet

router = DefaultRouter()
router.register(r'gender-choices', GenderChoiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]