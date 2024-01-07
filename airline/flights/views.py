from django.shortcuts import render
from .models import Passengers,Flight
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
  return render(request, "flights/index.html", {
    "flights": Flight.objects.all()
  })


def flight(request,flight_id):
  flight = Flight.objects.get(id=flight_id)
  return render(request, "flights/flight.html", {
      "flight": flight,
      "passengers":flight.passengers.all(),
      "non_passengers": Passengers.objects.exclude(flights=flight).all()
  }) 

def book(request, flight_id):
  if request.method == "POST":
    flight = Flight.objects.get(pk=flight_id)
    passenger = Passengers.objects.get(pk=int(request.POST["passenger"]))
    passenger.flights.add(flight)
    return HttpResponseRedirect("flight", args=(flight.id,))