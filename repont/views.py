import datetime
import json

from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from repont.forms import StatementForm, RepontForm
from repont.models import Repont, Statement


# Create your views here.
def index_view(request):
    template = "repont/index.html"
    context = {}
    return render(request,template,context)


def get_reponts(request):
    reponts = Repont.objects.all()
    features = []


    for repont in reponts:

        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [repont.lon, repont.lat],
            },
            "properties": {
                "id": repont.pk,
                "name": repont.name,
                "last_report": repont.get_state().created_at.strftime("%Y-%m-%d %H:%M:%S") if repont.get_state() else "None",
                "description": repont.description,
                "state": repont.get_state_value(),

            },
        })

    geojson_data = {
        "type": "FeatureCollection",
        "features": features,
    }

    return JsonResponse(geojson_data)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def repont_view(request,pk):
    repont = Repont.objects.get(id=pk)
    form = StatementForm()
    statements = repont.get_statements.all().order_by("-created_at")

    template = "repont/view.html"

    if request.method == "POST":
        form = StatementForm(request.POST)
        if form.is_valid():
            print("[*] valid form", form)
            statement = form.save(commit=False)
            statement.repont = repont
            print(request.POST.get("status"))
            statement.state = request.POST.get("status")
            statement.ip = get_client_ip(request)
            statement.created_at = datetime.datetime.now()
            statement.save()
            messages.success(request,message="Bejelentés sikeres")
            return redirect("index")

    context = {
        "repont":repont,
        "form":form,
        "statements":statements

    }
    return render(request,template,context)


def info_view(request):
    template = "repont/info.html"
    context = {}
    return render(request,template,context)


def add_repont_view(request):
    template = "repont/add_repont.html"
    form = RepontForm()

    if request.method == "POST":
        form = RepontForm(request.POST)
        if form.is_valid():
            repont = form.save(commit=False)
            repont.created_ip = get_client_ip(request)
            repont.created_at = datetime.datetime.now()
            repont.lat = request.POST.get("lat")
            repont.lon = request.POST.get("lon")
            repont.save()
            messages.success(request,message="Sikeres rögzítés")
            return redirect("index")

    context = {
        "form":form
    }
    return render(request,template,context)