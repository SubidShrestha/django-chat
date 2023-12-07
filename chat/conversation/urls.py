from django.urls import path
from .views import *

urlpatterns = [
    path('conversation/',ConversationView.as_view(),name="conversation"),
    path('conversation/details/<int:id>',ConversationDetailsView.as_view(),name="conversation_details"),
]
