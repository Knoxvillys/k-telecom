from rest_framework import viewsets

from .models import Equipment
from .serializers import Equipment_form


class EquipmentView(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = Equipment_form

