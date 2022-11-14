from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings 


# Create your views here.
def index(request):
    return render (request, 'index.html', {})

    if request.method == 'POST':
         name = request.POST['name']
         email = request.POST['email']
         message = request.POST['message']

         # Send an email
         send_mail(             
             name, # subject
             message, # message
             email, # from email 
             settings.EMAIL_HOST_USER,
             ['camtude2018@gmail.com'], # TO email
             fail_silently=False
             )
         return render(request, 'index.html', {'name':name})
        
    else: 
        return render (request, 'index.html', {})


 