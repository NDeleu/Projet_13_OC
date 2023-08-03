from django.test import TestCase, Client
from django.urls import reverse


class OcLettingsSiteViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        """
        Test that the 'index' view returns a status code of 200
            and uses the correct template.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'oc_lettings_site/index.html')

    def test_trigger_error_view(self):
        """
        Test that the 'sentrytest' view returns a status code of 500
            and uses the 'error.html' template.
        """
        response = self.client.get(reverse('sentrytest'))
        self.assertEqual(response.status_code, 500)
        self.assertTemplateUsed(response, 'error.html')
