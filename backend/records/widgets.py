from django.contrib.gis import forms

class XDSoftDateTimePickerInput(forms.DateTimeInput):
    template_name = 'records/widgets/xdsoft_datetimepicker.html'
