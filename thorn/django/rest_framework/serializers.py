"""DRF serializers."""
from __future__ import absolute_import, unicode_literals

from action_serializer import ModelActionSerializer
from rest_framework import serializers

from thorn.django.models import Subscriber

__all__ = ['SubscriberSerializer']


class SubscriberSerializer(serializers.HyperlinkedModelSerializer, ModelActionSerializer):
    """Serializer for :class:`~thorn.django.models.Subscriber`."""

    subscription = serializers.HyperlinkedIdentityField(
        view_name='webhook:detail',
        lookup_url_kwarg='uuid', lookup_field='uuid',
    )
    id = serializers.UUIDField(source='uuid', read_only=True)
    user = serializers.IntegerField(source='user.pk', default=None)

    class Meta:
        """Serializer configuration."""

        model = Subscriber
        fields = (
            'event', 
            'url', 
            'content_type', 
            'user',
            'id', 
            'created_at', 
            'updated_at', 
            'subscription',
            'hmac_secret', 
            'hmac_digest',
            'username',
            'password'
        )
        action_fields = {'list': {'fields': (
            'event', 
            'url', 
            'content_type', 
            'user',
            'id', 
            'created_at', 
            'updated_at', 
            'subscription',
            'username',
            'password'
        )},
        'retrieve': {'fields': (
            'event', 
            'url', 
            'content_type', 
            'user',
            'id', 
            'created_at', 
            'updated_at', 
            'subscription',
            'username',
            'password'
        )},}
        
        read_only_fields = ('id', 'created_at', 'updated_at', 'subscription')

# class SubscriberListSerializer(serializers.HyperlinkedModelSerializer):
#     """Serializer for :class:`~thorn.django.models.Subscriber`."""

#     subscription = serializers.HyperlinkedIdentityField(
#         view_name='webhook:detail',
#         lookup_url_kwarg='uuid', lookup_field='uuid',
#     )
#     id = serializers.UUIDField(source='uuid', read_only=True)
#     user = serializers.IntegerField(source='user.pk', default=None)

#     class Meta:
#         """Serializer configuration."""

#         model = Subscriber
#         fields = (
#             'event', 
#             'url', 
#             'content_type', 
#             'user',
#             'id', 
#             'created_at', 
#             'updated_at', 
#             'subscription',
#             'username',
#             'password'
#         )
