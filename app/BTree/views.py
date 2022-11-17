"""
Views for the BTree APIs
"""
from rest_framework import viewsets

from core.models import Leaf
from BTree import serializers


class BTreeViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs."""
    serializer_class = serializers.BTreeSerializer
    queryset = Leaf.objects.all()