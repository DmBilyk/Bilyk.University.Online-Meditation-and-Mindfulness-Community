from django import forms
from .models import Profile


#Profile form for editing
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['age', 'country', 'bio','level']