from django import forms
from .models import Datafile



class UploadForm(forms.ModelForm):
    class Meta:
        model = Datafile
        fields = ('description', 'csvfile', )
        widgets = {
            'csvfile': forms.ClearableFileInput(attrs={'multiple': True})
        }

class CsvProcessSettingsForm(forms.Form):
    rowsToSkip = forms.IntegerField()
    dayfirst = forms.BooleanField()




