from django import forms
from .models import Team, Equipment

class MoveForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['place']


class SelectForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['Country']