from django.test import SimpleTestCase
from django.urls import reverse, resolve
from lettings import views


class LettingsUrlsTest(SimpleTestCase):
    def test_index_url_resolves(self):
        url = reverse('lettings:index')
        self.assertEqual(resolve(url).func, views.index)

    def test_letting_url_resolves(self):
        url = reverse('lettings:letting', args=[1])
        self.assertEqual(resolve(url).func, views.letting)
