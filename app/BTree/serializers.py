"""
Serializers for recipe APIs
"""
from rest_framework import serializers

from core.models import Leaf


class BTreeSerializer(serializers.ModelSerializer):
    """Serializer for BTrees"""

    class Meta:
        model = Leaf
        fields = ['id', 'data', 'left', 'right']
        read_only_fields = ['id']