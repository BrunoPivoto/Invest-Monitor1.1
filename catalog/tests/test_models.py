from django.test import TestCase

class YourTestClass(TestCase):
    @classmethod
    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)