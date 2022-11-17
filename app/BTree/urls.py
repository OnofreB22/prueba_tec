"""
URL mappings for the recipe app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from BTree import views


router = DefaultRouter()
router.register('BTree', views.BTreeViewSet)

app_name = 'BTree'

urlpatterns = [
    path('', include(router.urls)),
]