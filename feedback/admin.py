from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from .models import Product, Feedback
from django import forms


class FeedbackAdminForm(forms.ModelForm):
    response_message = forms.CharField(label="Response Message", widget=forms.Textarea)

    class Meta:
        model = Feedback
        fields = '__all__'


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer_name', 'date', 'happy',)
    list_filter = ('product', 'date',)
    search_fields = ('product__name', 'details',)
    form = FeedbackAdminForm

    def respond_to_feedback(self, request, queryset):
        for feedback in queryset:
            response_message = feedback.response_message  # Get the response message from the form
            if response_message.strip():  # Check if response message is not empty or whitespace only
                subject = f"Response to your feedback for {feedback.product.name}"
                sender_email = settings.EMAIL_HOST_USER
                recipient_email = feedback.email
                send_mail(subject, response_message, sender_email, [recipient_email])
            else:
                self.message_user(request,
                                  f"Skipping email response for {feedback.customer_name} as message was empty.")
        self.message_user(request, "Emails sent successfully.")

    respond_to_feedback.short_description = "Respond to selected feedback"

    actions = ['respond_to_feedback']

admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Product)
