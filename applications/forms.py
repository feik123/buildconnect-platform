from django import forms
from django.core.exceptions import ValidationError

from applications.models import Application


class ApplicationBaseForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['contractor', 'message', 'price_quote',]

        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['price_quote'].help_text = 'Enter approximate budget in Euro.'

        self.fields['contractor'].empty_label = 'Select contractor'

        self.fields['message'].widget.attrs['placeholder'] = 'Describe why you are suitable for this job...'


class ApplicationCreateForm(ApplicationBaseForm):

    def __init__(self, *args, **kwargs):
        self.job = kwargs.pop('job', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()


        contractor = cleaned_data.get('contractor')

        if not self.job or not contractor:
            return cleaned_data

        if self.job.status != self.job.StatusChoices.OPEN:
            raise ValidationError('Cannot apply to a closed job.')

        already_applied = Application.objects.filter(
            job=self.job,
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

