from django.test import TestCase
from .models import Stock
# Create your tests here.

class StockTestCase(TestCase):
    def setUp(self):
        Stock.objects.create(Codigo="ITUB4", Preço=45, Quantidade=10, Data=2021-12-27 )

    def test_stock_date(self):
        
        itau = Stock.objects.get(name="ITUB4")
        self.assertEqual(itau.Data, 2021-12-27)