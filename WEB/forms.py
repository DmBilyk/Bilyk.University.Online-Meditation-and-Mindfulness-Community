from django import forms

from .models import Profile


# Profile feedback for editing
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['age', 'country', 'level', 'bio']
