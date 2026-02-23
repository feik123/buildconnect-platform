from django.shortcuts import render
from django.views.generic import TemplateView

from contractors.models import Contractor
from jobs.models import Job


class StatusChoices:
    pass


class HomeView(TemplateView):
    template_name = 'common/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['latest_jobs'] = Job.objects.filter(
            status=Job.StatusChoices.OPEN
        )[:3]

        context['top_contractors'] = Contractor.objects.order_by(
            '-years_experience'
        )[:3]

        return context