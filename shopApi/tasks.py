from django.core.mail import send_mail

from account.models import Spam_Contacts
from account.send_mail import send_confirmation_email, send_notification
from .celery import app


@app.task
def send_confirm_email_task(user, code):
    send_confirmation_email(user, code)


@app.task
def send_notification_task(user_email, order_id, price):
    send_notification(user_email, order_id, price)


@app.task
def send_spam_email():
    ls = [user.email for user in Spam_Contacts.objects.all()]
    send_mail(
        'SPAM',
        'SPAM FROM NURISLAM',
        'test@gmail.com',
        [*ls],
        fail_silently=False
    )
