from django.core.management import BaseCommand
from django.utils.timezone import now

from main.models.projects.university_saturdays import Event
from main.views.projects.university_saturdays import send_email_to_university_and_save


class Command(BaseCommand):
    def check_and_send_due_emails(self):
        events = Event.objects.getFutureEvents()
        for event in events:
            print(event.title)
            if event.date.timestamp() <= now().timestamp() + 60 * 60 * 24 and now().weekday() == 5 and now().hour == 1 and not event.isClosed:
                print(event.isClosed)
                send_email_to_university_and_save(event)

    def handle(self, *args, **options):
        self.check_and_send_due_emails()
        print('Check is complete')
