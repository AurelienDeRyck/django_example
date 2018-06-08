from django.test import TestCase

# Create your tests here.
from ave_cesar.views import home


class TestCaseHome(TestCase):
    def setUp(self):
        pass

    def test_home(self):
        r = self.client.get('/')
        self.assertEqual(r.status_code, 200)
