from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Post


class newPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'status',
        ]
        labels = {
            'title': _('Title'),
            'text': _('Text'),
            'status': _('Status'),
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Enter post title')}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 8, 'placeholder': _('Enter post text')}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
