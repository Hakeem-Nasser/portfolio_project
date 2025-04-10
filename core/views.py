from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactSubmission
from django.core.mail import send_mail

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            ContactSubmission.objects.create(
                name=name,
                email=email,
                message=message
            )

            # Send email
            subject = f"New message from {name}"
            full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            send_mail(
                subject,
                full_message,
                None, 
                ['abdulnasserabdulhakeem@gmail.com'],  # Receiver's email
                fail_silently=False,
            )

            messages.success(request, 'Your message has been sent!')
            return redirect('core:contact')
        else:
            messages.error(request, 'Please fill all required fields.')

    return render(request, 'core/contact.html')
