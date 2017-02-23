from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.template import loader
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from .models import Message


def index(request):
    message_list = Message.objects.order_by('date')
    template = loader.get_template('index.html')
    context = {
        'message_list': message_list,
    }
    return HttpResponse(template.render(context, request))

# @login_required(login_url='login') 
@login_required 
def add_message(request):
    if request.user.is_authenticated():
        title = request.POST.get('title')
        text = request.POST.get('text')
        author = request.user
        new_message = Message(title=title, text=text, author=author)
        new_message.save()
        return HttpResponseRedirect('/')
   
    # message_list = Message.objects.order_by('date')
    # template = loader.get_template('index.html')
    # context = {
    #     'message_list': message_list,
    # }
    # return HttpResponse(template.render(context, request))
    
    # if request.method == 'POST':
    #     title = request.POST['title']
    #     text = request.POST['text']
    #     author = request.POST['author']
    #     new_message = Message(title=title, text=text, author=author)
    #     new_message.save()
    #     return HttpResponse(request, 'index.html', new_message)
        
        
        