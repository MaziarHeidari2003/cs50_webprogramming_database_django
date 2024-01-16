from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
  if request.user.is_authenticated:
    return HttpResponseRedirect(reverse("login"))
  
def login(request):
  return render(request, "")  