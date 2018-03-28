from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils.timezone import now

from main.models.university import University
from main.models.utils import make_filepath


class EventManager(models.Manager):
    def createEvent(self, date, title, location, description, maximumCapacity, university, auditory, types):
        if description is None:
            description = ''
        event = Event(date=date, title=title, location=location, description=description,
                      maximumCapacity=maximumCapacity, university=university)
        event.save()
        for auditory_item in auditory:
            event.auditory.add(auditory_item)

        for type in types:
            event.types.add(type)
        event.save()

    def getAllEvents(self):
        try:
            result = self.order_by('isClosed', 'date')
        except Exception:
            result = None
        return result

    def getSomeEvents(self, amount):
        try:
            result = self.order_by('isClosed', 'date')[:amount]
        except Exception:
            result = None
        return result

    def getFutureEvents(self):
        try:
            result = self.filter(date__gte=now())
        except Exception:
            result = None
        return result

    def getById(self, id):
        try:
            result = self.get(id=id)
        except Exception:
            result = None
        return result


class Subject(models.Model):
    subject = models.CharField(verbose_name='Subject', max_length=30)

    def __str__(self):
        return self.subject


class EventType(models.Model):
    type = models.CharField(verbose_name='Event type', max_length=50)

    def __str__(self):
        return self.type


class Auditory(models.Model):
    auditory = models.CharField(verbose_name='Auditory', max_length=30)

    def __str__(self):
        return self.auditory


def event_default():
    res = None
    try:
        res = EventType.objects.first()
    except Exception as e:
        res = EventType(type='Лекция')
        res.save()

    if res is None:
        res = EventType(type='Лекция')
        res.save()

    return res.id


def subject_default():
    res = None
    try:
        res = Subject.objects.first()
    except Exception:
        res = Subject(subject='История')
        res.save()

    if res is None:
        res = Subject(subject='История')
        res.save()

    return res.id


class Event(models.Model):
    old_university = None
    date = models.DateTimeField(verbose_name='Date', default=now)
    title = models.TextField(verbose_name='Title')
    location = models.TextField(verbose_name='Address', max_length=255, default='N/A')
    description = models.TextField(verbose_name='Description', default='', null=True)
    maximumCapacity = models.IntegerField(verbose_name='Maximum capacity')
    currentlyRegistered = models.IntegerField(verbose_name='Currently registered (DON\'T TOUCH THAT!!!, НЕ ТРОГАТЬ!!!)', editable=True, default=0)
    university = models.ForeignKey(University, verbose_name='University', on_delete=models.CASCADE)
    auditory = models.ManyToManyField(Auditory, verbose_name='Auditory')
    types = models.ManyToManyField(EventType, verbose_name='Event type')
    subject = models.ForeignKey(Subject, verbose_name='Subject', default=subject_default, editable=False, on_delete=models.CASCADE)
    isClosed = models.BooleanField(verbose_name='Registration closed', default=False)
    image = models.ImageField(verbose_name='news image', default='no_image.png', upload_to=make_filepath)
    objects = EventManager()

    def __init__(self, *args, **kwargs):
        super(Event, self).__init__(*args, **kwargs)
        try:
            self.old_university = self.university
        except ObjectDoesNotExist:
            self.old_university = None

    def save(self, *args, **kwargs):
        super(Event, self).save(*args, **kwargs)
        university = University.objects.filter(id=self.university.id).get()
        if self.old_university is not None and self.old_university != self.university:
            self.old_university.saturdayRating -= 1
            self.old_university.save()
            university.saturdayRating += 1
        elif self.old_university is None:
            university.saturdayRating += 1
        university.save()

    def __str__(self):
        return self.title
