from django.test import SimpleTestCase
from django.urls import reverse, resolve
from profiles import views


class ProfilesUrlsTest(SimpleTestCase):
    def test_index_url_resolves(self):
        """
        Test that the URL pattern for the index view resolves
            to the correct view function.
        """
        url = reverse('profiles:index')
        self.assertEqual(resolve(url).func, views.index)

    def test_profile_url_resolves(self):
        """
        Test that the URL pattern for the profile view with a username
            as an argument resolves to the correct view function.
        """
        url = reverse('profiles:profile', args=["testuser"])
        self.assertEqual(resolve(url).func, views.profile)
