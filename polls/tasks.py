from celery.decorators import task
from celery.utils.log import get_task_logger
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

logger = get_task_logger(__name__)


@task(name="send_feedback_email_task")
def send_feedback_email_task(email, message):
    """sends an email when feedback form is filled successfully"""
    logger.info("Sent feedback email")
    return send_feedback_email(email, message)


def send_feedback_email(email, message):
    subject = 'Thank you for registering to our site'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    msg_plain = render_to_string('email/email.txt', {'name': email})
    msg_html = render_to_string('email/email.html', {'name': email})
    send_mail(subject, msg_plain, email_from, recipient_list, html_message=msg_html)
