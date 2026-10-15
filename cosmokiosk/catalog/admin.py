
from django.contrib import admin
from django import forms

from .models import (
    Profile_Instance,
    Client_Waiver,
    Feedback_Questions,
    Feedback,
    Waxing_Waiver,
    Services
)


# Form for creating and editing teacher profiles



class ProfileInstanceAdminForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput(render_value=False),
        required=False,
        help_text="Enter a new password, or leave blank to keep the current password."
    )

    class Meta:
        model = Profile_Instance
        exclude = ["password"]

    def save(self, commit=True):
        profile = super().save(commit=False)

        new_password = self.cleaned_data.get("password")

        if new_password:
            profile.set_password(new_password)

        if commit:
            profile.save()

        return profile

# Admin for teacher profiles
class Profile_Instance_Admin(admin.ModelAdmin):

    form = ProfileInstanceAdminForm

    list_display = (
        "email_address",
        "password_status",
        "first_name",
        "last_name",
        "is_student",
        "is_shop_instructor",
    )

    readonly_fields = ("password_status",)

    @admin.display(description="Password")
    def password_status(self, obj):
        if obj.password:
            return "Password is set"
        return "No password set"

    list_per_page = 25

# Admin for client waivers
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "date_time"
    )
    list_per_page = 25


# Admin for feedback questions
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question", "question_text")
    list_per_page = 25


# Admin for feedback responses
class ResponsesAdmin(admin.ModelAdmin):
    list_display = (
        "client_info",
        "q1",
        "q2",
        "q3",
        "q4",
        "q5",
        "q6",
        "q7",
        "q8",
        "feedback_message"
    )
    list_per_page = 25


# Admin for waxing waivers
class WaxingAdmin(admin.ModelAdmin):
    list_display = (
        "medicine",
        "allergy",
        "soap_use",
        "exposed",
        "health_issues",
        "agreement"
    )
    list_per_page = 25


# Admin for services
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "client_info",
        "perm",
        "color",
        "hairstyle",
        "waxing",
        "nails"
    )
    list_per_page = 25


# Register models with Django admin
models_and_admins = [
    (Profile_Instance, Profile_Instance_Admin),
    (Client_Waiver, ClientAdmin),
    (Feedback_Questions, QuestionAdmin),
    (Feedback, ResponsesAdmin),
    (Waxing_Waiver, WaxingAdmin),
    (Services, ServiceAdmin),
]

for model, admins in models_and_admins:
    admin.site.register(model, admins)
