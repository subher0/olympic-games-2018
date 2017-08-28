from django.contrib import admin

from main.models import Tagline, Partner, Chump, Article, Pupil, News, Project, FamousOne
from main.models.projects.university_saturdays import Event, Auditory, Subject, EventType
from main.models.university import University

admin.site.register(Article)
admin.site.register(Pupil)
admin.site.register(News)
admin.site.register(Project)
admin.site.register(Tagline)
admin.site.register(Partner)
admin.site.register(Chump)
admin.site.register(FamousOne)
admin.site.register(University)
admin.site.register(Event)
admin.site.register(EventType)
admin.site.register(Subject)
admin.site.register(Auditory)