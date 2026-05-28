from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'catalog/welcome.html') 

def feedback_view(request):
    return render(request, 'catalog/feedback.html')

def signIn_view(request):
    return render(request, 'catalog/sign-in.html')

def welcome_page(request):
    return render(request, 'catalog/welcome.html')