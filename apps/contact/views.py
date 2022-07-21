from django.shortcuts import render
from .models import *
from .forms import ContactForm


def contact(request):
    sbb = request.GET.get('sbb')
    if sbb:
        Subscribe.objects.create(email=sbb)
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    email = request.GET.get('email')
    if email:
        Subscribe.objects.create(email=email)
    ctx = {
        'form': form
    }
    return render(request, 'contact.html', ctx)


def about(request):
    email = request.GET.get('email')
    sbb = request.GET.get('sbb')
    if sbb:
        Subscribe.objects.create(email=sbb)
    if email:
        Subscribe.objects.create(email=email)
    return render(request, 'about.html')


