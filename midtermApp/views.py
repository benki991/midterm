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
            name = "Jemwel"
            age = 21
            email = "jemwel@gmail.com"
            hobbies = {"Basketball", "Linux"}
            wait = True
        case '2':
            name = "Joswa"
            age = 100
            email = "shab-dealer@pdea.com"
            hobbies = {"Shab-"}
            wait = True
        case '3':
            name = "Stephen"
            age = 69
            email = "spidermansavecity@gmail.com"
            hobbies = {"Spider"}
            wait = True
        case '4':
            name = "Kevin"
            age = 21
            email = "kevinbarret.payos@gmail.com"
            hobbies = {"Sleep"}
            wait = True
        case _:
            wait = False

    context = {
        "data": {
            "id":id,
            "name": name,
            "age": age,
            "email": email,
            "hobbies": hobbies,
        },
    }     
    if wait == True:
        return HttpResponse(render(req, "profile.html", context))
    else:
        return HttpResponseRedirect("/")