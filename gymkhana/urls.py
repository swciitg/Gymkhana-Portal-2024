from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'home-page'),
    path('senate/',views.Senate,name='senate-page'),
    path('minutes/',views.minutes,name='minutes-page'),
]