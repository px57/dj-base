from django.db import models
from kernel.models.base_metadata_model import BaseMetadataModel
from profiles.models import Profile
from django.forms import model_to_dict


class ChatRoom(BaseMetadataModel):
    """
        A chatroom.
    """
    name = models.CharField(max_length=255)

    def serialize(self, request, serializer_type='little'):
        """
            @description: Serialize the message.
        """
        serialized = model_to_dict(self)
        return serialized

class Message(BaseMetadataModel):
    """A message in a chatroom."""
    content = models.TextField()

    chatroom = models.ForeignKey(
        ChatRoom,
        on_delete=models.CASCADE,
        related_name='messages',
        null=True,
        blank=True
    )

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='messages'
    )

    def serialize(self, request):
        """
            @description: Serialize the message.
        """
        serialized = model_to_dict(self)
        serialized['profile'] = self.profile.serialize(request, serializer_type='little')
        return serialized

class ChatRoomRaccordedToUser(BaseMetadataModel):
    """
        @description: 
    """
    chatroom = models.ForeignKey(
        ChatRoom,
        on_delete=models.CASCADE,
        related_name='chatroom_raccorded_to_user'
    )

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='chatroom_raccorded_to_user'
    )

    def serialize(self, request):
        """
            @description: Serialize the message.
        """
        serialized = model_to_dict(self)
        serialized['profile'] = self.profile.serialize(request, serializer_type='little')
        serialized['chatroom'] = self.chatroom.serialize(request, serializer_type='little')
        return serialized