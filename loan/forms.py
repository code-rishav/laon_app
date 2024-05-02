from django import forms
from .models import Profile

class ApplicatioForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ['date','status']