from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils import timezone
from .models import Message
from .forms import MessageForm


def index(request):
    message_list = Message.objects.order_by('date')
    template = loader.get_template('billboard/index.html')
    context = {
        'message_list': message_list,
    }
    return HttpResponse(template.render(context, request))

def add_message(request):
    title = request.POST.get('title')
    text = request.POST.get('text')
    author = request.POST.get('author')
    new_message = Message(title=title, text=text, author=author)
    new_message.save()
    return HttpResponseRedirect('/')

   