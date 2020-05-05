from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import PdfForm
from django.utils import timezone
from .models import Resumes
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your views here.

@login_required(login_url = '/login/')
def home(request):
    return render(request, 'Final/index.html')


def index(request):
    return render(request, 'Final/home.html')

def success(request):
    return render(request, 'Final/success.html')

def calendar(request):
    return render(request, 'Final/calendar.html')


def get_form(request):
    if request.method == 'POST':
        form = PdfForm(request.POST, request.FILES)

        if form.is_valid():

            instance = Resumes(file= request.FILES['file'], name = request.POST['name'],  email = request.POST['email'], date_pub = timezone.now())
            instance.save()

            return  HttpResponseRedirect("/success/")

    else:
        form = PdfForm()
        context = {'form':form}
        return render(request, 'Final/pdfForm.html', context)
