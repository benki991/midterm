from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def home(req):
    context = {
        "id":[
            {"name": "Jemwel", "data": "Jose Rizal"},
            {"name": "Joswa", "data": "shao long bao"},
            {"name": "Stephen", "data": "spidigong"},
            {"name": "Kevin", "data": "im partially black"},
        ], 
    }
    return HttpResponse(render(req, "index.html", context))