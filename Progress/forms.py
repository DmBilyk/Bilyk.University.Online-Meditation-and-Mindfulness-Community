# forms.py

from django import forms
from .models import Task, WeeklyChallenge

from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'completed']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['placeholder'] = 'Enter task description'


class WeeklyChallengeForm(forms.ModelForm):
    class Meta:
        model = WeeklyChallenge
        fields = ['start_date', 'end_date']  # Adjust fields as needed

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        # Add custom validation logic if needed
        if start_date and end_date and end_date <= start_date:
            raise forms.ValidationError("End date must be after start date.")
