from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def home(req):
    context = {
        "id":[
            {"id": 1, "name": "Jemwel", "data": "Jose Rizal"},
            {"id": 2, "name": "Joswa", "data": "shao long bao"},
            {"id": 3, "name": "Stephen", "data": "spidigong"},
            {"id": 4, "name": "Kevin", "data": "im partially black"},
        ], 
    }
    return HttpResponse(render(req, "index.html", context))

def profile(req, id):
    wait = False
    match id:
        case '1':
            context = {
                "data": {
                    "id":id,
                    "name": "Jemwel",
                    "age": 21,
                    "hobbies": "Basketball",
                },
            }
            wait = True
        case _:
            wait = False
            
    if wait == True:
        return HttpResponse(render(req, "profile.html", context))
    else:
        return HttpResponseRedirect("/")