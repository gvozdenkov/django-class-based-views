from django.http import HttpResponse
from django.utils.timezone import datetime
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView


from . forms import MessageForm
from . models import Message

# Create your views here.

def home(request):
    return HttpResponse("Hello, Django!")

class ThankyouView(TemplateView):
    template_name = "hello/thank-you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["custom_message"] = "sending data successfull"
        return context

class MessageView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'hello/hello-there.html'

class MessageListView(ListView):
    template_name = "hello/message-list.html"
    model = Message
    context_object_name = "messages"

class MessageDetailView(DetailView):
    template_name = "hello/message-detail.html"
    model = Message
    context_object_name = "msg"