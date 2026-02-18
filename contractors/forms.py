from django import forms
from django.core.exceptions import ValidationError

from contractors.models import Contractor


class ContractorBaseForm(forms.ModelForm):
    class Meta:
        model = Contractor
        fields = ['name', 'description', 'city', 'skills','years_experience', ]
        widgets = {
            'description': forms.Textarea(),
            'skills': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].label = 'Contractor Name'
        self.fields['name'].widget.attrs['placeholder'] = 'Ivan Ivanov'

        self.fields['description'].label = 'Description'
        self.fields['description'].widget.attrs['placeholder'] = 'Describe your experience and services...'

        self.fields['city'].label = 'Select city'

        self.fields['skills'].label = 'Skills'

        self.fields['years_experience'].label = 'Years of Experience'
        self.fields['years_experience'].widget.attrs['placeholder'] = 'e.g. 5'

    def clean_years_of_experience(self):
        years = self.cleaned_data.get('years_experience')

        if years < 0:
            raise forms.ValidationError('Years of experience cannot be negative.')

        return years

    def clean_skills(self):
        skills = self.cleaned_data.get('skills')

        if not skills:
            raise ValidationError('Please select at least one skill.')

        return skills


class ContractorCreateForm(ContractorBaseForm):
    pass


class ContractorEditForm(ContractorBaseForm):
    pass


class ContractorDeleteForm(ContractorBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.disabled = True

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance