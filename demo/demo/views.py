from django.shortcuts import render,HttpResponse
from main.forms import *
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = StudentFrom(request.POST)
        if form.is_valid():
            # Process the form data
            pass
    else:
        form = StudentFrom()
    
    return render(request, 'home.html', {'form': form})