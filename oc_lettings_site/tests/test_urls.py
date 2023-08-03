from django.test import SimpleTestCase
from django.urls import reverse, resolve
from oc_lettings_site import views


class OcLettingsSiteUrlsTest(SimpleTestCase):
    def test_index_url_resolves(self):
        """
        Test that the URL for the 'index' view resolves
            to the correct view function.
        """
        url = reverse('index')
        self.assertEqual(resolve(url).func, views.index)

    def test_trigger_error_url_resolves(self):
        """
        Test that the URL for the 'sentrytest' view resolves
            to the correct view function.
        """
        url = reverse('sentrytest')
        self.assertEqual(resolve(url).func, views.trigger_error)
