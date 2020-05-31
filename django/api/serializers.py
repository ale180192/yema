from django.contrib.auth import get_user_model
from django.db.models import ObjectDoesNotExist
from rest_framework.exceptions import APIException
from rest_framework.serializers import (
    ModelSerializer,
    RelatedField,
    IntegerField
)

from .models import (
    Appointment,
    Pediatrician
)

User = get_user_model()

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class PediatricianSerializer(ModelSerializer):
    
    class Meta:
        model = Pediatrician
        fields = '__all__'

class AppointmentsListSerializer(ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    pediatrician = PediatricianSerializer(many=False, read_only=True)

    class Meta:
        model = Appointment
        fields = ['pediatrician', 'user', 'commentary', 'datetime']
        extra_kwargs = {'commentary': {'read_only': False, 'required': True},
                        'pediatrician': {'required': True}}


class AppointmentCreateSerializer(ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    pediatrician = IntegerField(write_only=True, required=True)

    class Meta:
        model = Appointment
        fields = ['pediatrician', 'user', 'commentary', 'datetime']
        extra_kwargs = {'commentary': {'required': True}}

    def validate_pediatrician(self, value):
        try:
            return Pediatrician.objects.get(pk=value)
        except ObjectDoesNotExist:
           raise APIException(detail={'pediatrician': 'obj id not valid'})


