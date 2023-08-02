from django.test import SimpleTestCase
from django.urls import reverse, resolve
from profiles import views


class ProfilesUrlsTest(SimpleTestCase):
    def test_index_url_resolves(self):
        url = reverse('profiles:index')
        self.assertEqual(resolve(url).func, views.index)

    def test_profile_url_resolves(self):
        url = reverse('profiles:profile', args=["testuser"])
        self.assertEqual(resolve(url).func, views.profile)
