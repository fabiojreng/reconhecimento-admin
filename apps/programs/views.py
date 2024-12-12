from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Program
from .forms import ProgramForm


class ProgramListView(ListView):
    model = Program
    template_name = "program_list.html"
    context_object_name = "programs"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        program_name = self.request.GET.get("name")

        if program_name:
            queryset = queryset.filter(name__icontains=program_name)

        return queryset


class ProgramCreateView(CreateView):
    model = Program
    template_name = "program_create.html"
    form_class = ProgramForm
    success_url = reverse_lazy("program_list")


class ProgramDetailView(DetailView):
    model = Program
    template_name = "program_detail.html"


class ProgramUpdateView(UpdateView):
    model = Program
    template_name = "program_update.html"
    form_class = ProgramForm
    success_url = reverse_lazy("program_list")


class ProgramDeleteView(DeleteView):
    model = Program
    template_name = "program_delete.html"
    success_url = reverse_lazy("program_list")
