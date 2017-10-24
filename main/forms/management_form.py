from django import forms


class ManagementForm(forms.Form):
    university = forms.IntegerField(label='university')
    auditory = forms.IntegerField(label='auditory')
    type = forms.IntegerField(label='type')
    subject = forms.IntegerField(label='subject')

    date = forms.CharField(label='date', max_length=30)
    title = forms.CharField(label='phone', max_length=100)
    location = forms.CharField(label='school', max_length=1000)
    description = forms.CharField(label='grade', max_length=10000)
    maximumCapacity = forms.IntegerField(label='eventId')


class LoginForm(forms.Form):
    login = forms.CharField(label='login', max_length=30)
    password = forms.CharField(label='password', max_length=100)