from django.shortcuts import render
from .forms import FeedbackForm


def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'feedback_form/thanks.html')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form/feedback_form.html', {'feedback': form})
