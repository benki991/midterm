from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def home(req):
    context = {
        "id":[
            {"id": 1, "name": "Jemwel", "data": "Jose Rizal"},
            {"id": 2, "name": "Joshua", "data": "shao long bao"},
            {"id": 3, "name": "Stephen", "data": "spidigong"},
            {"id": 4, "name": "Kevin", "data": "im partially black"},
        ], 
    }
    return HttpResponse(render(req, "index.html", context))

def profile(req, id):
    wait = False
    match id:
        case '1':
            name = "Jemwel Jerald Salamida"
            age = 21
            email = "jemsadimalas@gmail.com"
            hobbies = {"Family Vehicle Operator", "Playing Basketball", "Making Music Snippets"}
            img = "jemwel"
            wait = True
        case '2':
            name = "Joshua Uy"
            age = 100
            email = "joshualex1234@gmail.com"
            hobbies = {"Sleeping", "Playing Video Games", "Playing Kalimba"}
            img = "joshua"
            wait = True
        case '3':
            name = "Stephen Morado"
            age = 21
            email = "stepenmorado27@gmail.com"
            hobbies = {"Watching Anime/Movies", "Playing Video Games", "Playing Guitar"}
            img = "stephen"
            wait = True
        case '4':
            name = "Kevin Barret Payos"
            age = 21
            email = "kevinbarret.payos@gmail.com"
            hobbies = {"Gym", "Programming", "Playing Video Games"}
            img = "kevin"
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
            "img": img,
        },
    }     
    if wait == True:
        return HttpResponse(render(req, "profile.html", context))
    else:
        return HttpResponseRedirect("/")