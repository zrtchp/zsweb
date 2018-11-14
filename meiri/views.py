from django.shortcuts import render
from .models import DataCs

def query_cs(request,qdate):
    datacs=DataCs.objects.filter(date=qdate)
    return render(request,'index.html',{'datacs':datacs,})
