from django.shortcuts import render, redirect
from .forms import Waxing_Waiver, ClientWaiverForm, Feedback_Questions, Feedback
from django.utils import timezone


# Create your views here.
def index(request):
    return render(request, 'catalog/welcome.html') 

def feedback_view(request):
    return render(request, 'catalog/feedback.html')


def signin_view(request):
    if request.method == "POST":
        form = ClientWaiverForm(request.POST)
        if form.is_valid():
            form.save()
            print("--- DATA SUCCESSFULLY SAVED TO DATABASE ---")
            return redirect('services')
        else: 
            print("--- FORM VALIDATION FAILED ---")
            print(form.errors.as_data())
    else:
        form = ClientWaiverForm(initial={'date_time': timezone.now()})
    return render(request, 'catalog/sign-in.html', {'form': form})


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


def client_waiver_view(request):
    return signin_view(request)


def feedback_view(request):
    if request.method == "POST":
        form = Feedback(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    
    else:
        form = Feedback()

    return render(request, 'catalog/feedback.html', {
        'form':form
    })
#Big L said to recieve the data from data and time
#Use time.now, so the server gets the time and the date