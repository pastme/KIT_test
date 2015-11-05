from django.conf.urls import include, url
from chat import views

# Create a router and register our viewsets with it.


urlpatterns = [
    url(r'^api/messages/list/$', views.ListMessages.as_view(), name='api_message_list'),
    url(r'^api/messages/create/$', views.CreateMessage.as_view(), name='api_message_create'),
    url(r'^registration/$', 'chat.views.registration', name='registration'),
    url(r'^signin/$', 'chat.views.login',
    {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', 'chat.views.logout', name='logout'),
    url(r'^home/$', 'chat.views.home', name = 'home'),

]
