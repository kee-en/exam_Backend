from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentProfileViewSet

router = DefaultRouter()
router.register(r"profiles", StudentProfileViewSet)
router.register(
    r"profile-create", StudentProfileViewSet, basename="studentprofile-create"
)

urlpatterns = [
    path("", include(router.urls)),
]
