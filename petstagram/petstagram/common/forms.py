from django import forms

from petstagram.common.models import Comment


class CommentForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control rounded-2',
            },
        ),
    )