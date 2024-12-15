from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Administrator
from .forms import AdminForm, GroupForm
from django.contrib.auth.models import Group, Permission


class AdminListView(ListView):
    model = Administrator
    template_name = "admin_list.html"
    context_object_name = "administrators"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name")

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class AdminCreateView(CreateView):
    model = Administrator
    template_name = "admin_create.html"
    form_class = AdminForm
    success_url = reverse_lazy("admin_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["groups"] = Group.objects.all()
        context["permissions"] = Permission.objects.all()
        return context


class AdminDetailView(DetailView):
    model = Administrator
    template_name = "admin_detail.html"
    context_object_name = "admin"


class AdminUpdateView(UpdateView):
    model = Administrator
    template_name = "admin_update.html"
    form_class = AdminForm
    success_url = reverse_lazy("admin_list")
    context_object_name = "admin"


class AdminDeleteView(DeleteView):
    model = Administrator
    template_name = "admin_delete.html"
    success_url = reverse_lazy("admin_list")
    context_object_name = "admin"


class GroupListView(ListView):
    model = Group
    template_name = "group_list.html"
    context_object_name = "groups"


class GroupCreateView(CreateView):
    model = Group
    template_name = "group_create.html"
    form_class = GroupForm
    success_url = reverse_lazy("group_list")


class GroupUpdateView(UpdateView):
    model = Group
    template_name = "group_update.html"
    form_class = GroupForm
    success_url = reverse_lazy("group_list")
