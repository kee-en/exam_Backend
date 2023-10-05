from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherProfileViewSet

router = DefaultRouter()
router.register(r"profiles", TeacherProfileViewSet)
router.register(
    r"profile-create", TeacherProfileViewSet, basename="teacherprofile-create"
)

urlpatterns = [
    path("", include(router.urls)),
    ]
