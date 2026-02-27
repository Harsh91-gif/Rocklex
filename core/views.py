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


# CONTACT
def contact_page_view(request):

    if request.method == "POST":

        CustomerInquiry.objects.create(
            name=request.POST.get("name"),
            phone=request.POST.get("phone"),
            email=request.POST.get("email"),
            city=request.POST.get("city"),
            inquiry_type=request.POST.get("inquiry_type"),
            message=request.POST.get("message"),
        )

        messages.success(request, "Inquiry sent successfully ✅")
        return redirect("contact")

    return render(request, "core/contact_page.html")