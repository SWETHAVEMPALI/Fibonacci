from django.test import TestCase
from .views import *
# Create your tests here.

class FibonacciApiTest(TestCase):
	
	def get_nth_number_Test(self):
		nthNumber = views.get_nth_number(6)
		self.assertIs(nthNumber,8)
