from django.urls import path
from . import views
baseurl = "gymkhana/"
urlpatterns = [
    path(baseurl+'', views.home, name = 'home-page'),
    path('stud/'+baseurl+'senate/',views.Senate,name='senate-page'),
    path('stud/'+baseurl+'minutes/',views.minutes,name='minutes-page'),
    path('stud/'+baseurl+'powersenate/',views.powersenate,name='powersenate'),
    path('stud/'+baseurl+'vpmessage/',views.vpmessage,name='vpmessage'),
  
]
