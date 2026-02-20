from django.shortcuts import get_object_or_404, redirect
from django.template.base import kwarg_re
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from contractors.forms import ContractorCreateForm, ContractorEditForm, ContractorDeleteForm
from contractors.models import Contractor


class ContractorListView(ListView):
    model = Contractor
    template_name = 'contractors/contractor_list.html'
    context_object_name = 'contractors'
    paginate_by = 4

    def get_queryset(self):
        return super().get_queryset().select_related('city').prefetch_related('skills')


class ContractorDetailView(DetailView):
    model = Contractor
    template_name = 'contractors/contractor_detail.html'
    context_object_name = 'contractor'

    def get_queryset(self):
        return super().get_queryset().select_related('city').prefetch_related('skills', 'applications')


class ContractorCreateView(CreateView):
    model = Contractor
    template_name = 'contractors/contractor_create.html'
    form_class = ContractorCreateForm
    success_url = reverse_lazy('contractors:list')


class ContractorUpdateView(UpdateView):
    model = Contractor
    form_class = ContractorEditForm
    template_name = 'contractors/contractor_edit.html'

    def get_success_url(self):
        return reverse_lazy('contractors:detail', kwargs={'pk': self.object.pk})

    def get_queryset(self):
        return super().get_queryset().select_related('city').prefetch_related('skills')


class ContractorDeleteView(DeleteView):
    model = Contractor
    form_class = ContractorDeleteForm
    template_name = 'contractors/contractor_delete.html'
    success_url = reverse_lazy('contractors:list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = get_object_or_404(Contractor, pk=self.kwargs['pk'])

        return kwargs


    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)


