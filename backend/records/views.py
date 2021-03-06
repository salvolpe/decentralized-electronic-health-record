from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.serializers import serialize

from .forms import ConfirmedCaseForm, SpaceTimeFormset, ContagionSiteForm
from .models import ConfirmedCase, ContagionSite


def index(request):
    return HttpResponse("Recorcds Index")

def confirmed(request):
    if request.method == 'POST':
        form = ConfirmedCaseForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/records/')
    else:
        form = ConfirmedCaseForm()
    return render(request, 'records/confirmed_case.html', {'form' : form})

def add_contagion_site(request, confirmed_case_id):
    if request.method == 'POST':
        form = ContagionSiteForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['finished'] == False:
                return HttpResponseRedirect(f'/records/add_contagion_site/{confirmed_case_id}')
            else:
                return HttpResponseRedirect('/records/map')
    else:
        form = ContagionSiteForm()
    return render(request, 'records/add_contagion_site.html',
                  {'form' : form,
                   'confirmed_case_id' : confirmed_case_id})


def submit(request):
    template_name = 'records/submit.html'
    heading_message = 'Submit COVID-19 Case'
    if request.method == 'GET':
        formset = SpaceTimeFormset(request.GET or None)
    elif request.method == 'POST':
        formset = SpaceTimeFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                print(form.cleaned_data.get('location'), form.cleaned_data.get('time'))
                return HttpResponseRedirect('/records/')
    return render(request, template_name, {
        'formset' : formset,
        'heading' : heading_message
    })

def map(request):
    sites = ContagionSite.objects.all()
    points = [site.transmission_site for site in sites]
    print(points)
    return render(request, 'records/map.html', {'queryset' : points})

def data(request):
    sites = ContagionSite.objects.all()
    points = [site.transmission_site for site in sites]
    points_as_geojson = serialize('geojson', sites, geometry_field='transmission_site')
    return HttpResponse(points_as_geojson, content_type='json')

