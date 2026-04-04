from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from jobs.forms import JobCreateForm, JobDeleteForm, JobEditForm
from jobs.models import Job


class JobListView(ListView):
    model = Job
    context_object_name = 'jobs'
    template_name = 'jobs/job_list.html'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()

        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query)
                |
                Q(description__icontains=query)
            )

        return queryset.select_related(
            'city',
            'category'
        )


class JobCreateView(LoginRequiredMixin,CreateView):
    model = Job
    form_class = JobCreateForm
    template_name = 'jobs/job_create.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['applications'] = self.object.applications.all()

        return context

class JobUpdateView(UpdateView):
    model = Job
    form_class = JobEditForm
    template_name = 'jobs/job_edit.html'
    success_url = reverse_lazy('jobs:list')


class JobDeleteView(DeleteView):
    model = Job
    form_class = JobDeleteForm
    context_object_name = 'job'
    template_name = 'jobs/job_delete.html'
    success_url = reverse_lazy('jobs:list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = get_object_or_404(Job, pk=self.kwargs['pk'])

        return kwargs


