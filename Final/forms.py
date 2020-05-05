from django import forms

class PdfForm(forms.Form):
    name = forms.CharField(label = "Name", max_length = 100)
    email = forms.EmailField(label = "Email")
    file = forms.FileField(label = "Upload Resume")
