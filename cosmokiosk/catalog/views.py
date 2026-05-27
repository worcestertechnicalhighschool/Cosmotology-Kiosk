from django.shortcuts import render
from djago.shortcuts import render

# Create your views here.
def index(request):
    pass

def feedback_view(request):
    return render(request, 'feedback.html')