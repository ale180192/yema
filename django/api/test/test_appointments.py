from datetime import datetime

from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from api.models import (
	Appointment,
	Pediatrician
)
from app.core.lib_test import ApiUserTest

User = get_user_model()

class AppointmentsTest(ApiUserTest):

	def create_pediatrician(self):
		return Pediatrician.objects.create(email='test@test.com', name='pediatrician test')

	def test_create_appointment(self):
		"""
		Ensure we can create a new appointment.
		"""
		ped = self.create_pediatrician()
		url = reverse('api:appointments-create')
		data = {"user": self.user.id, "pediatrician": ped.id, "commentary": "test commentary", "datetime": datetime.now()}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Appointment.objects.count(), 1)
		self.assertEqual(Appointment.objects.get().commentary, 'test commentary')