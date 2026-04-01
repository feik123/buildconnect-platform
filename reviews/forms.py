from django import forms

from reviews.models import Review


class ReviewCreateForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['rating', 'comment']

        widgets = {
            'comment': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Write your comment about the contractor'
            })
        }