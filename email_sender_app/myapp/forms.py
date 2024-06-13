from django import forms


class BulkEmailForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    recipients = forms.CharField(widget=forms.Textarea, help_text="Enter comma-separated email addresses.")

