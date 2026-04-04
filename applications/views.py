from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView

from applications.forms import ApplicationCreateForm
from applications.models import Application
from jobs.models import Job
from .tasks import notify_application_accepted


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


def accept_application(request, pk):
    application = get_object_or_404(Application, pk=pk)

    if application.contractor != request.user:
        raise PermissionDenied('Not allowed')

    application.status = Application.ApplicationChoices.ACCEPTED
    application.save(update_fields=['status'])

    job = application.job
    job.status = job.StatusChoices.CLOSE
    job.save()

    notify_application_accepted.delay(
        application.contractor.name,
        job.title
    )

    return redirect('jobs:detail', pk=job.pk)

def reject_application(request, pk):
    application = get_object_or_404(Application, pk=pk)

    application.status = Application.ApplicationChoices.REJECTED
    application.save()

    return redirect('jobs:detail', pk=application.job.pk)

