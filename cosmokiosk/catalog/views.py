from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import ClientWaiverForm, FeedbackForm, WaxingWaiverForm, ServicesForm
from .models import Client_Waiver, Services, Waxing_Waiver, Feedback, Profile_Instance
from django.utils import timezone
from functools import wraps


# Create your views here.
def index(request):
    return render(request, 'catalog/welcome.html') 


def signin_view(request):
    if request.method == "POST":
        form = ClientWaiverForm(request.POST)
        if form.is_valid():
            client_waiver = form.save(commit=False)
            client_waiver.date_time = timezone.now()
            client_waiver.save()
            print("--- DATA SUCCESSFULLY SAVED TO DATABASE ---")
            first_name = form.cleaned_data.get('first_name', '')
            last_name = form.cleaned_data.get('last_name', '')
            request.session['client_id'] = client_waiver.id
            request.session['saved_full_name'] = f"{first_name} {last_name}".strip()
            return redirect('services')
        else: 
            print("--- FORM VALIDATION FAILED ---")
            print(form.errors.as_data())
    else:
        form = ClientWaiverForm(initial={'date_time': timezone.now()})
    return render(request, 'catalog/sign-in.html', {'form': form})

def client_waiver_view(request):
    return signin_view(request)

def welcome_page(request):
    return render(request, 'catalog/welcome.html')
    
def services_page(request):
    if request.method == "POST":
        form = ServicesForm(request.POST)

        if form.is_valid():
            client_id = request.session.get('client_id')

            if client_id:
                client = Client_Waiver.objects.get(id=client_id)

                # Save the client's selected services FIRST
                service = form.save(commit=False)
                service.client_info = client
                service.save()

                # If they selected waxing, send them to the waxing waiver
                if service.waxing:
                    return redirect('waxing_waiver')

                # If they did NOT select waxing
                return redirect('welcome')

        else:
            print("SERVICE FORM INVALID")
            print(form.errors)

    else:
        form = ServicesForm()

    return render(
        request,
        'catalog/services.html',
        {'form': form}
    )


#this is the place for all the forms stuff
def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)

        if form.is_valid():
            feedback = form.save(commit=False)

            
            client_id = request.session.get('checkout_client_id')

            if client_id:
                try:
                    client = Client_Waiver.objects.get(id=client_id)

                    feedback.client_info = client
                    feedback.save()

                    
                    client.checked_out = True
                    client.save()

                except Client_Waiver.DoesNotExist:
                    
                    feedback.save()

            else:
                
                feedback.save()

           
            request.session.pop('checkout_client_id', None)

           
            return redirect('welcome')

        else:
            print("FEEDBACK FORM INVALID")
            print(form.errors)

    else:
        form = FeedbackForm()

    return render(
        request,
        'catalog/feedback.html',
        {'form': form}
    )

def waiver_view(request):
    if request.method == "POST":
        print("USER SUBMITTED")
        form = WaxingWaiverForm(request.POST)

        if form.is_valid():
            print("VALID")

            waiver = form.save(commit=False)

            client_id = request.session.get('client_id')

            if client_id:
                try:
                    waiver.client_info = Client_Waiver.objects.get(
                        id=client_id
                    )
                except Client_Waiver.DoesNotExist:
                    pass

            waiver.save()

            return redirect('welcome')

        else:
            print("INVALID", form.errors)

    else:
        form = WaxingWaiverForm()

    full_name = request.session.get('saved_full_name', '')

    return render(
        request,
        'catalog/waxing.html',
        {
            'form': form,
            'full_name': full_name
        }
    )



def checkout(request):

    clients = Client_Waiver.objects.filter(checked_out=False).order_by('first_name', 'last_name')

    if request.method == "POST":
        selected_client_id = request.POST.get("client_id")

        if selected_client_id:
            request.session["checkout_client_id"] = selected_client_id
            return redirect("feedback")

    return render(
        request,
        "catalog/checkout.html",
        {"clients": clients}
    )

def teacher_page(request):

    error_message = None

    if request.method == "POST":

        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")

        teacher = Profile_Instance.objects.filter(
            email_address__iexact=email,
            is_shop_instructor=True
        ).first()

        if teacher and teacher.check_password(password):

            request.session["teacher_id"] = teacher.id

            return redirect("teacher_dashboard")

        error_message = "Invalid email or password."

    return render(
        request,
        "catalog/teacher_sign_in.html",
        {"error_message": error_message}
    )


# Teacher authentication decorator
def teacher_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        teacher_id = request.session.get("teacher_id")

        if not Profile_Instance.objects.filter(
            id=teacher_id,
            is_shop_instructor=True
        ).exists():

            return redirect("teacher_sign_in")

        return view_func(request, *args, **kwargs)

    return wrapper


# Teacher dashboard
@teacher_required
def teacher_dashboard(request):

    clients = Client_Waiver.objects.filter(
        checked_out=False
    ).order_by('date_time')

    feedback_list = Feedback.objects.select_related(
        'client_info'
    ).order_by('-id')

    selected_feedback = None

    feedback_id = request.GET.get('feedback_id')

    if feedback_id:
        try:
            selected_feedback = Feedback.objects.select_related(
                'client_info'
            ).get(id=feedback_id)

        except Feedback.DoesNotExist:
            selected_feedback = None

    return render(
        request,
        'catalog/teacher-dashboard.html',
        {
            'clients': clients,
            'feedback_list': feedback_list,
            'selected_feedback': selected_feedback
        }
    )



def teacher_feedback(request):

    feedback_list = Feedback.objects.select_related(
        'client_info'
    ).order_by('-id')

    return render(
        request,
        'catalog/teacher-feedback.html',
        {
            'feedback_list': feedback_list
        }
    )
    
@teacher_required
def client_details(request, client_id):
    try:
        client = Client_Waiver.objects.get(id=client_id)
    except Client_Waiver.DoesNotExist:
        return redirect('teacher_dashboard')

    try:
        services = Services.objects.get(client_info=client)
    except Services.DoesNotExist:
        services = None

    try:
        waxing_waiver = Waxing_Waiver.objects.get(client_info=client)
    except Waxing_Waiver.DoesNotExist:
        waxing_waiver = None

    return render(
        request,
        'catalog/client-details.html',
        {
            'client': client,
            'services': services,
            'waxing_waiver': waxing_waiver
        }
    )