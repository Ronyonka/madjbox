from django import forms
from .models import Files


class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=50)
    uploaded_file = forms.FileField()

    class Meta:
        model = File
        fields = ('name','uploaded_file',)