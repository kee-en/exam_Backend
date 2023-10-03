from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GenderChoiceViewSet, TokenCreateView

router = DefaultRouter()
router.register(r"gender-choices", GenderChoiceViewSet)

urlpatterns = [
    path("api/token/", TokenCreateView.as_view(), name="token-create"),
    path("", include(router.urls)),
]
