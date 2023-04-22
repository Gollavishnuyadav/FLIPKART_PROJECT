from django.urls import path

from app2.views import *

app_name="app2"

urlpatterns=[
    path("two/",two,name="two"),
    path("four/",four,name="four"),
    path('six/',six,name="six"),
]