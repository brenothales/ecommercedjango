from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import View, TemplateView


from .forms import ContactForm



# def index(request):
#     return render(request, "index.html")

class IndexView(TemplateView):
# utilizando class based views
    template_name = 'index.html'

index = IndexView.as_view()


def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)