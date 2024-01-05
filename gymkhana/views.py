from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import meeting,ugSenator,pgSenator,facultyExecutivebodie,studentExecutivebodie,upcomingEvent

from rest_framework.decorators import api_view

def home(request):
    faculty=facultyExecutivebodie.objects.all()
    student=studentExecutivebodie.objects.all()
    return render(request,'main/home.html',{'response':faculty,'response1':student})
    



def Senate(request):
    ugsenator=ugSenator.objects.all()
    pgsenator=pgSenator.objects.all()
    return render(request,'main/senate.html',{'res2':ugsenator,'response3':pgsenator})


def minutes(request):
    meetings=meeting.objects.all()
    return render(request,'main/minutes.html',{'res3':meetings})


