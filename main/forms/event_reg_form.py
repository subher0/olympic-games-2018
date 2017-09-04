from django import forms


class EventSignupForm(forms.Form):
    nameField = forms.CharField(label='name', max_length=30)
    emailField = forms.EmailField(label='email', max_length=30)
    phoneField = forms.RegexField(regex=r'^(\+7|8)[\(-]?\d{3}[-\)]?\d{3}-?\d{2}-?\d{2}$', label='phone', max_length=30)
    schoolField = forms.CharField(label='school', max_length=60)
    gradeField = forms.IntegerField(label='grade')
    eventId = forms.IntegerField(label='eventId')


class EventSearchForm(forms.Form):
    university = forms.IntegerField(label='university')
    auditory = forms.IntegerField(label='auditory')
