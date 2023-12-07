from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import UserSerializer
from .models import User

class UserListView(ListAPIView):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer

class UserDetailsView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
