# Importamos diccionarios
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

# Definimos las funciones
def index(request):
    return render(request, "index.html", {})

def portfolio(request):
    return render(request, "portfolio.html", {})

def mensaje(request):
    return render(request, "mensaje.html", {})

def contact(request):
    if request.method == "POST":
        name =request.POST['nombre']
        email =request.POST['email']
        subject = 'Pedido de informacion Vicky Bijou'
        message =request.POST['mensaje']

        template = render_to_string('email_template.html', {
            'name': name,
            'email': email,
            'message': message
        })

        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['MAIL_QUE_ENVIA ACA']
        )

        email.fail_silently = False
        email.send()

        messages.success(request, 'Se ha enviado tu mansaje!')
        return redirect('mensaje')
    
