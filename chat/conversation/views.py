from .models import Conversation
from rest_framework.response import Response
from user.models import User
from .serializers import ConversationSerializer,ConversationListSerializer
from django.db.models import Q
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

# Create your views here.
class ConversationView(ListCreateAPIView):
    serializer_class = ConversationSerializer

    def get_queryset(self):
        user = self.request.user
        return Conversation.objects.filter(Q(initiator=user) | Q(receiver=user))
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        data = request.data
        username = data['receiver']
        try:
            participant = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'message': 'You cannot chat with a non existent user'})

        conversation = Conversation.objects.filter(Q(initiator=self.request.user, receiver=participant) |
                                                Q(initiator=participant, receiver=self.request.user))
        if conversation.exists():
            return Response(self.serializer_class(instance=conversation).data)
        else:
            conversation = Conversation.objects.create(initiator=self.request.user, receiver=participant)
            return Response(self.serializer_class(instance=conversation).data)
        
class ConversationDetailsView(RetrieveAPIView):
    serializer_class = ConversationListSerializer

    def get_queryset(self):
        user = self.request.user
        return Conversation.objects.filter(Q(initiator=user) | Q(receiver=user))
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
