from django import forms
from django.core.exceptions import ValidationError

from BuildConnect.asgi import application
from applications.models import Application


class ApplicationBaseForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['job', 'contractor', 'message',]

        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['job'].empty_label = 'Select job'
        self.fields['contractor'].empty_label = 'Select contractor'

        self.fields['message'].widget.attrs['placeholder'] = 'Describe why you are suitable for this job...'


class ApplicationCreateForm(ApplicationBaseForm):

    def clean(self):
        cleaned_data = super().clean()

        job = cleaned_data.get('job')
        contractor = cleaned_data.get('contractor')

        if not job and not contractor:
            return cleaned_data

        if job.status != job.StatusChoices.OPEN:
            raise ValidationError('Cannot apply to a closed job.')

        already_applied = Application.objects.filter(
            job=job,
            contractor=contractor,
        ).exists()

        if already_applied:
            raise ValidationError('You have already applied for this job.')

        return cleaned_data


class ApplicationDeleteForm(ApplicationBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.disabled = True

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

