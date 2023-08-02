from django.test import SimpleTestCase
from django.urls import reverse, resolve
from oc_lettings_site import views


class OcLettingsSiteUrlsTest(SimpleTestCase):
    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, views.index)

    def test_trigger_error_url_resolves(self):
        url = reverse('sentrytest')
        self.assertEqual(resolve(url).func, views.trigger_error)
