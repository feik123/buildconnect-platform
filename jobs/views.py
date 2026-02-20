
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from jobs.forms import JobCreateForm
from jobs.models import Job


class JobListView(ListView):
    model = Job
    context_object_name = 'jobs'
    template_name = 'jobs/job_list.html'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset.select_related(
            'city',
            'category'
        )


class JobCreateView(CreateView):
    model = Job
    form_class = JobCreateForm
    template_name = 'jobs/job_create.html'
    success_url = reverse_lazy('jobs:list')


class JobDetailView(DetailView):
    model = Job
    context_object_name = 'job'
    template_name = 'jobs/job_detail.html'

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset.select_related(
            'city',
            'category'
        ).prefetch_related(
            'applications__contractor'
        )


