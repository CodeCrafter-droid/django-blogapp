from django import forms
from .models import comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Write your comment...',
                'id': 'comment-input'
            })
        }