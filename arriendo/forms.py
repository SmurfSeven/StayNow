#from typing_extensions import Required
from django import forms
from django.forms.fields import ChoiceField
from django.contrib.auth.forms import UserCreationForm
#from django.views.generic.list import T

class AvailabilityForm(forms.Form):
    check_in =  forms.DateTimeField(required=True, input_formats=["%Y -%m -%dT%H:%M",]) #'%m/%d/%Y'
    check_out = forms.DateTimeField(required=True, input_formats=["%Y -%m -%dT%H:%M",]) # "%Y -%m -%dT%H:%M"

class CustomCreationForm(UserCreationForm):
    pass