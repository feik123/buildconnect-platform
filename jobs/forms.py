from dataclasses import fields

from django import forms
from django.core.exceptions import ValidationError

from jobs.models import Job


class JobBaseForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'category', 'city', 'budget', 'status']
        widgets = {
            'description': forms.Textarea()
        }
        error_messages = {
            'title': {
                'required': 'Please enter job title.'
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['placeholder'] = 'Job title'
        self.fields['description'].widget.attrs['placeholder'] = 'Describe the job in detail...'
        self.fields['category'].empty_label = 'Select category'
        self.fields['city'].empty_label = 'Select city'
        self.fields['budget'].widget.attrs['placeholder'] = 'e.g. 2000'

    def clean_budget(self):
        budget = self.cleaned_data.get('budget')

        if budget is not None and  budget < 0:
           raise ValidationError('Budget cannot be negative.')

        return budget


class JobCreateForm(JobBaseForm):
    pass


class JobEditForm(JobBaseForm):
    pass


class JobDeleteForm(JobBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.disabled = True

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
