from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q

from .forms import NewMessageForm
from .models import Message

# Create your views here.
@login_required
def inbox(request, *args, **kwargs):
    logged_in_user = request.user.username
    messages = Message.objects.filter(Q(sender__iexact=logged_in_user)|Q(recipient__iexact=login_required()))
    context = {
        'inboxes': messages
    }
    return render(request, 'messages_app/inbox.html', context=context)


@login_required
def individual_message(request, *args, **kwargs):
    message_id = kwargs['pk']
    message = Message.objects.get(pk=message_id)
    message.read = True
    message.save()
    message.get_predictions()
    return render(request, 'messages_app/read.html', {'message':message})


@login_required
def new_message(request):
    if request.method == 'POST':
        form = NewMessageForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            sender = request.user.username
            recipient = form.cleaned_data['recipient']
            content = form.cleaned_data['content']
            subject = form.cleaned_data['subject']
            Message.objects.create(sender=sender, recipient=recipient, subject=subject, content=content)
            return HttpResponseRedirect('/messages/inbox')
    else:
        form = NewMessageForm()
    return render(request, 'messages_app/new_message.html', {'form': form})
