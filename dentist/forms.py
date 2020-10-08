from django import forms

class contactformemail(forms.Form):
    message_name=forms.EmailField(required=True)
    message_email=forms.CharField(required=True)
    message=forms.CharField(required=True)