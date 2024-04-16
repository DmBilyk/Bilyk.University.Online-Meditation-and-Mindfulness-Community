from .models import Task
from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'time', 'date', 'link']

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['time'].widget = forms.TimeInput(attrs={'type': 'time'})
        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['time', 'description', 'completed', 'category']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['time'].widget = forms.TimeInput(attrs={'type': 'time'})
