from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import meeting,ugSenator,pgSenator,facultyExecutivebodie,studentExecutivebodie,upcomingEvent

# from rest_framework.decorators import api_view

def home(request):
    faculty=facultyExecutivebodie.objects.all()
    student=studentExecutivebodie.objects.all()
    events=upcomingEvent.objects.all()
    return render(request,'main/home.html',{'faculty':faculty,'student':student,'events':events})
    



def Senate(request):
    ugsenator=ugSenator.objects.all()
    pgsenator=pgSenator.objects.all()
    return render(request,'main/senate.html',{'ugsenator':ugsenator,'pgsenator':pgsenator})


def minutes(request):
    meetings=meeting.objects.all()
    return render(request,'main/minutes.html',{'meetings':meetings})


