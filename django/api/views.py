from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import APIException

from app.core.pagination import CustomNumberPagination
from app.core.auth import CustomTokenAuthentication
from api.models import (
    Appointment,
    Pediatrician
)
from .serializers import (
    AppointmentCreateSerializer,
    AppointmentsListSerializer,
    PediatricianSerializer
)

class HealthView(APIView):
    def get(self, request):
        return Response([], 200)

class BaseAppointmentListView(ListAPIView):
    authentication_classes = [CustomTokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    pagination_class = CustomNumberPagination

class BaseAppointmentCreateView(CreateAPIView):
    authentication_classes = [CustomTokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    pagination_class = CustomNumberPagination


class AppointmentsListView(BaseAppointmentListView):
    serializer_class = AppointmentsListSerializer
    queryset  = Appointment.objects.all()
    

class AppointmentsCreateView(BaseAppointmentCreateView):
    serializer_class = AppointmentCreateSerializer
    queryset  = Appointment.objects.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def post(self, request):
        ser = AppointmentCreateSerializer(data=request.data)
        if ser.is_valid(raise_exception=True):
            appointment = self.perform_create(ser)
            ser_response = AppointmentsListSerializer(appointment)
            return Response(data=ser_response.data, status=status.HTTP_201_CREATED)