from django.shortcuts import render


# Create your views here.
def home(request):
	return render(request, 'mainapp/base.html', {})

def dashboard(request):
	return render(request, 'mainapp/dashboard.html', {})


def area(request):
	return render(request, 'mainapp/area.html', {})

def water(request):
	return render(request, 'mainapp/water.html', {})