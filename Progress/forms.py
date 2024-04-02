# forms.py

from django import forms
from WEB.models import Task, TaskCategory


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['time', 'description', 'completed', 'category']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['time'].widget = forms.TimeInput(attrs={'type': 'time'})

