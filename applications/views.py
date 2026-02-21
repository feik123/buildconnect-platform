
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from applications.forms import ApplicationCreateForm
from applications.models import Application
from jobs.models import Job


class ApplicationCreateView(CreateView):
    model = Application
    form_class = ApplicationCreateForm
    template_name = 'applications/application_create.html'

    def dispatch(self, request, *args, **kwargs):
        self.job = get_object_or_404(Job, pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['job'] = self.job
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job'] = self.job
        return context

    def form_valid(self, form):
        form.instance.job = self.job
        return super().form_valid(form)


    def get_success_url(self):
        return reverse_lazy('jobs:detail', kwargs={'pk': self.job.pk})