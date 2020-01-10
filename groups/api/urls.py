from django.urls import include, path
from rest_framework.routers import DefaultRouter

from groups.api import views

router = DefaultRouter()
router.register(r"groups", views.GroupViewSet)

urlpatterns = [
    path("", include(router.urls))
]

