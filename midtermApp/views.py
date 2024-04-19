from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def home(req):
    return HttpResponse(render(req, "index.html", context={"id":["Jemwel", "Stephen", "Joswa", "Kevin"]}))