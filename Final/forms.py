from django import forms
from .models import Resumes

class PdfForm(forms.ModelForm):
    class Meta:
        model=Resumes
        exclude=("date_pub", )

        widgets = {'file': forms.FileInput(
            attrs={
                'accept': 'application/pdf, application/vnd.openxmlformats-officedocument.wordprocessingml.document, application/msword'})}

    # name = forms.CharField(label = "Name", max_length = 100)
    # email = forms.EmailField(label = "Email")
    # file = forms.FileField(label = "Upload Resume")
