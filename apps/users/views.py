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
from apps.logs.models import RecognitionLog
from datetime import datetime
import locale


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        recognition_logs = RecognitionLog.objects.filter(user_id=self.object)

        formatted_logs = []
        locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")

        for log in recognition_logs:
            formatted_logs.append(
                {
                    "data": log.access_time.date(),
                    "dia_semana": log.access_time.strftime("%A"),
                    "hora": log.access_time.strftime("%H:%M:%S"),
                    "status": log.status,
                }
            )

        context["recognition_logs"] = formatted_logs

        return context


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
