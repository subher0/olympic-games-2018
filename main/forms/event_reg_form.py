from django import forms


class EventSignupForm(forms.Form):
    nameField = forms.CharField(label='name', max_length=50)
    emailField = forms.CharField(label='email', max_length=50)
    phoneField = forms.CharField(label='phone', max_length=50)
    schoolField = forms.CharField(label='school', max_length=60)
    gradeField = forms.CharField(label='grade', max_length=50)
    eventId = forms.CharField(label='eventId', max_length=50)


class EventSearchForm(forms.Form):
    university = forms.IntegerField(label='university')
