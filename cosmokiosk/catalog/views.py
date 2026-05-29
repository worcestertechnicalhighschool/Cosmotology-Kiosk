from django.shortcuts import render, redirect
from .forms import Waxing_Waiver, Client_Waiver


# Create your views here.
def index(request):
    return render(request, 'catalog/welcome.html') 

def feedback_view(request):
    return render(request, 'catalog/feedback.html')

def signIn_view(request):
    return render(request, 'catalog/sign-in.html')

def welcome_page(request):
    return render(request, 'catalog/welcome.html')
    
def services_page(request):
    return render(request, 'catalog/services.html')




#this is the place for all the forms stuff

def waiver_view(request):
    if request.method == "POST":
        form = Waxing_Waiver(request.POST)

        if form.is_valid():
            form.save()
            return redirect
    else:
        form = Waxing_Waiver()
    return render(request, 'waiver_template.html', {'form':form})

def client_view(request):
    if request.method == "POST":
        form = Client_Waiver(request.POST)

        if form.is_valid():
            form.save()
            return redirect
    else:
        form = Client_Waiver()
    return render(request, 'sign-in.html', {'form':form})