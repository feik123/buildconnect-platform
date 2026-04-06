from django import forms
from django.core.exceptions import ValidationError

from applications.models import Application
from reviews.models import Review


class ReviewCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.contractor = kwargs.pop('contractor', None)
        self.user = kwargs.pop('user', None)

        super().__init__(*args, **kwargs)


    def clean(self):
        cleaned_data = super().clean()

        if not Application.objects.filter(
                contractor=self.contractor,
                job__owner=self.user,
                status='accepted'
        ).exists():
            raise ValidationError("You can only review contractors you worked with")

        if Review.objects.filter(
                contractor=self.contractor,
                user=self.user
        ).exists():
            raise ValidationError("You have already reviewed this contractor")

        return cleaned_data

    class Meta:
        model = Review
        fields = ['rating', 'comment']

        widgets = {
            'comment': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Write your comment about the contractor'
            })
        }