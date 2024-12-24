from django.shortcuts import render, redirect
from .forms import SendEmailForm
from django.contrib import messages
#email imports
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    if request.method == 'POST':
        form = SendEmailForm(request.POST)
        if form.is_valid():
            # Save the form data
            form.save()
            
            # Get the email and message from the form
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Send the email
            send_mail(
                'Your Subject Here',  # Subject of the email
                message,              # Message body
                settings.DEFAULT_FROM_EMAIL,  # From email (set in settings.py)
                [email],              # Recipient list
                fail_silently=False,  # Raise an error if sending fails
            )
            
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('home')
    else:
        form = SendEmailForm()
    
    context = {
        'form': form,
    }
    return render(request, 'app/home.html', context)

