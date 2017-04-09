from django import forms
from .models import Candidate

class ShowProfiles(forms.Form):

    candidate_name = forms.ModelChoiceField(queryset=Candidate.objects.all())