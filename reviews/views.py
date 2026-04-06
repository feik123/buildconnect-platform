
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from contractors.models import Contractor
from reviews.forms import ReviewCreateForm
from reviews.models import Review


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewCreateForm
    template_name = 'reviews/review_create.html'

    def dispatch(self, request, *args, **kwargs):

        self.contractor = get_object_or_404(
            Contractor, pk=self.kwargs['pk']
        )

        if request.user.profile.is_contractor:
            raise PermissionDenied('Contractors cannot leave reviews')

        print(request.user.profile.is_contractor)

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.contractor = self.contractor
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            'contractors:detail',
            kwargs={'pk': self.contractor.pk}
        )

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['contractor'] = self.contractor
        kwargs['user'] = self.request.user
        return kwargs

