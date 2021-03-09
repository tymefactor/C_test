from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.

def index(request):
    now = datetime.datetime.now()
    return render(request, "Pay_day/index.html", {
        "Pay_day": now.day == 25
    })