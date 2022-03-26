from .views import inbox, individual_message, new_message
from django.urls import path

app_name = 'messages'

urlpatterns = [
    path('inbox', inbox, name='inbox'),
    path('read/<int:pk>/', individual_message, name='read'),
    path('new', new_message, name='new'),
]
