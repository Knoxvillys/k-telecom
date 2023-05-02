from rest_framework import routers

# from django.contrib import admin
# from django.urls import path

from mask_app.views import EquipmentView

router = routers.SimpleRouter()

router.register('equipment', EquipmentView, basename='equipment')
urlpatterns = router.urls