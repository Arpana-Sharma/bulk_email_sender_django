from django.shortcuts import render

from .forms import BulkEmailForm
from .tasks import send_bulk_email


def send_emails(request):

    batch_size = 50
    if request.method == 'POST':
        form = BulkEmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipients = [email.strip() for email in form.cleaned_data['recipients'].split(',')]
            for i in range(0, len(recipients), batch_size):
                batch_recipients = recipients[i:i + batch_size]
                success = send_bulk_email(subject, message, batch_recipients)
                if success:
                    print(f"Successfully sent to {len(batch_recipients)} recipients.")
                else:
                    print(f"Failed to send to {len(batch_recipients)} recipients.")
            return render(request, 'success.html')
    else:
        form = BulkEmailForm()

    return render(request, 'send_email.html', {'form': form})
