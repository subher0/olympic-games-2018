from django.conf.urls import url

from main.views import about_us, feedback
from main.views.projects import chumps_circle, elective, university_saturdays, journey_to_dream, hall_of_fame, \
    smart_and_smarter
from .views import contacts
from .views import index
from .views import news
from .views import olympics

urlpatterns = [
    url(r'^$', index.index_view, name='index'),
    url(r'^feedback$', feedback.feedback, name='feedback'),
    url(r'^news$', news.news_view, name='news'),
    url(r'^olympics$', olympics.olympics_view, name='olympics'),
    url(r'^contacts$', contacts.contacts_view, name='contacts'),
    url(r'^about$', about_us.about_view, name='about'),
    url(r'^projects/chumps_circle$', chumps_circle.chump_circle_view, name='chumps_circle'),
    url(r'^projects/university_saturdays$', university_saturdays.university_saturdays_view,
        name='university_saturdays'),
    url(r'^projects/hall_of_fame$', hall_of_fame.hall_of_fame_view, name='hall_of_fame'),
    url(r'^projects/smart_and_smarter$', smart_and_smarter.smart_view, name='hall_of_fame'),
    url(r'^projects/journey_to_dream$', journey_to_dream.journey_to_dream_view, name='journey_to_dream'),
    url(r'^projects/elective$', elective.elective_view, name='elective'),
    url(r'^projects/university_saturdays/register$', university_saturdays.signup_for_event, name='Sign up for event'),
    url(r'^projects/university_saturdays/search$', university_saturdays.eventSearch, name='Search for event')
]
