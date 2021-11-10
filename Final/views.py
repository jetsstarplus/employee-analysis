from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.sessions.models import Session
import datetime
from django.core.files import File


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
    return render(request, 'index/index.html')

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
                instance=form.save()
            except:
                return HttpResponseRedirect('/failed/')

            else:
                scanned_text=textExtract.pdfFileScan(instance.file.url, instance.name)
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
            return HttpResponseRedirect('/failed/')

    else:
        form = PdfForm()
        context = {'form': form}
        return render(request, 'Final/pdfForm.html', context)

@login_required(login_url='/login/')
def details(request, person_id):
    person = get_object_or_404(Resume_Information, pk=person_id)
    specifics=eval(person.pdf_text)
    sessions = Session.objects.all().count()
    total = Resumes.objects.all().count()
    application = Resume_Information.objects.all().order_by('-date_pub')
    new = Resume_Information.objects.filter(status=False).all().count()


    context={
        'person':person,
        'specifics':specifics,
        'application': application,
        'total': total,
        'sessions': sessions,
        'new': new
    }
    return render(request, 'Final/detail.html', context)


# def pdfShow(request, url):
#     pdf
#
# def downloadPdf(request, applicant_id):
#     file_path=Resume_Information.objects.get(pk=applicant_id)
#     path=file_path.owner.file.url
#
#     f1=open(path, 'r')
