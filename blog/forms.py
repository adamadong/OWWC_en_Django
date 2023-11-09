from django import forms
from .models import Team, Equipment

class MoveForm(forms.ModelForm):
    class Meta:
        model = Team
        field = ['place']