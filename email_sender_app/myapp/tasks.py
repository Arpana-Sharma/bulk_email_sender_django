# utils.py (or any suitable module)

from django.core.mail import send_mail
from django.conf import settings


def send_bulk_email(subject, message, recipient_list):
    try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            recipient_list,
            fail_silently=False,  # Set to True to suppress errors (not recommended)
        )
        return True
    except Exception as e:
        # Handle exceptions (e.g., logging, retry mechanism)
        print(f"Failed to send email: {e}")
        return False
