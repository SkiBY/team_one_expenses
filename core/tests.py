from django.test import TestCase
from core.models import *
from core.views import get_full_data, get_account_data

class CoreTest(TestCase):
	"""docstring for ClassName"""
	def setUp(self):
		f= Currency.objects.create(name='Доллары', currency_code='USD', code='$')
		Account.objects.create(name='Мой счет',currency=f, amount=1000)
		
	def test_get_account_data(self):
		a = Account.objects.get(name='Мой счет')
		self.assertEqual(get_account_data(a.id)['total'], 1000)
