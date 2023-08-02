from django.test import TestCase, Client
from django.urls import reverse


class OcLettingsSiteViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'oc_lettings_site/index.html')

    def test_trigger_error_view(self):
        response = self.client.get(reverse('sentrytest'))
        self.assertEqual(response.status_code, 500)
        self.assertTemplateUsed(response, 'error.html')
