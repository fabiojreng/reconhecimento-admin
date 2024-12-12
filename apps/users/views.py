from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import User
from .forms import UserForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class UserListView(ListView):
    model = User
    template_name = "user_list.html"
    context_object_name = "users"
    paginate_by = 10
    permission_required = "users.view_user"

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name")

        if name:
            queryset = queryset.filter(username__icontains=name)

        return queryset


class UserCreateView(CreateView):
    model = User
    template_name = "user_create.html"
    form_class = UserForm
    success_url = reverse_lazy("user_list")
    permission_required = "users.add_user"


class UserDetailView(DetailView):
    model = User
    template_name = "user_detail.html"
    permission_required = "users.view_user"
    # context_object_name = "user"


class UserUpdateView(UpdateView):
    model = User
    template_name = "user_update.html"
    form_class = UserForm
    success_url = reverse_lazy("user_list")
    permission_required = "users.change_user"


class UserDeleteView(DeleteView):
    model = User
    template_name = "user_delete.html"
    success_url = reverse_lazy("user_list")
    permission_required = "users.delete_user"
    # context_object_name = "User"
