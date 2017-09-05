import os
from django.core.mail import send_mail
from django.http import HttpResponse
import json


def feedback(request):
    messageObj = json.loads(request.body.decode('utf-8'))
    message = messageObj['email'] + '\n' + messageObj['message']
    send_mail(subject='Trouble in paradise!',
              message=message, from_email=os.environ.get('OLIMP_EMAIL_HOST_USER'),
              recipient_list=['subher0@mail.ru'])

    return HttpResponse(message)