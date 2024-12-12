from django.urls import path
from . import views

urlpatterns = [
    path("programs/list/", views.ProgramListView.as_view(), name="program_list"),
    path("programs/create/", views.ProgramCreateView.as_view(), name="program_create"),
    path(
        "programs/<uuid:pk>/detail/",
        views.ProgramDetailView.as_view(),
        name="program_detail",
    ),
    path(
        "programs/<uuid:pk>/update/",
        views.ProgramUpdateView.as_view(),
        name="program_update",
    ),
    path(
        "programs/<uuid:pk>/delete/",
        views.ProgramDeleteView.as_view(),
        name="program_delete",
    ),
]
