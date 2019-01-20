from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import AccessRecord,Topic,Webpage
from . import forms
# Create your views here.

def index(request):
    a_records = AccessRecord.objects.order_by("date")
    dict = {"a_records":a_records}
    return render(request,'second_app/index.html',context=dict)

def index2(request):
    return HttpResponse("<h1>Vardhan</h1>")

def form_name(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print('hi')
            print('NAME : ' + form.cleaned_data['name'])
            print('EMAIL : ' + form.cleaned_data['email'])
            print('TEXT : ' + form.cleaned_data['text'])
    dict = {'form':form}
    return render(request,'second_app/form.html',context=dict)
