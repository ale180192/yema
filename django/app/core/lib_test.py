from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

User = get_user_model()

class ApiUserTest(APITestCase):
	username = 'root@root.com'
	password = 'root'
	
	def setUp(self):
		super().setUp()
		self.user = User.objects.create(email=self.username)
		self.user.set_password(self.password)
		self.user.save()
		self.token = Token.objects.create(user=self.user)
		self.token.save()
		self.client.credentials( HTTP_AUTHORIZATION = 'Bearer {}'.format(self.token) )