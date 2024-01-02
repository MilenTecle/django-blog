from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    class Meta:
        """
        Form class for users to request a collaboration
        """
        model = CollaborateRequest
        fields = ('name', 'email', 'message')