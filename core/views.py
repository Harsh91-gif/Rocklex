from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomerInquiry


# HOME
def home_page_view(request):
    return render(request, "core/home_page.html")


# ABOUT
def about_page_view(request):
    return render(request, "core/about_page.html")


# PRODUCTS
def products_page_view(request):
    return render(request, "core/products_page.html")
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import CustomerInquiry


# HOME
def home_page_view(request):
    return render(request, "core/home_page.html")


# ABOUT
def about_page_view(request):
    return render(request, "core/about_page.html")


# PRODUCTS
def products_page_view(request):
    return render(request, "core/products_page.html")

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.conf import settings
from .models import CustomerInquiry


def contact_page_view(request):

    if request.method == "POST":

        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        city = request.POST.get("city")
        inquiry_type = request.POST.get("inquiry_type")
        message_text = request.POST.get("message")

        # ✅ Email validation
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Invalid email address ❌")
            return redirect("contact")

        # ✅ Save to DB
        CustomerInquiry.objects.create(
            name=name,
            phone=phone,
            email=email,
            city=city,
            inquiry_type=inquiry_type,
            message=message_text,
        )

        # ✅ Send BOTH Emails
        try:
            # 1️⃣ Email to ADMIN (you)
            send_mail(
                subject="New Contact Inquiry",
                message=f"""
New Inquiry Received:

Name: {name}
Phone: {phone}
Email: {email}
City: {city}
Type: {inquiry_type}

Message:
{message_text}
""",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            # 2️⃣ Email to USER (confirmation)
            send_mail(
                subject="Thank you for contacting Rocklex 💧",
                message=f"""
Hi {name},

Thank you for reaching out to Rocklex.

We have received your inquiry and our team will contact you shortly.

Your Details:
- Name: {name}
- Inquiry Type: {inquiry_type}

Regards,  
Rocklex Team
""",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )

        except Exception as e:
            print("Email Error:", e)
            messages.error(request, "Email sending failed ❌")
            return redirect("contact")

        messages.success(request, "Inquiry sent successfully ✅")
        return redirect("contact")

    return render(request, "core/contact_page.html")