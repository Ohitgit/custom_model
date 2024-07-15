from .models import *
from django import forms
# from captcha.fields import ReCaptchaField
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox 
class StudentFrom(forms.Form):
     
    name = forms.CharField(max_length=100)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)  
   