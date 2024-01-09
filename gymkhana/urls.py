from django.urls import path
from . import views
baseurl = "gymkhana_2024/"
urlpatterns = [
    path(baseurl+'', views.home, name = 'home-page'),
    path(baseurl+'senate/',views.Senate,name='senate-page'),
    path(baseurl+'minutes/',views.minutes,name='minutes-page'),
    path(baseurl+'powersenate/',views.powersenate,name='powersenate'),
    path(baseurl+'vpmessage/',views.vpmessage,name='vpmessage'),
  
]