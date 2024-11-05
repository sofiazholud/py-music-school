# musician/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MusicianListView,
    MusicianDetailView,
    MusicianCreateView,
    MusicianUpdateView,
    MusicianDeleteView,
    MusicianViewSet
)

app_name = "musician"

router = DefaultRouter()
router.register(
    r"manage",
    MusicianViewSet,
    basename="manage"
)

urlpatterns = [
    path(
        "",
        MusicianListView.as_view(),
        name="musician_list"
    ),
    path(
        "<int:pk>/",
        MusicianDetailView.as_view(),
        name="musician_detail"
    ),
    path(
        "create/",
        MusicianCreateView.as_view(),
        name="musician_create"
    ),
    path(
        "<int:pk>/update/",
        MusicianUpdateView.as_view(),
        name="musician_update"
    ),
    path(
        "<int:pk>/delete/",
        MusicianDeleteView.as_view(),
        name="musician_delete"
    ),
    path(
        "",
        include(router.urls)
    ),
]
