from django.urls import path
from . import views

urlpatterns = [
    path("users/list/", views.UserListView.as_view(), name="user_list"),
    path("users/create/", views.UserCreateView.as_view(), name="user_create"),
    path("users/<uuid:pk>/detail/", views.UserDetailView.as_view(), name="user_detail"),
    path("users/<uuid:pk>/update/", views.UserUpdateView.as_view(), name="user_update"),
    path("users/<uuid:pk>/delete/", views.UserDeleteView.as_view(), name="user_delete"),
]
