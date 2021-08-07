from django import forms
from app.models import FileUpload


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['title', 'image']