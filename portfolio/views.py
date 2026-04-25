from django.shortcuts import render, redirect
from .models import Project, Messages
from .forms import MessageForm
from django.core.mail import send_mail
from blog.models import Blog


def set_language(request):
    lang = request.GET.get('lang', 'en')
    if lang in ('en', 'cs'):
        request.session['language'] = lang
    return redirect(request.META.get('HTTP_REFERER', '/'))


def home(request):
    lang = request.session.get('language', 'en')
    projects = Project.objects.all()
    blogs = Blog.objects.filter(language=lang).order_by('-date')[:3]
    return render(request, 'portfolio/home.html', {'projects': projects, 'blogs': blogs})


def contact(request):
    if request.method == 'GET':
        return render(request, 'portfolio/contact.html', {'form': MessageForm()})
    else:
        try:
            form = MessageForm(request.POST or None)
            form.save()
            send_mail(
                'Personal Website' + '-' + request.POST['subject'],
                'Message from: ' + request.POST['from_email'] + ' Message: ' + request.POST['message'],
                request.POST['from_email'],
                ['martinczarkowski@gmail.com'],
                fail_silently=False,
            )
            return render(request, 'portfolio/contact.html', {'message': form})
        except ValueError:
            return render(request, 'portfolio/contact.html', {'error': 'Something went wrong. Try again!'})
