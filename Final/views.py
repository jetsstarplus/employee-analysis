from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.sessions.models import Session
import datetime


from .forms import PdfForm
from django.utils import timezone
from .models import Resumes, Resume_Information
from . import textExtract
import pandas as pd
import environ
import time

env=environ.Env(
    SLEEP = (int, 0)
)



@login_required(login_url = '/login/')
def home(request):
    sessions = Session.objects.all().count()
    total = Resumes.objects.all().count()
    application = Resume_Information.objects.all().order_by('-date_pub')
    new = Resume_Information.objects.filter(status=False).all().count()

    context = {
        'application': application,
        'total': total,
        'sessions': sessions,
        'new': new
    }
    return render(request, 'Final/index.html', context)


def index(request):
    return render(request, 'Final/home.html')

# def success(request):
#     return render(request, 'Final/success.html')

def failed(request):
    return render(request, 'Final/failed.html')

def calendar(request):
    return render(request, 'Final/calendar.html')


def get_form(request):
    if request.method == 'POST':
        form = PdfForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                ufile = request.FILES['file']
                uname = request.POST['name']
                umail = request.POST['email']



                instance = Resumes(file=ufile, name=uname, email=umail, date_pub=timezone.now())
                instance.save()
            except:
                return HttpResponseRedirect('/failed/')

            else:
                # Calling the method of scanning the pdf document and outputting the result in a text file using OCR
                time.sleep(env('SLEEP'))
                resume = Resumes.objects.filter(id=instance.id).get()
                # scanned_pdf = PdfScan.pdf(resume.file.url, uname)
                scanned_text=textExtract.pdfFileScan(resume.file.url, uname)
                # scanned_text
                total_score = 0.00
                count=0
                for key, value in dict(scanned_text).items():
                    for value in value.values():
                        total_score+=value
                        count+=1

                mean=(total_score/count)
                instance2 = Resume_Information(owner=instance, pdf_text=scanned_text, rating=mean)

                instance2.save()
                content = Resume_Information.objects.filter(owner=instance).get()
                # df=pd.DataFrame(data=scanned_text)
                # table=df.to_html(classes="table")
                table=dict(scanned_text)
                context = {'content': content, 'table':table}
                return render(request, "Final/success.html", context)

    else:
        form = PdfForm()
        context = {'form': form}
        return render(request, 'Final/pdfForm.html', context)


def details(request, person_id):
    person = get_object_or_404(Resume_Information, pk=person_id)
    specifics=eval(person.pdf_text)
    context={
        'person':person,
        'specifics':specifics
    }
    return render(request, 'Final/detail.html', context)