import os

import re
from django.core.management import BaseCommand
from django.utils.timezone import datetime, timedelta
from openpyxl import load_workbook

from main.models.projects.university_saturdays import Event, EventType, Auditory
from main.models.university import University


class Command(BaseCommand):
    def addEvents(self, *args, **options):
        try:
            print(os.path.dirname(os.path.realpath(__file__)))
            workbook = load_workbook(
                filename=os.path.dirname(os.path.realpath(__file__)) + '/' + options['file_name'][0], read_only=True)
        except:
            print("File doesn't exist")
            return

        auditories = {}
        types = {}
        universities = {}

        for auditory in Auditory.objects.all():
            auditories[auditory.auditory.lower()] = auditory
        for type in EventType.objects.all():
            types[type.type.lower()] = type
        for university in University.objects.getAllUniversities():
            universities[university.name.lower()] = university

        worksheet = workbook.worksheets[0]
        counter = 0
        date = worksheet['A2'].value - timedelta(days=7)
        timePattern = re.compile('^(\d{2})ч (\d{2}) м')
        universityLocationPattern = re.compile('^(\w+), (.*)')
        maxParticipantsPattern = re.compile('(\d+)')
        for row in worksheet.rows:
            counter += 1
            if counter == 1:
                continue
            date = date + timedelta(days=7)
            timeStr = row[1].value
            if timeStr is None:
                continue
            time = timePattern.search(timeStr)
            date = date.replace(hour=int(time.group(1)), minute=int(time.group(2)))
            universityTitle = universityLocationPattern.search(row[2].value).group(1)
            location = universityLocationPattern.search(row[2].value).group(2)
            eventTitle = row[3].value
            annotation = row[4].value
            eventType = row[5].value
            eventAuditories = re.split(' и |, ', row[6].value)
            maxParticipants = int(maxParticipantsPattern.search(row[7].value).group(1))

            university = {}
            try:
                university = universities[universityTitle.lower()]
            except KeyError:
                university = University(name=universityTitle)
                university.save()
                universities[university.name.lower()] = university

            evTypes = []
            try:
                evTypes.append(types[eventType.lower()])
            except KeyError:
                evType = EventType(type=eventType)
                evType.save()
                types[evType.type.lower()] = evType
                evTypes.append(evType)

            evAuditories = []
            for eventAuditory in eventAuditories:
                try:
                    evAuditories.append(auditories[eventAuditory.lower()])
                except KeyError:
                    auditory = Auditory(auditory=eventAuditory)
                    auditory.save()
                    auditories[auditory.auditory.lower()] = auditory
                    evAuditories.append(auditory)

            Event.objects.createEvent(date=date, title=eventTitle, location=location, description=annotation,
                                      maximumCapacity=maxParticipants, university=university, auditory=evAuditories,
                                      types=evTypes)

    def add_arguments(self, parser):
        parser.add_argument('file_name', nargs='+', type=str)

    def handle(self, *args, **options):
        self.addEvents(*args, **options)
        print('ParsingIsComplete')
