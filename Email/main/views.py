from django.shortcuts import render,redirect
from .forms import SendForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages



def home(request):
    form = SendForm()

    if request.method =='POST':
        form=SendForm(request.POST)
        if form.is_valid():
             subject = request.POST['subject']
        message = request.POST['message']
        email=request.POST['email']
        recipient = form.cleaned_data.get('email')
        send_mail(subject, 
              message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
        messages.success(request, 'The mail was sent Successfully')
        return redirect('home')

    context ={
        'form':form
       
    }

    return render(request, 'home.html',context)


