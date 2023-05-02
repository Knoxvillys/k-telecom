from rest_framework import serializers
    #ValidationError
import re

from .models import Equipment_type, Equipment


class Equipment_form(serializers.ModelSerializer):

    class Meta:
        model = Equipment
        fields = ('equipment_type_id', 'serial_number')

    # def __init__(self, *args, **kwargs):
    #     super(Equipment_form, self).__init__(*args, **kwargs)
    #
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control'

    def clean(self, data, value):
        number = data['serial_number']
        equip_id = value['equipment_type_id']
        equip_data = Equipment_type.objects.get(name_type=equip_id)
        mask = getattr(equip_data, 'mask_sn')
        
        new_mask_list = []
        
        for i in mask:
            if i == 'Z':
                new_mask_list.append(r'[-_@]')
            elif i == 'X':
                new_mask_list.append(r'[A-Z0-9]')
            elif i == 'A':
                new_mask_list.append(r'[A-Z]')
            elif i == 'a':
                new_mask_list.append(r'[a-z]')
            elif i == 'N':
                new_mask_list.append(r'[0-9]')

        new_mask_str = ''.join(new_mask_list)

        if re.search(new_mask_str, number) is None:
            raise serializers.ValidationError('Неверный серийный номер')

        elif Equipment.objects.filter(serial_number=number):
            raise serializers.ValidationError('Cерийный номер уже есть')

        else:
            return number