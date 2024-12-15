from django.urls import path
from . import views

urlpatterns = [
    path("admins/list/", views.AdminListView.as_view(), name="admin_list"),
    path("admins/create/", views.AdminCreateView.as_view(), name="admin_create"),
    path(
        "admins/<uuid:pk>/detail/", views.AdminDetailView.as_view(), name="admin_detail"
    ),
    path(
        "admins/<uuid:pk>/update/", views.AdminUpdateView.as_view(), name="admin_update"
    ),
    path(
        "admins/<uuid:pk>/delete/", views.AdminDeleteView.as_view(), name="admin_delete"
    ),
    path("group/create/", views.GroupCreateView.as_view(), name="group_create"),
    path(
        "group/update/<int:pk>/", views.GroupUpdateView.as_view(), name="group_update"
    ),
    path("group/list/", views.GroupListView.as_view(), name="group_list"),
]
