import os
from sendgrid import SendGridAPIClient


def send_notification(to_email, subject, body):
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    # Stub: would build and send a message here
    return None
