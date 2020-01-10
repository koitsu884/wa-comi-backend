from django.urls import include,path
from common.api import views


urlpatterns = [
    path("areas/", views.AreaListViewSet.as_view({'get':'list'}), name="area_list"),
    path("categories/", views.CategoryViewSet.as_view({'get':'list'}), name="category-list"),
]