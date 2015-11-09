import logging
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.views import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FileUploadParser, FormParser, JSONParser, MultiPartParser
from chat.models import Message
from chat.serializers import MessageSerializer, MessageShortSerializer



logger = logging.getLogger(__name__)



def registration(request):
    """
    Registration view
    """

    if request.user.is_authenticated():
        return redirect('home')
    registration_template = 'registration/registration.html'
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, registration_template, {'form': form})
    else:
        form = UserCreationForm()
        return render(request, registration_template, {'form': form})


def login(request, *args, **kwargs):
    """
    Authentication view. Changes session expiry time
    """
    if request.method == 'POST':
        if not request.POST.get('remember_me', None):
            request.session.set_expiry(0)
    return auth_login(request, *args, **kwargs)


def logout(request):
    """
    Log out view
    """
    auth_logout(request)
    return redirect('home')

def home(request):
    """
    Serving main page template
    """

    return render(request,'KIT_test/home.html')

### Api Views ###

class ListMessages(generics.ListAPIView):
    """
    API for listing all messages
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class CreateMessage(generics.CreateAPIView):
    """
    API for creating messages
    """
    permission_classes = (IsAuthenticated,)
    queryset = Message.objects.all()
    serializer_class = MessageShortSerializer
    parser_classes = (FormParser, MultiPartParser,JSONParser )

    def perform_create(self, serializer):
        instance = serializer.save(from_user=self.request.user)
        logger.info(
            'User "{0}" sent message : "{1}" on  {2}'.format(
                instance.from_user.username, instance.text.encode('utf-8'), instance.timestamp
            )
        )     

        
