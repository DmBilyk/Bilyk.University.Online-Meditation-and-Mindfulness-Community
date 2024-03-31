from django import forms
from WEB.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['time', 'description', 'completed']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['time'].widget = forms.TimeInput(attrs={'type': 'time'})
