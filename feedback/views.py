from django.shortcuts import render

from .forms import FeedbackForm


def feedback_form(request):
    """
     Handles the feedback form request.

     If the request method is POST, it validates the form and saves it if it's valid.
     If the request method is not POST, it initializes an empty form.

     Args:
         request (HttpRequest): The request object.

     Returns:
         HttpResponse: The response object. Renders the 'thanks' page if the form is valid and saved,
         otherwise renders the feedback form page.
     """
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'feedback_form/thanks.html')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form/feedback_form.html', {'feedback': form})
