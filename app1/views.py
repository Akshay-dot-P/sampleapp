from django.shortcuts import render ,redirect
from django.http import HttpResponseRedirect
from .forms import IndexForm

# Create your views here


def index(request):
    if request.method == 'POST':
        form = IndexForm(request.POST)
        if form.is_valid():
            note = form.cleaned_data['note']
            print(note)

    return render(request, "index.html")