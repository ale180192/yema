from django.core.mail import send_mail
from django.conf import settings
import requests


def send_mail_appointment(to, datetime, pediatrician):
    message = 'Remember that you have an appointment with pediatrician {pediatrician} for the {date} at {time}'.format_map({
            'pediatrician': pediatrician,
            'date': datetime,
            'time': datetime })
    return requests.post(
                        "{mailgun_url}/messages".format_map({'mailgun_url': settings.MAILGUN_API_BASE_URL + '/' + settings.MAILGUN_DOMAIN}),
                        auth=("api", settings.MAILGUN_API_KEY),
                        data={
                            "from": "noreply@sandboxc3b6f01b10144878aae6b0830d2cfe4b.mailgun.org",
                            "to": to,
                            "subject": "Appointment with pediatrician",
                            "text": message})
