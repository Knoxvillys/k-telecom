from django.db import models


class Equipment_type(models.Model):
    equipment_type = models.CharField(max_length=30, verbose_name='Тип оборудования')
    mask_sn = models.TextField(verbose_name='Маска SN')


class Equipment(models.Model):
    equipment_type_id = models.ForeignKey(Equipment_type, on_delete=models.CASCADE)
    serial_number = models.IntegerField()
    
    