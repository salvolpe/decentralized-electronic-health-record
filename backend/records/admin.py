from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import ConfirmedCase, ContagionSite

@admin.register(ConfirmedCase)
class ConfirmedCaseAdmin(OSMGeoAdmin):
    list_display = ['location', 'estimated_date_contracted', 'date_confirmed']

@admin.register(ContagionSite)
class ContagionSiteAdmin(OSMGeoAdmin):
    list_display = ['confirmed_case', 'transmission_site', 'start_time', 'end_time']
