from django.urls import path
from .views import *

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('details/',UserDetailsView.as_view(), name='user_details')
]
