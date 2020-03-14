from django.urls import path

from . import views

app_name = 'records'
urlpatterns = [
    path('add_contagion_site/<int:confirmed_case_id>', views.add_contagion_site, name='add_contagion_site'),
    path('map', views.map, name='map'),
    path('submit', views.submit, name='submit'),
    path('data', views.data, name='data'),
    path('confirmed', views.confirmed, name='confirmed_case'),
    path('', views.index, name='index')
]
