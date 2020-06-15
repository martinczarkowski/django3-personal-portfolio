from django.shortcuts import render
from .models import Project, Messages
from .forms import MessageForm
from django.core.mail import send_mail

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects })

def contact(request):
    if request.method == 'GET':
        return render(request, 'portfolio/contact.html', {'form':MessageForm()})
    else:
        try:
            form = MessageForm(request.POST or None)
            form.save()
            # send email
            send_mail(
                'Personal Website' + '-' + request.POST['subject'], # subject
                'Message from: ' + request.POST['from_email'] + ' Message: ' +  request.POST['message'], # message
                request.POST['from_email'], # from email
                ['martinczarkowski@gmail.com'], # to email
                fail_silently=False,
            )
            return render(request, 'portfolio/contact.html', {'message':form})
        except ValueError:
            return render(request, 'portfolio/contact.html', {'error':MessageForm(), 'error':'Something is whong. Try again!'})
        
        
