from django.test import SimpleTestCase
from django.urls import reverse, resolve
from lettings import views


class LettingsUrlsTest(SimpleTestCase):
    def test_index_url_resolves(self):
        """
        Test that the URL for the 'index' view resolves
            to the correct view function.
        """
        url = reverse('lettings:index')
        self.assertEqual(resolve(url).func, views.index)

    def test_letting_url_resolves(self):
        """
        Test that the URL for the 'letting' view resolves
            to the correct view function with an argument.
        """
        url = reverse('lettings:letting', args=[1])
        self.assertEqual(resolve(url).func, views.letting)
